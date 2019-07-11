#!/usr/bin/env python
# -*- coding:utf-8 -*-

import inspect


def code2msg(code):  # 外部展示
    if code in StatusCode.StatusDict:
        return {"reactCode": code, "message": StatusCode.StatusDict[code][0]}
    else:
        return {"reactCode": "100000", "message": StatusCode.StatusDict["100000"][0]}


class StatusCode:
    Succeed = "000000"
    NotFound = "000010"
    Unknown = "100000"
    ParamError = "100001"
    MissingParam = "100002"
    ProxyInvalid = "100003"
    AccountQuotaLimit = "100004"
    NotImplementedError = "100005"
    TokenOverdue = "100006"
    ProxyTmr = '100007'
    ProxyError = '100008'
    ReqTmr = '100009'
    Timeout = "100010"
    IPBlock = "100020"
    IPLimit = "100021"
    AuthCode = "100030"
    TempUnavailable = "100040"
    ProxyRequest = '100050'

    StatusDict = {
        "000000": ("succeed", "正常"),
        "100000": ("unknown", "未知错误"),
        "000010": ("search no result", "未找到数据"),
        "100001": ("param error", "输入参数错误"),
        "100002": ("missing param", "缺少输入的参数"),
        "100003": ("current proxy invalid", "代理失效"),
        "100004": ("account quota limit", "调用额度达到上限"),
        "100005": ("http method not implemented", "未定义该方法"),
        "100006": ("token overdue", "token过期"),
        "100007": ("too many requests to proxy", "代理请求过快"),
        "100008": ("proxy error", "代理出错"),
        "100009": ("429 Too Many Requests", "请求过快"),
        "100010": ("request time out", "请求超时"),
        "100020": ("IP block", "IP被禁止访问"),
        "100021": ("IP limit", "IP访问限制 数据异常"),
        "100030": ("verify code", "出现验证码"),
        "100040": ("request temporarily unavailable", "暂时无数据返回"),
    }


class BaseStatusError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        class_name = kwargs["class_name"] if "class_name" in kwargs else self.__class__.__name__
        self.value = kwargs["value"] if "value" in kwargs else getattr(StatusCode, class_name)
        if "msg" in kwargs:
            self.msg = kwargs["msg"]
        elif args:
            self.msg = args[0]
        else:
            self.msg = StatusCode.StatusDict[self.value][0]

        error_logging = False if "off_error_logging" in kwargs else True
        self.error_logging = bool(kwargs["error_logging"]) if "error_logging" in kwargs else error_logging
        self.frames = inspect.getouterframes(inspect.currentframe())[1] if self.error_logging else None

    def __str__(self):
        return str(self.msg)


class Status:
    # def __init__(self):
    #     super(Status, self).__init__()

    class Succeed(BaseStatusError):
        class NotFound(BaseStatusError):
            def __init__(self, *args, **kwargs):
                super().__init__(off_error_logging=True, *args, **kwargs)

        def __init__(self, *args, **kwargs):
            super().__init__(off_error_logging=True, *args, **kwargs)
            self.result = args[0]

    class MissingParam(BaseStatusError):
        def __init__(self, *args, **kwargs):
            super().__init__(off_error_logging=True, *args, **kwargs)

    class ParamError(BaseStatusError):
        def __init__(self, *args, **kwargs):
            super().__init__(off_error_logging=True, *args, **kwargs)

    class Timeout(BaseStatusError):
        pass

    class IPBlock(BaseStatusError):
        pass

    class IPLimit(BaseStatusError):
        pass

    class AuthCode(BaseStatusError):
        pass

    class TempUnavailable(BaseStatusError):
        pass

    class Unknown(BaseStatusError):
        pass

    class TokenOverdue(BaseStatusError):
        pass

    class ProxyInvalid(BaseStatusError):
        pass

    class NotImplementedError(BaseStatusError):
        pass

    class AccountQuotaLimit(BaseStatusError):
        pass

    class ProxyTmr(BaseStatusError):
        pass

    class ProxyError(BaseStatusError):
        pass

    class ReqTmr(BaseStatusError):
        pass

    # Exception in StatusErrTup will be caught by try_helper(in common.func), try_helper will return Empty result
    # to http client and log the error message
    StatusErrTup = (Succeed.NotFound, Timeout, IPBlock, IPLimit, AuthCode, TempUnavailable, Unknown,
                    ParamError, TokenOverdue, ProxyInvalid, AccountQuotaLimit, MissingParam, ProxyTmr, ProxyError,
                    ReqTmr)
