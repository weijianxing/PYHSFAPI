# -*- coding: UTF-8 -*-
__author__ = 'jianxing.wei@wuage.com '
"""
    HSF 正常交互是通过注册中心获取接口服务地址，可行性有待验证
    单可以通过otps http接口获取
"""
class ServerConf:
    SERVICEIP="172.17.4.46"
    #HSF console 开发的qos端口
    SERVICEPORT="29491"
    TIMEOUT=60
    INTERFACE="com.wuage.search.share.service.SellerQueryService"
    VERSION="1.0.0"
    #多个接口方法直接添加到集合中
    METHOD={"searchSeller"}
    def __init__(self):
        pass
#todo 通过register获取 服务ip：port