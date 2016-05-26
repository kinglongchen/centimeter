# coding=utf-8
from datetime import date, time
from dal.domain.do.OrderReceiptDO import OrderReceiptDO
from dal.domain.do.OrderReceiptRecordDO import OrderReceiptRecordDO
from dal.mapper.OrderInfoMapper import OrderInfoMapper
from dal.mapper.OrderReceiptMapper import OrderReceiptMapper
from dal.mapper.OrderReceiptRecordMapper import OrderReceiptRecordMapper
from dal.mapper.PayOrderItemMapper import PayOrderItemMapper
from dal.mapper.PayOrderMapper import PayOrderMapper
import time as timeSleep
from facade.impl.OrderReceiptFacadeImpl import OrderReceiptFacadeImpl

__author__ = 'chenjinlong'
class Finance4ReceiptService():
    orderInfoMapper = OrderInfoMapper()

    orderReceiptMapper = OrderReceiptMapper()

    orderReceiptRecordMapper = OrderReceiptRecordMapper()

    payOrderMapper = PayOrderMapper()

    payOrderItemMapper = PayOrderItemMapper()

    orderReceiptFacade = OrderReceiptFacadeImpl()


    DO_ONLINE_SUCCESS_TYPE = 'DO_ONLINE_SUCCESS'

    BATCH_NUMBER = 50


    def doScript(self):

        orderInfoDO = self.orderInfoMapper.selectByPrimaryKey(1)

        print  orderInfoDO.companyName

    def doInsert4Record(self):
        record = OrderReceiptRecordDO()
        rs = self.orderReceiptRecordMapper.insertSelective(record)
        return rs

    def doInsert4Receipt(self):
        receipt = OrderReceiptDO()
        rs = self.orderReceiptMapper.insertSelective(receipt)
        return rs

    def selectBatch(self,start):
        return self.payOrderMapper.selectBatch(start,self.BATCH_NUMBER)

    def doFinanceReceiptDataInit(self):
        start = 0
        payOrderDOList = None
        while payOrderDOList == None:
            try:
                payOrderDOList = self.payOrderMapper.selectBatch(start,self.BATCH_NUMBER)
            except Exception,e:
                print e
                print "获取失败，正在尝试。。。"
                timeSleep.sleep(1)
                payOrderDOList = None

        # 批量处理
        while not payOrderDOList:

            outOrderSnList = []
            payOrderIdList = []

            for payOrderDO in payOrderDOList:
                outOrderSnList.append(payOrderDO.outOrderSn)
                payOrderIdList.append(payOrderDO.id)

            try:
                orderInfoDict = self.getOrderInfoDict(outOrderSnList)

                payOrderItemDict = self.getPayOrderItemDict(outOrderSnList)
            except Exception,e:
                print e
                print "获取第%d到%d数据出错,忽略改组,准备尝试下一组。。。"
                continue


            orderReceipt4InsertList = []

            orderReceiptRecord4InsertList = []

            for payOrderDO in payOrderDOList:
                orderInfoDOList = orderInfoDict[payOrderDO.outOrderSn]
                payOrderItemDOList = payOrderItemDict[payOrderDO.outOrderSn]

                if self.check4NotNull(payOrderDO,orderInfoDOList, payOrderItemDOList):
                    continue

                orderReceipt,receiptRecord4ReceivedList = self.doAssemble(payOrderDO,orderInfoDOList, payOrderItemDOList)

                orderReceipt4InsertList.append(orderReceipt)

                orderReceiptRecord4InsertList += receiptRecord4ReceivedList

            # 插入数据
            try:
                self.orderReceiptFacade.doOrderReceiptDataInit(orderReceipt4InsertList,orderReceiptRecord4InsertList)
            except Exception,e:
                print e
                print "获取第%d到%d数据出错,忽略改组,准备尝试下一组。。。"
                continue
            # 查询下一组数据
            start += self.BATCH_NUMBER
            payOrderDOList = self.payOrderMapper.selectBatch(start,self.BATCH_NUMBER)

    def doAssemble(self,payOrder,orderInfoList,payOrderItemList):

        orderReceipt =  OrderReceiptDO()
        # payOrder = PayOrderDO()
        # payOrderItem = PayOrderItemDO()
        orderReceipt.gmtCreate = time.strptime("%Y-%m-%d %H:%M:%S")
        orderReceipt.gmtModified = time.strptime("%Y-%m-%d %H:%M:%S")
        orderReceipt.financeAccountId = payOrder.financeAccountId
        orderReceipt.platformId = payOrder.platformId
        orderReceipt.platformName = payOrder.platformName
        orderReceipt.outOrderSn = payOrder.outOrderSn
        orderReceipt.payId = payOrderItemList[0].payId
        orderReceipt.orderAmount = payOrder.payOrderAmount

        receiptType = self.receiptTypeJuge(payOrder,orderInfoList,payOrderItemList)

        receiptRecord4ReceivedList = []

        if receiptType == self.DO_ONLINE_SUCCESS_TYPE:
            receiptRecord4ReceivedList = self.doOnlineSuccess(orderReceipt,payOrder,orderInfoList,payOrderItemList)

        return orderReceipt,receiptRecord4ReceivedList

    def receiptTypeJuge(self,payOrder,orderInfoList,payOrderItemList):
        return self.DO_ONLINE_SUCCESS_TYPE

    def doOnlineSuccess(self,orderReceipt,payOrder,orderInfoList,payOrderItemList):
        if self.check4Online(payOrder,orderInfoList,payOrderItemList):
            return
        orderInfo = orderInfoList[0]
        payOrderItem = payOrderItemList[0]

        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList.append(self.doOnline4Recevied(orderReceipt,payOrder,orderInfo,payOrderItem))
        receiptRecord4ReceivedList.append(self.doOnline4OutStock(orderReceipt,payOrder,orderInfo,payOrderItem))
        receiptRecord4ReceivedList.append(self.doOnline4PaidConfirm(orderReceipt,payOrder,orderInfo,payOrderItem))

        return receiptRecord4ReceivedList


