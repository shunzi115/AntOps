#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models
from authcenter.models import UserInfo

ASSET_STATUS = (
    (0, u"使用中"),
    (1, u"未使用"),
    (2, u"故障"),
    (3, u"其它"),
    )

class Idc(models.Model):
    name = models.CharField(u"机房名称", max_length=128, unique=True)
    address = models.CharField(u"机房地址", max_length=128, null=True)
    tel = models.CharField(u"机房电话", max_length=30, null=True)
    contact = models.CharField(u"客户经理", max_length=30, null=True)
    contact_phone = models.CharField(u"移动电话", max_length=30, null=True)
    cabinet = models.CharField(u"机柜信息", max_length=32, null=True)
    ip_range = models.CharField(u"IP范围", max_length=30, null=True)
    bandwidth = models.CharField(u"接入带宽", max_length=30, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'数据中心'
        verbose_name_plural = verbose_name

class HostGroup(models.Model):
    name = models.CharField(u"组名", max_length=64, unique=True)
    desc = models.CharField(u"描述", max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Host(models.Model):
    hostname = models.CharField(max_length=64, verbose_name=u"主机名", unique=True)
    group = models.ForeignKey(HostGroup, verbose_name=u"设备组", on_delete=models.SET_NULL, null=True, blank=True)
    cpu_model = models.CharField(u'CPU型号', max_length=128,blank=True)
    cpu_count = models.CharField(u'物理cpu个数', max_length=10, null=True)
    cpu_core_count = models.CharField(u'cpu核数', max_length=10, null=True)
    memory = models.CharField(u"内存大小",max_length=32, null=True, blank=True)
    sn = models.CharField(u"SN号 码", max_length=128, blank=True)
    asset_type = models.CharField(u"设备类型", max_length=30, null=True, blank=True)
    status = models.IntegerField(u"设备状态", choices=ASSET_STATUS, null=True, blank=True, default=0)
    os = models.CharField(u"操作系统", max_length=100, null=True, blank=True)
    ip = models.CharField(u"IP", max_length=255, unique=True)
    disk = models.CharField(u"硬盘信息", max_length=255, null=True, blank=True)
    idc = models.ForeignKey(Idc, verbose_name=u"所在机房", on_delete=models.SET_NULL, null=True, blank=True)
    vendor = models.CharField(u"设备厂商", max_length=50, null=True, blank=True)
    memo = models.TextField(u"备注信息", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.hostname

class NetworkDevices(models.Model):
    name = models.CharField(u'名称', max_length=64, unique=True)
    ip = models.GenericIPAddressField(u'IP地址', max_length=20, null=True)
    group = models.ForeignKey(HostGroup, verbose_name=u"设备组", on_delete=models.SET_NULL, null=True, blank=True)
    desc = models.CharField(u'描述', max_length=128, null=True)

    def __str__(self):
        return self.name

class IpSource(models.Model):
    net = models.CharField(max_length=30)
    subnet = models.CharField(max_length=30,null=True)
    describe = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.net