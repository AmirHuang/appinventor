from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.throttling import UserRateThrottle
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .models import Cases, CasesCategory, HotSearchWords, Banner
from .filters import CasesFilter
from .serializers import GetCasesSerializer, PostCasesSerializer, CategorySerializer, HotWordsSerializer, \
    BannerSerializer
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework import views
from django.db.models import Count


class CasesPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class CasesListViewSet(viewsets.ModelViewSet):
    # 案例列表页, 分页， 搜索， 过滤， 排序
    throttle_classes = (UserRateThrottle,)
    queryset = Cases.objects.all().order_by('-add_time')
    pagination_class = CasesPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = CasesFilter
    search_fields = ('name', 'cases_brief', 'cases_desc')
    ordering_fields = ('click_num', 'add_time')

    def get_serializer_class(self):
        # 当进行的是创建新案例或修改旧案例时
        if self.action == 'create' or self.action == 'update':
            return PostCasesSerializer
        else:
            return GetCasesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        case = serializer.save()
        re_dict = serializer.data
        re_dict['id'] = case.id
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        案例分类列表数据
    retrieve:
        获取案例分类详情
    """
    queryset = CasesCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class HotCategoryView(views.APIView):
    # 获取案例类型的案例数量排行榜
    def get(self, request):
        hot_category_list = CasesCategory.objects.annotate(num_cases=Count('cases')).values(
            'num_cases',
            'name',
            'parent_category_id').order_by('-num_cases')[:9]
        return Response(hot_category_list, status=status.HTTP_200_OK)


class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取案例轮播图列表
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer
