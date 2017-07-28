#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def service_line(request):
    '''
    用来管理主机属于哪个业务线的
    :param request:
    :return:
    '''
    return HttpResponse("service_line...")