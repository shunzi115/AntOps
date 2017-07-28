#!/usr/bin/evn python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from cmdb import  idc, asset, group, service_line, network

urlpatterns = [
    url(r'^asset/$', asset.asset, name='cmdb'),
    url(r'^report/$', asset.asset_report, name='asset_report'),

    url(r'^asset/add/$', asset.asset_add, name='asset_add'),
    url(r'^asset/del/$', asset.asset_del, name='asset_del'),
    url(r'^asset/edit/(?P<ids>\d+)/$', asset.asset_edit, name='asset_edit'),

    url(r'^group/$', group.group, name='group'),
    url(r'^group/del/$', group.group_del, name='group_del'),
    url(r'^group/add/$', group.group_add, name='group_add'),
    url(r'^group/edit/(?P<ids>\d+)/$', group.group_edit, name='group_edit'),
    url(r'^group/save/$', group.group_save, name='group_save'),
    url(r'^idc/$', idc.idc, name='idc'),
    url(r'^idc/add/$', idc.idc_add, name='idc_add'),
    url(r'^idc/del/$', idc.idc_del, name='idc_del'),
    url(r'^idc/save/$', idc.idc_save, name='idc_save'),
    url(r'^idc/edit/(?P<ids>\d+)/$', idc.idc_edit, name='idc_edit'),
    url(r'service_line/$', service_line.service_line, name='service_line'),

    url(r'^network/$', network.network, name='network'),
    url(r'^network/add/$', network.network_add, name='network_add'),
    url(r'^network/del/$', network.network_del, name='network_del'),
    url(r'^network/edit/(?P<ids>\d+)/$', network.network_edit, name='network_edit'),
    url(r'^network/save/$', network.network_save, name='network_save'),


    # url(r'^collect', api.collect, name='update_api'),
    # url(r'^get/host/', api.get_host, name='get_host'),
    # url(r'^get/group/', api.get_group, name='get_group'),
]
