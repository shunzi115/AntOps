#!/usr/bin/env python
# -*- coding:utf-8 -*-
## filename: info_collection.py

import platform, json,sys
from plugins import plugin_api

class InfoCollection(object):
    def __init__(self):
        pass

    def get_platform(self):
        '''
        获取系统平台
        :return: 返回系统平台类型
        '''
        os_platform = platform.system()
        return os_platform

    def collect(self):
        '''
        收集平台数据
        :return:平台数据
        '''
        os_platform = self.get_platform()
        try:
            func = getattr(self,os_platform)
            # info_data 就是收集到的所有的信息
            info_data = func()
            # 使用格式化函数对收集到的数据进行 格式化
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except Exception as E:
            sys.exit("Error: Tanker doens't support os [%s]! " % os_platform)

    def Linux(self):
        sys_info = plugin_api.LinuxSysInfo()
        # 序列化输出收集数据
        # f = open("Linux.json", 'w')
        # f.write(json.dumps(sys_info))
        # f.close()
        return sys_info

    def build_report_data(self, data):
        return data
