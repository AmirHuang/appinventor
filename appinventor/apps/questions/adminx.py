# _*_ coding: utf-8 _*_
# @Time     : 17:57
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm


import xadmin
from .models import Questions


class CasesAdmin(object):
    list_display = ["name", "click_num", "fav_num",
                    "cases_brief", "cases_desc", "add_time"]
    search_fields = ['name', ]
    list_filter = ["name", "click_num", "fav_num",
                   "add_time", "category__name"]
    style_fields = {"cases_desc": "ueditor"}


xadmin.site.register(Questions, CasesAdmin)
