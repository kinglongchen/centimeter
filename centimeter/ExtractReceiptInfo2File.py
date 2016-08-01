from common.config.Config import Config
from common.file.Receipt4FileInput import Receipt4FileInput
from common.util.SShTunnel import SSHTunnel
Config.initConf()

from server.helper.Finance4ReceiptHelper import Finance4ReceiptHelper


from dal.mapper.OrderReceiptMapper import OrderReceiptMapper
from dal.util.conn.MySqlConn import MySqlConn

__author__ = 'chenjinlong'


@MySqlConn.dbWrapper
@SSHTunnel.sshWrapper
def extractRemainingAmountNotZearo():
    orderReceiptMapper = OrderReceiptMapper()
    receipt4FileInput = Receipt4FileInput()
    finance4ReceiptHelper = Finance4ReceiptHelper()


    orderReceiptDOList = orderReceiptMapper.selectRemainingAmountNotZearo()

    outOrderSnList = []

    for receiptDO in orderReceiptDOList:
        outOrderSnList.append(receiptDO.outOrderSn)


    orderInfoDict,saleReturnExchangeBillDict,returnGoodsBillDict = finance4ReceiptHelper.getRetrunOrderInfo(outOrderSnList)

    saveList = __getTreeZearoOrderList(orderInfoDict,orderReceiptDOList,saleReturnExchangeBillDict,returnGoodsBillDict)




    receipt4FileInput.writeList(saveList)

    receipt4FileInput.flush()

def __getTreeZearoOrderList(orderInfoDict,orderReceiptDOList,saleReturnExchangeBillDict,returnGoodsBillDict):
    saveList = []
    for orderReceiptDO in orderReceiptDOList:
        orderInfoDO = orderInfoDict.get(orderReceiptDO.outOrderSn,None)
        if orderInfoDO.tradeStatus=="XTDD":
            if orderInfoDO.returnAmount is None or orderInfoDO.returnAmount==0:
                saleReturnExchangeBillList = saleReturnExchangeBillDict.get(orderInfoDO.orderSn,None)
                returnGoodsBillList = returnGoodsBillDict.get(orderInfoDO.orderSn,None)

                if saleReturnExchangeBillList is None and returnGoodsBillList is None:
                    saveList.append(orderReceiptDO)

    return saveList


extractRemainingAmountNotZearo()
