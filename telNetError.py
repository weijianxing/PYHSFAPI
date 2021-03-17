# coding=utf-8
__author__ = 'jianxing.wei@wuage.com '

hsf_telnet_error={}
class HSFTelnetError(RuntimeError):
    code = None
    message = None
    data = None
    def __init__(self, message=None, data=None, code=None):
        RuntimeError.__init__(self)
        self.message = message or self.message
        self.data = data
        self.code = code or self.code
        assert self.code, "没有指定错误code."

    def __str__(self):
        return "HSFTelnetError({code}): {message}".format(
            code=self.code,
            message=str(self.message)
        )

    def __unicode__(self):
        return u"HSFTelnetError({code}): {message}".format(
            code=self.code,
            message=self.message
        )
class MethodNotFound(HSFTelnetError):
    code = -1000
    message = u"没有指定调用方法."

    def __init__(self, message=None, data=None):
        HSFTelnetError.__init__(self, message=message, data=data)


class ConnectionFail(HSFTelnetError):
    code = 1000
    message = u'连接失败 {0}'

    def __init__(self, message=None, data=None):
        message = self.message.format(data)
        HSFTelnetError.__init__(self, message=message, data=data)


class NoProvider(HSFTelnetError):
    code = 2000
    message = u'服务接口不存在 {0}'
    provide_name = u''

    def __init__(self, message=None, data=None):
        self.provide_name = data
        HSFTelnetError.__init__(self, message=self.message.format(data), data=data)


class InvalidParams(HSFTelnetError):
    code = 2001
    message = u"调用参数错误."

    def __init__(self, message=None, data=None):
        HSFTelnetError.__init__(self, message=message, data=data)


class InternalError(HSFTelnetError):
    code = 3000
    message = u"交互异常."

    def __init__(self, message=None, data=None):
        HSFTelnetError.__init__(self, message=message, data=data)


class InvalidRequest(HSFTelnetError):
    code = 3002
    message = u"请求异常."

    def __init__(self, message=None, data=None):
        HSFTelnetError.__init__(self, message=message, data=data)


class UserDefinedError(HSFTelnetError):
    code = 5000
    message = u'自定义异常：'

    def __init__(self, message=None, data=None):
        HSFTelnetError.__init__(self, message=message, data=data)
hsf_telnet_error[MethodNotFound.code] = MethodNotFound
hsf_telnet_error[NoProvider.code] = NoProvider
hsf_telnet_error[ConnectionFail.code] = ConnectionFail
hsf_telnet_error[InvalidParams.code] = InvalidParams
hsf_telnet_error[InternalError.code] = InternalError
hsf_telnet_error[InvalidRequest.code] = InvalidRequest
hsf_telnet_error[UserDefinedError.code] = UserDefinedError