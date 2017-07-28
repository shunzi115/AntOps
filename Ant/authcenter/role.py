#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authcenter.forms import RoleListForm
from authcenter.models import RoleList
from authcenter.permission import permission_verify


def role_add(request):
    temp_name = "accounts/accounts-header.html"
    if request.method == "POST":
        form = RoleListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('role_list'))
    else:
        form = RoleListForm()

    kwvars = {
        'temp_name': temp_name,
        'form': form,
        'request': request,
    }

    return render(request, 'accounts/role_add.html', kwvars)


def role_list(request):
    temp_name = "accounts/accounts-header.html"
    all_role = RoleList.objects.all()
    return render(request, 'accounts/role_list.html', locals())

def role_edit(request, ids):
    iRole = RoleList.objects.get(id=ids)
    temp_name = "accounts/accounts-header.html"
    if request.method == "POST":
        form = RoleListForm(request.POST,instance=iRole)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('role_list'))
    else:
        form = RoleListForm(instance=iRole)

    kwvars = {
        'temp_name': temp_name,
        'ids': ids,
        'form': form,
        'request': request,
    }

    return render(request, 'accounts/role_edit.html', kwvars)


def role_del(request, ids):
    RoleList.objects.filter(id=ids).delete()
    return HttpResponseRedirect(reverse('role_list'))

