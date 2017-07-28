#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import *

from cmdb.models import Host, Idc, HostGroup, NetworkDevices

class AssetForm(forms.ModelForm):

    class Meta:
        model = Host
        exclude = ("id",)
        widgets = {
            'hostname': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'必填项'}),
            'group': Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'cpu_model': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'cpu_count': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'cpu_core_count': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'memory': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'sn': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'asset_type': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'status': Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'os': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'ip': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'必填项'}),
            'disk': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'idc': Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'vendor': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'memo': Textarea(attrs={'class': 'form-control', 'style': 'width:530px;'}),
        }

class IdcForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(IdcForm, self).clean()
        value = cleaned_data.get('name')
        try:
            Idc.objects.get(name=value)
            self._errors['name'] = self.error_class(["%s的信息已经存在" % value])
        except Idc.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = Idc
        exclude = ("id",)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control','style': 'width:450px;'}),
            'address': TextInput(attrs={'class': 'form-control','style': 'width:450px;'}),
            'tel': TextInput(attrs={'class': 'form-control','style': 'width:450px;'}),
            'contact': TextInput(attrs={'class': 'form-control','style': 'width:450px;'}),
            'contact_phone': TextInput(attrs={'class': 'form-control','style': 'width:450px;'}),
            'cabinet': TextInput(attrs={'class': 'form-control','style': 'width:450px;'}),
            'ip_range': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
            'bandwidth': TextInput(attrs={'class': 'form-control','style': 'width:450px;'}),
        }

class GroupForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(GroupForm, self).clean()
        value = cleaned_data.get('name')
        try:
            HostGroup.objects.get(name=value)
            self._errors['name'] = self.error_class(["%s的信息已经存在" % value])
        except HostGroup.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = HostGroup
        exclude = ("id", )

class NetworkDevicesForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(NetworkDevicesForm, self).clean()
        value = cleaned_data.get('name')
        try:
            NetworkDevices.objects.get(name=value)
            self._errors['name'] = self.error_class(["%s的信息已经存在" % value])
        except NetworkDevices.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = NetworkDevices
        exclude = ()

        # 控制表单样式
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'style': 'width:200px;'}),
            'ip': TextInput(attrs={'class': 'form-control', 'style': 'width:200px;'}),
            'group': Select(attrs={'class': 'form-control', 'style': 'width:200px;'}),
            'desc': Textarea(attrs={'class': 'form-control', 'style': 'width:200px;'}),
        }