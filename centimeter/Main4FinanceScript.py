# coding=utf-8
#初始化配置参数
import time
from common.config.Config import Config

Config.initConf()
from facade.impl.OrderReceiptFacadeImpl import OrderReceiptFacadeImpl

from dal.domain.do.OrderInfoDO import OrderInfoDO
from dal.util.conn.MySqlConn import MySqlConn
from server.Finance4ReceiptService import Finance4ReceiptService

__author__ = 'chenjinlong'



# @MySqlConn.dbWrapper
# def main():
#     fileInput = open("../output/receipt/retryfile.txt","w")
#     try:
#
#         # service = Finance4ReceiptService(fileInput)
#         #
#         # payOrderList = service.selectBatch(0)
#         orderReceiptFacade = OrderReceiptFacadeImpl()
#         orderReceiptFacade.doBatchUpdateById()
#     except Exception,e:
#         print e
#     finally:
#         fileInput.close()


    # print len(payOrderList)

@MySqlConn.dbWrapper
def doOrderReceiptBiz():
    start = time.time()
    finance4ReceiptService = Finance4ReceiptService()
    finance4ReceiptService.doFinanceReceiptDataInit()
    end = time.time()
    print "用时:%ds" %(end-start)

doOrderReceiptBiz()
# main()