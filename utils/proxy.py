#!/usr/bin/env python
# -*- coding:utf-8 -*-
proxyHost = "http-proxy-t3.dobel.cn"
proxyPort = "9180"
proxyUser = "LIEXINHTT1"
proxyPass = "oK97IIl298"
proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host" : proxyHost,
        "port" : proxyPort,
        "user" : proxyUser,
        "pass" : proxyPass,
}
proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
}