# 在线预收
    def doOnline4Recevied(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord

    # 在线出库
    def doOnline4OutStock(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord
    # 在线财务确认收款
    def doOnline4PaidConfirm(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord

    # 部分拒收
    def doOnlinePartReject(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord

    # 拒收退款
    def doOnlinePartRefund(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord

    # 退货
    def doReturnGoods(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord

    # 退货退款
    def doReturnGoodsRefund(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord

    # 拆单失效
    def doSplitOrderOriInvalid(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord

    # 拆单新单
    def doSplitOrderChild(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord
    # 取消订单
    def doOnlineCancel(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord
    # 取消退款
    def doOnlineCancelRefund(self,orderReceipt,payOrder,orderInfo,payOrderItem):
        receiptRecord = OrderReceiptRecordDO()
        #TODO

        return receiptRecord

    def check4Online(self, payOrder, orderInfoList, payOrderItemList):
        if len(orderInfoList) > 1 or len(payOrderItemList) >1:
            # TODO
            self.doRetryProcess(payOrder)
            return False
        return True
    def check4NotNull(self,payOrder, orderInfoList, payOrderItemList):
        if len(orderInfoList) <=0 or len(payOrderItemList) <= 0:
            self.doRetryProcess(payOrder)
            return False
        return True

    def doRetryProcess(self, payOrder):
        # TODO 将初始化失败的payOrder记录一下
        pass

    def getOrderInfoDict(self, outOrderSnList):
        orderInfoDict = {}
        orderInfoList = self.orderInfoMapper.selectByOutOrderSnList(outOrderSnList)

        for orderInfo in orderInfoList:
            orderInfoEntry = orderInfoDict[orderInfo.orderSn]
            if orderInfoEntry == None:
                orderInfoEntry = []
            orderInfoEntry.append(orderInfo)
        return orderInfoDict

    def getPayOrderItemDict(self, payOrderIdList):
        payOrderItemDict = {}
        payOrderItemList = self.payOrderItemMapper.selectByOutOrderSnList(payOrderIdList)
        for payOrderItem in payOrderItemList:
            payOrderItemEntry = payOrderItemDict[payOrderItem.outOrderSn]

            if payOrderItemEntry == None:
                payOrderItemEntry = []
            payOrderItemEntry.append(payOrderItem)
        return payOrderItemDict


def testFunc(var):
    if var == 1:
        return

    return 1,2

if __name__ == '__main__':
    i = 0
    while True:
        timeSleep.sleep(1)
        try:
            print "第%d次尝试" %(i)
            i+=1

            raise Exception

        except Exception,e:
            print e
            break








