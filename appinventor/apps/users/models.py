from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    # 自定义用户
    name = models.CharField('姓名', max_length=30, null=True, blank=True)
    birthday = models.DateField('出生年月', null=True, blank=True)
    gender = models.CharField('性别', choices=(('male', u'男'), ('famale', u'女')),
                              default='famale', max_length=6, null=True, blank=True)
    mobile = models.CharField('电话', null=True, blank=True, max_length=11)
    email = models.EmailField('邮件', null=True, blank=True, max_length=100)

    # 利用内部Meta类来进行元数据配置项的设置
    class Meta:
        verbose_name = "用户"  # 对象名（单数）
        verbose_name_plural = verbose_name  # 对象名（复数）

    def __str__(self):
        return self.username
