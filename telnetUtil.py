__author__ = 'jianxing.wei@wuage.com '
import logging
import logging.config
import telnetlib
import json
# from hsf_telnet_client import serviceConfig
from .serviceConfig import ServerConf
from .telNetError import ConnectionFail
class HSFTelnet(object):
    logger=None
    host=None
    port=None
    timeout=None
    interface=None
    method=None
    version=None
    timeout=0
    tf=None
    def __init__(self, ip=ServerConf.SERVICEIP, port=ServerConf.SERVICEPORT, timeout=ServerConf.TIMEOUT):
        from os import path
        log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
        logging.config.fileConfig(log_file_path)
        self.logger=logging.getLogger('HSFTelnet')
        self.ip = ip
        self.port=port
        self.timeout=timeout
        try:
            self.logger.info("telnet {0} ： {1} ; timeout={2}".format(ip ,port ,timeout ))
            self.tf=telnetlib.Telnet(ip,port=port , timeout=timeout)

            self.logger.info(self.tf.read_until(b"pandora>"))
        except Exception as ex:
            if hasattr(ex, 'reason'):
                raise ConnectionFail(ex.reason, ue.reason)
            else:
                raise ConnectionFail(ex.reason, None)

    def connection(self, ip=ServerConf.INTERFACE, method=None, version=ServerConf.VERSION):
        """
        同HAF QOS console 建立网络通道
        """
        #todo 判断服务端是否存在实例
    def close(self):
        """
            退出控制台并关闭telnet 通道
        """
        self.tf.write(b"quit\n")
        self.tf.close()
        pass
    def preInvoke(self):
        self.tf.write(b"cd hsf\n")
        self.logger.info("response cd hsf.")
        self.logger.info(self.tf.read_until(b"hsf>"))
        self.tf.write(b"ls \n")
        self.logger.info("response  is command.")
        self.logger.info(self.tf.read_until(b"hsf>"))
    def invoke(self , interface=ServerConf.INTERFACE, method=None, version=ServerConf.VERSION ,singleParm=None, **kwargs):
        """
        调用HSF服务
        eg:invoke com.wuage.search.share.service.SellerQueryService:1.0.0.searchSeller("友发")
        """
        self.interface=interface
        self.method=method
        self.version=version
        jsonP=""
        if(singleParm):
            jsonP=singleParm
        else:
            jsonP=json.dump(kwargs)
        command="invoke {0}:{1}.{2}(\"{3}\")".format(self.interface,self.version,self.method,jsonP)
        self.logger.info("telnet command : {0} ".format(command))
        self.preInvoke()
        self.tf.write(command.encode('utf-8')+b"\n")
        return self.tf.read_until(b"\r\n")