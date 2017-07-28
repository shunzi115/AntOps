# coding: utf-8

import re
from  django import template
register = template.Library()

@register.filter(name='int2str')
def int2str(value):
    """
    int 转换为 str
    """
    return str(value)

@register.filter(name='res_splict')
def res_split(value):
    """
    将结果格式化换行
    """
    res = []
    if isinstance(value, tuple):
        for v in value:
            if v is not None:
                data = v.replace('\n', '<br>')
                res.append(data)
        return res
    else:
        return value

@register.filter()
def manager_ip(value):
    '''
    格式化处理网卡IP
    这里是公司用的，需要根据个人公司进行修改
    :param value: 前端传递过来的 网卡地址信息
    :return:
    '''
    if len(value) < 10:
        '''为什么是<10呢？ 举个例子 len('em1:1.1.1.1') = 11；所以就用10'''
        return None
    else:
        for_m_ip = ['eth1', 'em2', 'p2p1']
        ip_list = re.findall('(e[a-z]+\d+:\d+.\d+.\d+.\d+)', value.strip())
        # ['eth1:10.1.2.57', 'eth0:10.10.100.103']
        for host in ip_list:
            host_ip = host.strip().split(':')
            for m_ip in for_m_ip:
                if m_ip ==  host_ip[0]:
                    ip_list = host_ip[1]
        return  ip_list

@register.filter()
def other_ip(value):
    '''
    格式化处理网卡IP
    这里是公司用的，需要根据个人公司进行修改
    '''
    if len(value) < 10:
        '''为什么是<10呢？ 举个例子 len('em1:1.1.1.1') = 11；所以就用10'''
        return None
    else:
        for_o_ip = ['eth0', 'em1',]
        ip_list = re.findall('e[a-z]+\d:\d+.\d+.\d+.\d+\.\d+', value.strip())
        # ['eth1:10.1.2.57', 'eth0:10.10.100.103']
        # ['em1:0:122.13.74.66', 'em1:119.147.212.248', 'em2:192.168.1.169']
        more_ip = []
        for host in ip_list:
            host_ip = host.strip().split(':')
            for o_ip in for_o_ip:
                if o_ip == host_ip[0]:
                    if len(host_ip) == 3:
                        more_ip.append(host_ip[2])
                    else:
                        more_ip.append(host_ip[1])

        if len(more_ip) < 1:
            pass
        elif len(more_ip) == 1:
            return more_ip[0]
        else:
            return "{0} {1}".format(more_ip[0], more_ip[1])