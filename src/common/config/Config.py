# coding=utf-8
import codecs

__author__ = 'chenjinlong'
from datetime import datetime, timedelta, time
from common.util import PathUtil
import os
import json


class Config(object):
    emailTextFilePath = os.sep.join([PathUtil.getResourcePath(), "emailText.txt"])
    toAddrMap = {}
    emailPassword = ""
    fromAddrMap = {}

    smtpServer = ""

    excludeFilterList = []

    statusDict = {'BYQX': '订单取消',
                  'BDFK': '待付款',
                  'BYFK': '已付款',
                  'BBFFH': '部分发货',
                  'BYFH': '已发货',
                  'BYQS': '已签收',
                  'BYJS': '已结算',
                  'XYQX': "需求单取消",
                  "XQRBJ": "确认报价单",
                  "XDBJ": "'待报价",
                  "XYBJ": "已报价"}

    # 报价单中是订单的条件
    isOrderFilter = ['BDFK', 'BYFK', 'BBFFH', 'BYFH', 'BYQS', 'BYJS']

    # 需求单过滤
    wishListFilter = ['XDBJ', 'XYBJ', 'XYQX', 'XQRBJ', 'BYQX']

    timeDelta = 1

    originalDate = {"year": 2015, "month": 7, "day": 7}

    excelFilePath = ""

    # 数据库相关配置
    dbHost = ""
    dbUser = ""
    dbPasswd = ""
    dbName = ""
    dbPort = ""

    # ssh相关配置
    sshUserName = "",
    sshPassword = ""
    sshHost = ""
    sshPort = None
    localBindAddress = ""
    localBindPort = None
    remoteBindAddress = ""
    remoteBindPort = None

    @classmethod
    def initConf(cls):
        configFilePath = os.sep.join([PathUtil.getConfigPath(), "centimeter.json"])
        confJson = None
        with codecs.open(configFilePath, "r", "utf-8") as f:

            confJson = json.load(f, encoding="utf-8")
        # email相关参数的配置
        emailJson = confJson["email"]

        for k, v in emailJson.iteritems():
            setattr(cls, k, v)

        # 报表相关设置
        reportJson = confJson["report"]
        for k, v in reportJson.iteritems():
            setattr(cls, k, v)

        # excel相关设置
        excelJson = confJson["excel"]
        for k, v in excelJson.iteritems():
            setattr(cls, k, v)

        # ssh相关配置
        sshJson = confJson["ssh"]
        for k, v in sshJson.iteritems():
            setattr(cls, k, v)

        # 数据库相关设置
        dbJson = confJson["db"]
        for k, v in dbJson.iteritems():
            setattr(cls, k, v)

    @classmethod
    def getDateSpan(cls):
        dt = datetime.now()
        dateFrom = datetime.combine(dt.date() - timedelta(cls.timeDelta), time.min)
        dateTo = datetime.combine(dt.date(), time.min)
        return dateFrom, dateTo

    @classmethod
    def getHistoryDateSpan(cls):
        dt = datetime.now()
        dateFrom = datetime(cls.originalDate["year"], cls.originalDate["month"], cls.originalDate["day"])
        dateTo = datetime.combine(dt.date(), time.min)
        return dateFrom, dateTo


if __name__ == "__main__":
    # Config.initConf()
    # print Config.excelFilePath
    a = '{"a":"陈"}'
    dict = json.loads(a)
    print dict["a"]
    print "end"
