# _*_ coding: utf-8 _*_
# @Time     : 17:58
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import UserFav


class UserFavAdmin(object):
    list_display = ['user', 'goods', "add_time"]


xadmin.site.register(UserFav, UserFavAdmin)
