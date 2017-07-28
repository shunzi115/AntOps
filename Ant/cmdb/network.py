#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from cmdb.models import NetworkDevices, HostGroup
from cmdb.forms import GroupForm, IdcForm, NetworkDevicesForm
from django.contrib.auth.decorators import login_required


@login_required
def network(request):
    temp_name = "cmdb/cmdb-header.html"
    allnetd = NetworkDevices.objects.all()
    context = {
        'temp_name': temp_name,
        'allgroup': allnetd
    }
    return render(request, 'cmdb/network.html', locals())

@login_required
def network_add(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == "POST":
        network_form = NetworkDevicesForm(request.POST)
        if network_form.is_valid():
            network_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return redirect('network_add')
    else:
        display_control = "none"
        network_form = NetworkDevicesForm()
        return render(request, "cmdb/network_add.html", locals())

@login_required
def network_del(request):
    if request.method == 'POST':
        group_items = request.POST.getlist('net_check', [])
        if group_items:
            for n in group_items:
                NetworkDevices.objects.filter(id=n).delete()
    return redirect("network")

@login_required
def network_edit(request, ids):
    if request.method == "GET":
        network_ojb = NetworkDevices.objects.filter(id=ids).first()
        network_form = NetworkDevicesForm(instance=network_ojb)
        return render(request, "cmdb/network_edit.html", {"network_form": network_form, "ids":ids})

@login_required
def network_save(request):
    nid = request.POST.get('nid')
    network_obj = NetworkDevices.objects.get(id=nid)
    if request.method == 'POST':
        network_form = NetworkDevicesForm(request.POST, instance=network_obj)
        if network_form.is_valid():
            network_form.save()
        status = 1
    else:
        status = 2
    return render(request, "cmdb/network_edit.html", {"status": status})