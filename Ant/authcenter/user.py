#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from authcenter.forms import LoginUserForm, EditUserForm, ChangePasswordForm

from django.contrib.auth import get_user_model
from authcenter.forms import AddUserForm
from django.core.urlresolvers import reverse

def acclogin(request):
    if request.method == "POST":
        # 基本认证
        # user = authenticate(username=request.POST.get('email'),
        #                     password=request.POST.get('password'))
        # if user is not None:
        #     login(request, user)
        #     return HttpResponse("LOGIN")

        # 使用form 认证
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            if form.get_user() is not None:
                login(request, form.get_user())
                return redirect('/')
            else:
                pass
    else:
        # 使用 Form 来简单认证
        form = LoginUserForm(request)
    kwargs = {
        'request': request,
        'form':  form,
    }
    return render(request, 'accounts/login.html', kwargs)

def acclogout(request):
    logout(request)
    return redirect('/')

@login_required
def user_list(request):
    temp_name = "accounts/accounts-header.html"
    all_user = get_user_model().objects.all()
    kwargs = {
        'temp_name': temp_name,
        'all_user':  all_user,
    }
    return render(request, 'accounts/user_list.html', kwargs)

@login_required
def user_add(request):
    temp_name = "accounts/accounts-header.html"
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            form.save()
            return HttpResponseRedirect(reverse('user_list'))
    else:
        form = AddUserForm()
    kwargs = {
        'form': form,
        'request': request,
        'temp_name': temp_name,
    }
    return render(request, 'accounts/user_add.html', kwargs)

@login_required
def user_del(request, ids):
    if ids:
        get_user_model().objects.filter(id=ids).delete()
    return HttpResponseRedirect(reverse('user_list'))

@login_required
def user_edit(request, ids):
    user = get_user_model().objects.get(id=ids)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            status = 1
        else:
            status = 2
    else:
        form = EditUserForm(instance=user)
    return render(request, 'accounts/user_edit.html', locals())

@login_required
def reset_password(request, ids):
    user = get_user_model().objects.get(id=ids)
    newpassword = get_user_model().objects.make_random_password(length=10, allowed_chars='abcdefghjklmnpqrstuvwxyABCDEFGHJKLMNPQRSTUVWXY3456789')
    # print('====>ResetPassword:{}-->{}'.format(user.name, newpassword))
    user.set_password(newpassword)
    user.save()
    kwargs = {
        'object': user,
        'newpassword': newpassword,
        'request': request,
    }
    return render(request, 'accounts/reset_password.html', kwargs)

@login_required
def change_password(request):
    temp_name = "accounts/accounts-header.html"
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logout'))
    else:
        form = ChangePasswordForm(user=request.user)
    kwargs = {
        'form': form,
        'request': request,
        'temp_name': temp_name,
    }
    return render(request, 'accounts/change_password.html', kwargs)