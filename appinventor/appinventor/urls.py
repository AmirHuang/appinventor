"""appinventor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import xadmin
from django.urls import path, include, re_path
from django.views.static import serve
from appinventor.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from users.views import PictureCodeView, UserViewset
from cases.views import CasesListViewSet, CategoryViewset, HotCategoryView, HotSearchsViewset
from cases.views import BannerViewset

router = DefaultRouter()  # 利用了ViewSet的重载as_view()方法进行请求方法和处理函数的动态绑定（简单好用，只需要逐一register，然后urls函数即可）

router.register(r'users', UserViewset, base_name="users")  # 用户的相关操作
router.register(r'cases', CasesListViewSet, base_name="cases")  # 案例列表的相关操作
router.register(r'categorys', CategoryViewset, base_name="categorys")  # 案例类别的相关操作
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")  # 热搜案例的相关操作
router.register(r'banners', BannerViewset, base_name="banners")  # 轮播图的相关操作

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),

    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # drf 文档 title 自定义
    path('docs', include_docs_urls(title='Amir')),
    # drf 入口
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'picturecodes/', PictureCodeView.as_view(), name='picturecodes'),  # 获取验证码图片
    re_path(r'captcha/', include('captcha.urls')),  # django-simple-captcha模块用于获取图片的URL
    re_path(r'api-token-auth/', views.obtain_auth_token),  # drf自带的token认证模式（一般称为Session模式）
    re_path(r'login/', obtain_jwt_token),  # jwt的认证接口（较之drf自带的认证模式，占用的服务器端资源更少，安全性更高）
    re_path(r'', include(router.urls)),  # 将调用刚才注册到router的各个ViewSet的as_view()方法，得到最终的URL映射配置
    re_path(r'hotcategory', HotCategoryView.as_view()),  # 获取案例数量最多的若干个案例类型
]
