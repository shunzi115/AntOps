#!/usr/bin/env python
# -*- coding:utf-8 -*-

from plugins.linux import sysinfo

def LinuxSysInfo():
    return sysinfo.collect()
