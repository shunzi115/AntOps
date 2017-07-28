#!/usr/bin/env python
# -*- coding:utf-8 -*-
## filename: conf.settings.py

import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Params = {
    "server": "10.1.2.102",
    "port":8080,
    'request_timeout':30,
    "urls":{
          "asset_report":"/cmdb/report/",
        },
    'log_file': '%s/logs/run_log' % BaseDir,
}