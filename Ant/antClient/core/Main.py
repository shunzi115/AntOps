#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# 客户端使用服务器默认的python版本 2.6 2.7

import os, json, sys, datetime
import urllib,urllib2,sys,os,json,datetime
from core import info_collection
from conf import settings

class ArgvHandler(object):
    def __init__(self, argvs):
        self.argvs = argvs
        self.parse_argv()

    def parse_argv(self):
        '''
        Parsing external arguments
        :return:
        '''
        if len(self.argvs) > 1:
            if hasattr(self, self.argvs[1]):
                func = getattr(self, self.argvs[1])
                func()
            else:
                self.help_msg()
        else:
            self.help_msg()

    def help_msg(self):
        msg = '''
        collect_asset
        report_asset
        '''
        print(msg)

    def collect_asset(self):
        obj = info_collection.InfoCollection()
        # 执行 收集模块的 收集函数取得所有 收集信息
        asset_data = obj.collect()
        print(asset_data)

    def __submit_data(self, url, data, method):
        if url in settings.Params['urls']:
            if type(settings.Params['port']) is int:
                url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['urls'][url])
            else:
                pass
            print('Connecting... \n  \033[32;2m[%s] \033[0m, it may take a minute...' % url)

            if method == "post":
                try:
                    data_encode = urllib.urlencode(data)
                    req = urllib2.Request(url=url,data=data_encode)
                    res_data = urllib2.urlopen(req,timeout=settings.Params['request_timeout'])
                    callback = res_data.read()
                    callback = json.loads(callback)
                    print("\033[31;1m[%s]:[%s]\033[0m response:\n%s" %(method,url,callback))
                    return callback
                except Exception as e:
                    sys.exit("\033[31;1m%s\033[0m"%e)
            else:
                raise KeyError

    def report_asset(self):
        obj = info_collection.InfoCollection()
        # 获取收集的信息
        asset_data = obj.collect()
        # 取到post  url
        post_url = "asset_report"
        data = {"asset_data": json.dumps(asset_data)}
        response = self.__submit_data(post_url, data, method="post")

        self.log_record(response)

    def log_record(self,log,action_type=None):
        f = open(settings.Params["log_file"],"a")
        if log is str:
            pass
        if type(log) is dict:
            if "info" in log:
                for msg in log["info"]:
                    log_format = "%s\tINFO\t%s\n" %(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),msg)
                    f.write(log_format)
            if "error" in log:
                for msg in log["error"]:
                    log_format = "%s\tERROR\t%s\n" %(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),msg)
                    f.write(log_format)
            if "warning" in log:
                for msg in log["warning"]:
                    log_format = "%s\tWARNING\t%s\n" %(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),msg)
                    f.write(log_format)
        f.close()
