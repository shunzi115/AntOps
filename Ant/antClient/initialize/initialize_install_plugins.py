#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 获取 操作系统 类型 并安装
import re, os, sys

from initialize import settings

class initailze(object):
    def __init__(self, os_file):
        self.os_file = os_file

    def resolve_os_type(self):
        text = ''
        if os.path.exists(self.os_file):
            with open(self.os_file, 'r') as osf:
                for line in osf:
                    text = line.strip()
        return text

    def os_type(self):
        text = self.resolve_os_type()
        if text:
            result = re.search(r'(centos)|(Red Hat)|(Ubuntu)', text).group()
        return result

    def execu_initialize(self):
        result = self.os_type()
        if result:
            if result == "centos" or result == "Red Hat":
                command_ex = settings.confi["centos_com"]
                os.system(command_ex)
            else:
                command_ex = settings.confi["ubuntu_com"]
                os.system(command_ex)

def runCom():
    os_file = settings.confi["os_file"]
    obj = initailze(os_file)
    obj.execu_initialize()