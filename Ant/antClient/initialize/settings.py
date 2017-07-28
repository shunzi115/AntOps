#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)

confi = {
    "os_file": "/proc/version",
    "centos_com": "bash %s/centos_os.sh" % BASE_DIR,
    "ubuntu_com": "bash %s/ubuntu_os.sh" % BASE_DIR,
}