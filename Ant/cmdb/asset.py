#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import json

from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cmdb.plugins import core
from cmdb import models
from cmdb.forms import AssetForm
from cmdb.api import pages, str2gb, get_object
from django.contrib.auth.decorators import login_required

@login_required()
def asset(request):
    temp_name = "cmdb/cmdb-header.html"

    idc_info = models.Idc.objects.all()
    host_list = models.Host.objects.all()

    assets_list, p, assets, page_range, current_page, show_first, show_end = pages(host_list, request)

    return render(request, 'cmdb/asset.html', locals())

# 配置 csrf 验证
@csrf_exempt
def asset_report(request):
    '''
    接收客户端资产上报数据，中间使用模块处理后直接保存到数据库
    :param request:
    :return:
    '''
    print(request.GET)
    if request.method == "POST":
        # print(request.POST.get("asset_data"))
        ass_handler = core.Asset(request)
        if ass_handler.data_is_valid():
            print("----asset data valid:")
            ass_handler.save_new_asset_to_approval_zone()

        return HttpResponse(json.dumps(ass_handler.response))


    return HttpResponse('--test--')

@login_required()
def asset_add(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == "POST":
        a_form = AssetForm(request.POST)
        if a_form.is_valid():
            a_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return render(request, "cmdb/asset_add.html", locals())
    else:
        display_control = "none"
        a_form = AssetForm()
        return render(request, "cmdb/asset_add.html", locals())

@login_required()
def asset_del(request):
    asset_id = request.GET.get('id', '')
    if asset_id:
        models.Host.objects.filter(id=asset_id).delete()

    if request.method == 'POST':
        asset_batch = request.GET.get('arg', '')
        asset_id_all = str(request.POST.get('asset_id_all', ''))

        if asset_batch:
            for asset_id in asset_id_all.split(','):
                asset_item = get_object(models.Host, id=asset_id)
                asset_item.delete()

    return HttpResponse(u'删除成功')

@login_required()
def asset_edit(request, ids):
    status = 0
    # asset_types = ASSET_TYPE
    obj = get_object(models.Host, id=ids)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            status = 1
        else:
            status = 2
    else:
        af = AssetForm(instance=obj)

    return render(request, 'cmdb/asset_edit.html', locals())
