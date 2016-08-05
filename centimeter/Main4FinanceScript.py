# coding=utf-8
#初始化配置参数
from datetime import datetime
import time
from common.config.Config import Config
from common.util.SShTunnel import SSHTunnel
from dal.mapper.OrderInfoMapper import OrderInfoMapper
from dal.mapper.OrderReceiptMapper import OrderReceiptMapper

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
@SSHTunnel.sshWrapper
def doOrderReceiptBiz():
    start = time.time()
    finance4ReceiptService = Finance4ReceiptService()
    finance4ReceiptService.doFinanceReceiptDataInit()
    # finance4ReceiptService.doFinanceReceiptData4ErrorOrder()
    end = time.time()
    print "用时:%ds" %(end-start)


@MySqlConn.dbWrapper
@SSHTunnel.sshWrapper
def test():
    start = time.time()
    orderReceiptMapper = OrderReceiptMapper()
    orderReceiptDO = orderReceiptMapper.selectByPrimaryKey(133)

    # print orderReceiptDO.__table__
    orderReceiptDO.id = 1331
    orderReceiptDO.outOrderSn = "B17050109001001"
    print orderReceiptDO.toInsertDict()
    orderReceiptDOList = []
    orderReceiptDOList.append(orderReceiptDO)
    orderReceiptFacade = OrderReceiptFacadeImpl()
    orderReceiptFacade.doOrderReceiptBatchInit2(orderReceiptDOList)

    # finance4ReceiptService.doFinanceReceiptData4ErrorOrder()
    end = time.time()
    print "用时:%ds" %(end-start)

@MySqlConn.dbWrapper
@SSHTunnel.sshWrapper
def doTest():
    orderInfoMapper = OrderInfoMapper()
    orderInfoDO = orderInfoMapper.selectByPrimaryKey(221)
    checkTime = datetime.strptime('2014-01-10 11:01:18',"%Y-%m-%d %H:%M:%S")
    print orderInfoDO.gmtCreate<checkTime

# main()
if __name__ == "__main__":
    doOrderReceiptBiz()
    # doTest()
