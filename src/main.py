#coding=utf-8
from common.config.Config import Config
from common.email.EmailTool import EmailTool
from server.SummaryServiceImpl import SummaryServiceImpl
from server.WishListServiceImpl import WishListServiceImpl

__author__ = 'chenjinlong'
from dal.util.conn.MySqlConn import MySqlConn
from biz.util.SShTunnel import SSHTunnel
from server.OfferListServiceImpl import OfferListServiceImpl
from common.excel.ExcelTool import ExcelTool
#初始化配置参数
Config.initConf()

@SSHTunnel.sshWrapper
@MySqlConn.dbWrapper
def main():
    excelTool = ExcelTool("报表")
    #订单报表
    offerListServiceImpl = OfferListServiceImpl()
    offerListServiceImpl.getReport(excelTool)
    #订单详情报表
    offerListServiceImpl.getDetailReport(excelTool)
    #需求单报表
    wishListServiceImpl = WishListServiceImpl()
    wishListServiceImpl.getReport(excelTool)
    #需求单明细报表
    wishListServiceImpl.getDetailReport(excelTool)
    #汇总明细报表
    summaryServiceImpl = SummaryServiceImpl()
    summaryServiceImpl.getDetailReport(excelTool)
    #发送邮件
    excelFileName = excelTool.fileName

    EmailTool.sendMail(excelFileName)

main()

