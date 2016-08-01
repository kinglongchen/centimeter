# coding=utf-8
from decimal import Decimal
from common.config.Config import Config
from common.util.SShTunnel import SSHTunnel
from dal.mapper.PayOrderItemMapper import PayOrderItemMapper
Config.initConf()
from dal.mapper.PayOrderMapper import PayOrderMapper
from dal.util.conn.MySqlConn import MySqlConn
from facade.impl.PayOrderFacadeImpl import PayOrderFacadeImpl
from server.helper.ReceiptTool4Gift import ReceiptTool4Gift

__author__ = 'chenjinlong'

@MySqlConn.dbWrapper
@SSHTunnel.sshWrapper
def doProcess():
    receiptTool4Gift = ReceiptTool4Gift()
    giftMapInfo = receiptTool4Gift.getGiftInfoMap()

    payOrderMapper = PayOrderMapper()

    payOrderItemMapper = PayOrderItemMapper()
    outOrderSnList = []
    payOrderFacade = PayOrderFacadeImpl()

    for key in giftMapInfo:
        outOrderSnList.append(key)

    payOrderDOList = payOrderMapper.selectPayOrderInfo(outOrderSnList)

    payOrderIdList = []

    updatePayOrderInfoOutOrderSnKey = {}

    updatePayOrderInfoPayOrderIdKey = {}

    for payOrderDO in payOrderDOList:
        payOrderIdList.append(payOrderDO.id)

        giftAmount = Decimal(giftMapInfo.get(payOrderDO.outOrderSn,0))



        orderAmount = payOrderDO.payOrderAmount

        updateOrderAmount = orderAmount-giftAmount

        updatePayOrderInfoOutOrderSnKey[payOrderDO.outOrderSn] = updateOrderAmount

        updatePayOrderInfoPayOrderIdKey[payOrderDO.id] = updateOrderAmount


    payOrderItemDOList = payOrderItemMapper.selectByPayOrderIdList(payOrderIdList)

    updatePayOrderItemInfo = {}

    for payOrderItemDO in payOrderItemDOList:
        updateOrderAmount = updatePayOrderInfoPayOrderIdKey.get(payOrderItemDO.payOrderId,payOrderItemDO.itemAmount)
        updatePayOrderItemInfo[payOrderItemDO.payOrderId] = updateOrderAmount

    print("debug info")
    # payOrderFacade.updateAmount(updatePayOrderInfoPayOrderIdKey,updatePayOrderItemInfo)


@MySqlConn.dbWrapper
@SSHTunnel.sshWrapper
def getErrorPayOrder4GiftAmount():
    receiptTool4Gift = ReceiptTool4Gift()
    giftMapInfo = receiptTool4Gift.getGiftInfoMap()

    orderSnList = [key for key in giftMapInfo]

    payOrderMapper = PayOrderMapper()

    payOrderItemMapper = PayOrderItemMapper()



    payOrderDOList = payOrderMapper.selectPayOrderInfo(orderSnList)

    errorOutOrderSn = ""
    errorCount = 0
    for payOrderDO in payOrderDOList:
        giftAmunt = giftMapInfo.get(payOrderDO.outOrderSn,0)
        checkGiftAmount = float(payOrderDO.payOrderAmount-payOrderDO.paidAmount)
        if giftAmunt!=checkGiftAmount:
            errorCount += 1
            errorOutOrderSn+='"%s",' %payOrderDO.outOrderSn
    print "错误的支付订单数量:%s" %errorCount
    print errorOutOrderSn[0:-1]

if __name__ == "__main__":
    getErrorPayOrder4GiftAmount()









