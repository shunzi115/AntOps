#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json
from django.core.exceptions import ObjectDoesNotExist
from cmdb import models
from django.utils import timezone


class Asset(object):
    def __init__(self,request):
        self.request = request
        self.response = {
            'error':[],
            'info':[],
            'warning':[]
        }

    def response_msg(self,msg_type,key,msg):
        if msg_type in self.response:
            self.response[msg_type].append({key:msg})
        else:
            raise ValueError

    def deal_ip(self, ip_list):
        if ip_list:
            # 'nic': [('em1:0', '122.13.74.66'), ('em1', '119.147.212.248'), ('em2', '192.168.1.169')],
            ip_str = ""
            for ip_data in ip_list:
                if ip_data == ip_list[-1]:
                    ip_str = ip_str + "%s:%s" % (ip_data[0], ip_data[1])
                else:
                    ip_str = ip_str + "%s:%s\n" % (ip_data[0], ip_data[1])
            return ip_str

    def deal_disk(self, disk_list):
        if disk_list:
            # 'physical_disk_driver': [{'sda': '500GB'}, {'sdb': '500GB'}],
            disk_str = ""
            for disk_data in disk_list:
                if disk_data == disk_list[-1]:
                    for k, v in disk_data.items():
                        disk_str = disk_str + "%s:%s" % (k, v)
                else:
                    for k, v in disk_data.items():
                        disk_str = disk_str + "%s:%s\n" % (k, v)
            return disk_str

    def deal_data(self, data):
        if data:
            deal_data = {}
            deal_data["hostname"] = data["hostname"]
            deal_data["ip"] = self.deal_ip(data["nic"])

            deal_data["cpu_model"] = data["cpu_model"]
            deal_data["cpu_count"] = data["cpu_count"]
            deal_data["cpu_core_count"] = data["cpu_core_count"]
            deal_data["memory"] = str(data["ram_size"])

            deal_data["disk"] = self.deal_disk(data["physical_disk_driver"])

            deal_data["sn"] = data["sn"]
            deal_data["asset_type"] = data["asset_type"]
            deal_data["os"] = data["os_distribution"]
            deal_data["vendor"] = data["manufactory"]
        return deal_data

    def data_is_valid(self):
        '''
        接收 客户端传递过来的数据 标记为 clean_data数据
        :return:
        '''
        data = self.request.POST.get("asset_data")
        if data:
            try:
                data = json.loads(data)
                data = self.deal_data(data)
                self.clean_data = data
                return True
            except ValueError as e:
                self.response_msg('error','AssetDataInvalid', str(e))
        else:
            self.response_msg('error','AssetDataInvalid', "The reported asset data is not valid or provided")

    def create_data(self):
        last_data = { 'hostname': self.clean_data["hostname"],
                      'cpu_model': self.clean_data["cpu_model"],
                      'cpu_count': self.clean_data["cpu_count"],
                      'cpu_core_count': self.clean_data["cpu_core_count"],
                      'memory': self.clean_data["memory"],
                      'sn': self.clean_data["sn"],
                      'asset_type': self.clean_data["asset_type"],
                      'os': self.clean_data["os"],
                      'ip': self.clean_data["ip"],
                      'disk': self.clean_data["disk"],
                      'vendor': self.clean_data["vendor"],
        }
        return last_data

    def save_new_asset_to_approval_zone(self):
        last_data = self.create_data()
        models.Host.objects.create(**last_data)
