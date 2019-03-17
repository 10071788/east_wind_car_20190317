#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
import xadmin
from .models import RentalCarInfo

class RentalCarInfoAdmin(object):
    list_display = ["carid", "srcaddr", "dstaddr"]
    search_fields = ["carid", "srcaddr", "dstaddr"]
    list_editable = ["carid", "srcaddr", "dstaddr"]
    list_filter = ["carid", "srcaddr", "dstaddr"]
    style_fields = {"carid": "ueditor"}

xadmin.site.register(RentalCarInfo, RentalCarInfoAdmin)