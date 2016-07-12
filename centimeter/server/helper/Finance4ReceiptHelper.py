# coding=utf-8
import time

import traceback
from common.config import ReceiptConfig
from dal.domain.do.OrderReceiptDO import OrderReceiptDO
from dal.domain.do.OrderReceiptRecordDO import OrderReceiptRecordDO
from dal.domain.do.SaleReturnExchangeBillEntryDO import  SaleReturnExchangeBillEntryDO
from dal.domain.do.ReturnGoodsBillEntryDO import ReturnGoodsBillEntryDO

from dal.mapper.OrderInfoMapper import OrderInfoMapper
from dal.mapper.OrderReceiptMapper import OrderReceiptMapper
from dal.mapper.OrderReceiptRecordMapper import OrderReceiptRecordMapper
from dal.mapper.PayOrderItemMapper import PayOrderItemMapper
from dal.mapper.PayOrderMapper import PayOrderMapper
from dal.mapper.RefundBillMapper import RefundBillMapper
from dal.mapper.ReturnGoodsBillEntryMapper import ReturnGoodsBillEntryMapper
from dal.mapper.ReturnGoodsBillMapper import ReturnGoodsBillMapper
from dal.mapper.ReturnOrderInfoMapper import ReturnOrderInfoMapper
from dal.mapper.SaleReturnExchangeBillEntryMapper import SaleReturnExchangeBillEntryMapper
from dal.mapper.SaleReturnExchangeBillMapper import SaleReturnExchangeBillMapper
from facade.impl.OrderReceiptFacadeImpl import OrderReceiptFacadeImpl
from server.domain.ReceiptInitParam import ReceiptInitParam
from server.helper.ReceiptErrorLogTool import ReceiptErrorLogTool

__author__ = 'chenjinlong'
class Finance4ReceiptHelper():
    ONLINE_PAY_TYPE = 'ONLINE_PAY_TYPE'

    COD_CASH_PAY_TYPE = 'COD_CASH_PAY_TYPE'

    COD_POS_PAY_TYPE = 'COD_POS_PAY_TYPE'

    FINANCE_PAY_TYPE = 'FINANCE_PAY_TYPE'

    CWQRSK_TRADE_STATU = 'CWQRSK'

    # 用于不同的应收操作:
    # 在线支付
    SPLIT_ORDER_ORI_INVALID_PROCESS = "SPLIT_ORDER_ORI_INVALID_PROCESS"
    ONLINE_CANCEL_PROCESS = "ONLINE_CANCEL_PROCESS"
    ONLINE_CANCEL_RETURN_PROCESS = "ONLINE_CANCEL_RETURN_PROCESS"
    RETURN_GOODS_REFUND_PROCESS = "RETURN_GOODS_REFUND_PROCESS"
    RETURN_GOODS_RERUND_PROCESS = "RETURN_GOODS_RERUND_PROCESS"
    RETURN_GOODS_PROCESS = "RETURN_GOODS_PROCESS"
    ONLINE_REJECT_REFUND_PROCESS = "ONLINE_REJECT_REFUND_PROCESS"
    ONLINE_REJECT_PROCESS = "ONLINE_PART_REJECT_PROCESS"
    ONLINE_OUT_STOCK_PROCESS = "ONLINE_OUT_STOCK_PROCESS"
    SPLIT_ORDER_CHILD_PROCESS = "SPLIT_ORDER_CHILD_PROCESS"
    ONLINE_RECEIVED_PROCESS = "ONLINE_RECEIVED_PROCESS"
    MERGE_ORDER_ORI_INVALID_PROCESS = "MERGE_ORDER_ORI_INVALID_PROCESS"

    # 货到付款 现金
    COD_CASH_ALL_REJECT_PROCESS = "COD_CASH_ALL_REJECT_PROCESS"
    COD_CASH_PART_REJECT_PAID_CONFIRM_PROCESS = "COD_CASH_PART_REJECT_PAID_CONFIRM_PROCESS"
    COD_CASH_PART_REJECT_PROCESS = "COD_CASH_PART_REJECT_PROCESS"
    COD_CASH_PAID_CONFIRM_PROCESS = "COD_CASH_PAID_CONFIRM_PROCESS"
    COD_OUT_STOCK_PROCESS = "COD_OUT_STOCK_PROCESS"

    # 货到付款 POS
    COD_POS_PAID_PROCESS = "COD_POS_PAID_PROCESS"

    COD_POS_PART_REJECT_PAID_CONFIRM_PROCESS = "COD_POS_PART_REJECT_PAID_CONFIRM_PROCESS"

    COD_POS_PART_REJECT_PART_PAID_PROCESS = "COD_POS_PART_REJECT_PART_PAID_PROCESS"

    COD_POS_PART_REJECT_PROCESS = "COD_POS_PART_REJECT_PROCESS"

    COD_POS_PART_PAID_CONFRIM_PROCESS = "COD_POS_PART_PAID_CONFRIM_PROCESS"

    COD_POS_PART_PAID_PROCESS = "COD_POS_PART_PAID_PROCESS"

    COD_POS_OUT_STOCK_PROCESS = "COD_POS_OUT_STOCK_PROCESS"

    # 金融订单
    FINANCE_SPLIT_ORI_INVALID_PROCESS = "FINANCE_SPLIT_ORI_INVALID_PROCESS"
    FINANCE_SPLIT_CHILED_ORDER_PROCESS = "FINANCE_SPLIT_CHILED_ORDER_PROCESS"
    FINANCE_CONFIRMED_NO_OUTSTOCK_PROCESS = "FINANCE_CONFIRMED_NO_OUTSTOCK_PROCESS"
    FINANCE_CONFIRMED_RECEIVED_OUT_STOCK_PROCESS = "FINANCE_CONFIRMED_RECEIVED_OUT_STOCK_PROCESS"
    FINANCE_SPLIT_NEW_ORDER_RETURN_GOODS_REFUND_PROCESS = "FINANCE_SPLIT_NEW_ORDER_RETURN_GOODS_REFUND_PROCESS"
    FINANCE_COMMON_RETURN_GOODS_REFUND_PROCESS = "FINANCE_COMMON_RETURN_GOODS_REFUND_PROCESS"
    FINANCE_SPLIT_NEW_ORDER_RETURN_GOODS_PROCESS = "FINANCE_SPLIT_NEW_ORDER_RETURN_GOODS_PROCESS"
    FINANCE_COMMON_RETURN_GOODS_PROCESS = "FINANCE_COMMON_RETURN_GOODS_PROCESS"
    FINANCE_SPLIT_CHILD_ORDER_OUTSTOCK_PROCESS = "FINANCE_SPLIT_CHILD_ORDER_OUTSTOCK_PROCESS"
    FINANCE_CONFIRMED_RECEIVED_OUTSTOCK_PROCESS = "FINANCE_CONFIRMED_RECEIVED_OUTSTOCK_PROCESS"


    # 换货订单
    EXCHANGE_PAID_CONFIRM_PROCESS = "EXCHANGE_PAID_CONFIRM_PROCESS"
    EXCHANGE_OUTSTOCK_PROCESS = "EXCHANGE_OUTSTOCK_PROCESS"


    DO_NOTHING = "DO_NOTHING"

    ONLINE_PAY_TYPE_LIST = [1,4,5,6,7,8,9,10,11,14,17,18,22,23,34]

    COD_CASH_PAY_TYPE_LIST = [3,12,13,19,20,21,25,26,27,28,29,30]

    COD_POS_PAY_TYPE_LIST = [16]

    FINANCE_PAY_TYPE_LIST = [31]

    orderInfoMapper = OrderInfoMapper()

    orderReceiptMapper = OrderReceiptMapper()

    orderReceiptRecordMapper = OrderReceiptRecordMapper()

    payOrderMapper = PayOrderMapper()

    payOrderItemMapper = PayOrderItemMapper()

    orderReceiptFacade = OrderReceiptFacadeImpl()

    returnOrderInfoMapper = ReturnOrderInfoMapper()

    saleReturnExchangeBillMapper = SaleReturnExchangeBillMapper()

    returnGoodsBillMapper = ReturnGoodsBillMapper()

    saleReturnExchangeBillEntryMapper = SaleReturnExchangeBillEntryMapper()

    returnGoodsBillEntryMapper = ReturnGoodsBillEntryMapper()

    refundBillMapper = RefundBillMapper()

    receiptErrorLogTool = ReceiptErrorLogTool()

    def __init__(self):
        self.BATCH_NUMBER = 50
        self.fileInput = open("../output/receipt/retryfile.txt","w")

    def getPayOrderDict(self, outOrderSnList):
        payOrderDict = {}
        payOrderIdList = []
        payOrderDOList = self.payOrderMapper.selectByOutOrderSnList(outOrderSnList)

        for payOrderDO in payOrderDOList:
            payOrderIdList.append(payOrderDO.id)
            payOrderEntry = payOrderDict.get(payOrderDO.outOrderSn,[])
            payOrderEntry.append(payOrderDO)
            payOrderDict[payOrderDO.outOrderSn] = payOrderEntry
        return payOrderDict,payOrderIdList

    def getPayOrderItemDict(self, payOrderIdList):
        payOrderItemDict = {}
        payOrderItemList = self.payOrderItemMapper.selectByOutOrderSnList(payOrderIdList)
        for payOrderItem in payOrderItemList:
            payOrderItemEntry = payOrderItemDict.get(payOrderItem.payOrderId,None)

            if payOrderItemEntry == None:
                payOrderItemEntry = []
            payOrderItemEntry.append(payOrderItem)
            payOrderItemDict[payOrderItem.payOrderId] = payOrderItemEntry
        return payOrderItemDict

    def getReturnOrderInfoDict(self, outOrderSnList):
        returnOrderInfoDict = {}
        returnOrderInfoList = self.returnOrderInfoMapper.selectByOrderSnList(outOrderSnList)
        for returnOrderInfo in returnOrderInfoList:
            returnOrderInfoDict[returnOrderInfo.billNo] = returnOrderInfo

        return returnOrderInfoDict

    def getSaleReturnExchangeBillDict(self, outOrderSnList):
        saleReturnExcahgneBillDict = {}
        saleReturnExchangeBillIdList = []
        saleReturnExchangeBillNoList = []
        saleReturnExchangeBillDOList = self.saleReturnExchangeBillMapper.selectReturnGoods4PartReject(outOrderSnList)

        for saleReturnExchangeBillDO in saleReturnExchangeBillDOList:
            saleReturnExchangeBillIdList.append(saleReturnExchangeBillDO.id)
            saleReturnExchangeBillNoList.append(saleReturnExchangeBillDO.billNo)
            entry = saleReturnExcahgneBillDict.get(saleReturnExchangeBillDO.mainBillNo,None)
            if entry is None:
                entry = []
            entry.append(saleReturnExchangeBillDO)
            saleReturnExcahgneBillDict[saleReturnExchangeBillDO.mainBillNo] = entry
        return saleReturnExcahgneBillDict,saleReturnExchangeBillIdList,saleReturnExchangeBillNoList

    def getReturnGoodsBillDict(self, outOrderSnList):
        returnGoodsBillDict = {}
        returnGoodsBillIdList = []
        returnGoodsBillNoList = []
        returnGoodsBillDOList = self.returnGoodsBillMapper.selectReturnGoodsInfo(outOrderSnList)


        for returnGoodsBillDO in returnGoodsBillDOList:
            entry = returnGoodsBillDict.get(returnGoodsBillDO.mainBillNo,None)
            returnGoodsBillIdList.append(returnGoodsBillDO.id)
            returnGoodsBillNoList.append(returnGoodsBillDO.billNo)
            if entry is None:
                entry = []
            entry.append(returnGoodsBillDO)
            returnGoodsBillDict[returnGoodsBillDO.mainBillNo] = entry
        return returnGoodsBillDict,returnGoodsBillIdList,returnGoodsBillNoList

    def getSaleReturnExchangeBillEntryDict(self, saleReturnExchangeBillIdList):
        if saleReturnExchangeBillIdList is None or len(saleReturnExchangeBillIdList) == 0:
            return {}
        saleReturnExchangeBillEntryDict = {}
        saleReturnExchangeBillEntryDOList = self.saleReturnExchangeBillEntryMapper.selectByBillIdList(saleReturnExchangeBillIdList)


        for saleReturnExchangeBillEntryDO in saleReturnExchangeBillEntryDOList:
            entry = saleReturnExchangeBillEntryDict.get(saleReturnExchangeBillEntryDO.billId,[])
            entry.append(saleReturnExchangeBillEntryDO)
            saleReturnExchangeBillEntryDict[saleReturnExchangeBillEntryDO.billId] = entry

        return saleReturnExchangeBillEntryDict



    def getReturnGoodsBillEntryDict(self, returnGoodsBillIdList):
        if returnGoodsBillIdList is None or len(returnGoodsBillIdList) == 0:
            return {}
        returnGoodsBillEntryDict = {}
        returnGoodsBillEntryDOList = self.returnGoodsBillEntryMapper.selectByBillIdList(returnGoodsBillIdList)

        for returnGoodsBillEntryDO in returnGoodsBillEntryDOList:
            entry = returnGoodsBillEntryDict.get(returnGoodsBillEntryDO.billId,[])
            entry.append(returnGoodsBillEntryDO)
            returnGoodsBillEntryDict[returnGoodsBillEntryDO.billId] = entry

        return returnGoodsBillEntryDict


    def getRefundBillDict(self, billNoList):
        if billNoList is None or len(billNoList) == 0:
            return {}
        refundBillDict = {}
        refundBillDOList = self.refundBillMapper.selectByReturnGoodsBillNoList(billNoList)
        for refundBillDO in refundBillDOList:
            entry = refundBillDict.get(refundBillDO.returnGoodsBillNo,[])
            entry.append(refundBillDO)
            refundBillDict[refundBillDO.returnGoodsBillNo] = entry

        return refundBillDict

    def getProcessOrderTest(self,orderSnList):
        return self.orderInfoMapper.selectByOutOrderSnList(orderSnList)

    def getProcessOrder4ErrorOrder(self,orderSnList):
        return self.orderInfoMapper.selectByOutOrderSnList(orderSnList)

    def getProcessOrder(self,start ,num):
        if ReceiptConfig.debug4SingleOrder:
            return None

        if start == None:
            start = 0
        if num == None:
            num = self.BATCH_NUMBER


        orderInfoDOList = self.orderInfoMapper.selectBatch(start,num)
        if len(orderInfoDOList)==0 or orderInfoDOList == None:
            return None

        orderInfoDOList = self.doFilterOrder(orderInfoDOList)
        # orderInfoDOList = self.doFilterOrder4Test(orderInfoDOList)
        return orderInfoDOList

    def batchDoProcessFinanceReceipt(self,orderInfoDOList):
        if len(orderInfoDOList) == 0:
            return []
        orderReceipt4InsertList,receiptRecord4InsertList,errorOrderInfoList = self.buildReceiptInfo(orderInfoDOList)
        self.orderReceiptFacade.doOrderReceiptDataInit(orderReceipt4InsertList,receiptRecord4InsertList)
        return errorOrderInfoList

    def batchDoProcessFinanceReceiptTest(self,orderInfoDOList,receiptTypeMap):
        if len(orderInfoDOList) == 0:
            return []
        orderReceipt4InsertList,receiptRecord4InsertList,errorOrderInfoList = self.buildReceiptInfo(orderInfoDOList)
        for orderReceiptRecord in receiptRecord4InsertList:
            key = orderReceiptRecord.receiptAction
            count = receiptTypeMap.get(key,0)
            count +=1
            receiptTypeMap[key] = count

        return errorOrderInfoList



    def buildReceiptInfo(self,orderInfoDOList):
        outOrderSnList = []

        errorOrderInfoList = []

        for orderInfoDO in orderInfoDOList:
            outOrderSnList.append(orderInfoDO.orderSn)

        payOrderDict,payOrderIdList = self.getPayOrderDict(outOrderSnList)
        if not payOrderDict:
            raise Exception("本组订单没有找到对应的支付订单")
        payOrderItemDict = self.getPayOrderItemDict(payOrderIdList)
        # orderReceiptDict = self.initOrderReceiptInfo4Array(orderInfoDOList,payOrderDict,payOrderItemDict)
        returnOrderInfoDict = self.getReturnOrderInfoDict(outOrderSnList)
        saleReturnExchangeBillDict,saleReturnExchangeBillIdList,saleReturnExchangeBillNoList = self.getSaleReturnExchangeBillDict(outOrderSnList)
        saleReturnExchangeBillEntryDict = self.getSaleReturnExchangeBillEntryDict(saleReturnExchangeBillIdList)
        returnGoodsBillDict,returnGoodsBillIdList,returnGoodsBillNoList = self.getReturnGoodsBillDict(outOrderSnList)
        returnGoodsBillEntryDict = self.getReturnGoodsBillEntryDict(returnGoodsBillIdList)
        refundBillDict = self.getRefundBillDict(returnGoodsBillNoList+saleReturnExchangeBillNoList)

        orderReceipt4InsertList = []
        receiptRecord4InsertList = []
        for orderInfoDO in orderInfoDOList:
            payOrderDOList = payOrderDict.get(orderInfoDO.orderSn,None)
            receiptInitParam = ReceiptInitParam()
            receiptInitParam.orderInfoDO = orderInfoDO
            receiptInitParam.payOrderDOList = payOrderDOList
            receiptInitParam.payOrderItemDict = payOrderItemDict
            # receiptInitParam.orderReceiptDict = orderReceiptDict

            returnOrderInfoDO = returnOrderInfoDict.get(orderInfoDO.orderSn,None)

            receiptInitParam.returnOrderInfoDO = returnOrderInfoDO

            saleReturnExchangeBillDOList = saleReturnExchangeBillDict.get(orderInfoDO.orderSn,[])

            receiptInitParam.saleReturnExchangeDOList = saleReturnExchangeBillDOList
            refundBillDOList = []
            saleReturnExchangeBillEntryDOList = []
            for saleReturnExchangeBillDO in saleReturnExchangeBillDOList:

                saleReturnExchangeBillEntryDOList += saleReturnExchangeBillEntryDict.get(saleReturnExchangeBillDO.id,[])
                refundBillDOList += refundBillDict.get(saleReturnExchangeBillDO.billNo,[])

            receiptInitParam.saleReturnExchangeBillEntryDOList = saleReturnExchangeBillEntryDOList


            returnGoodsBillDOList = returnGoodsBillDict.get(orderInfoDO.orderSn,[])

            receiptInitParam.returnGoodsBillDOList = returnGoodsBillDOList

            returnGoodsBillEntryDOList = []

            for returnGoodsBillDO in returnGoodsBillDOList:
                returnGoodsBillEntryDOList += returnGoodsBillEntryDict.get(returnGoodsBillDO.id,[])
                refundBillDOList += refundBillDict.get(returnGoodsBillDO.billNo,[])

            receiptInitParam.returnGoodsBillEntryDOList = returnGoodsBillEntryDOList
            receiptInitParam.refundBillDOList = refundBillDOList



            try :
                orderReceipt,receiptRecord4ReceiptList = self.doAssemble(receiptInitParam)
            except Exception:
                if ReceiptConfig.isDebug:
                    traceback.print_exc()
                errorOrderInfoList.append(orderInfoDO)
                continue

            if orderReceipt is None:
                continue
            orderReceipt4InsertList.append(orderReceipt)
            receiptRecord4InsertList += receiptRecord4ReceiptList

        return orderReceipt4InsertList,receiptRecord4InsertList,errorOrderInfoList

    def flushErrorInfo(self):
        self.receiptErrorLogTool.flush()


    def doAssemble(self,receiptInitParam):
        # 这里的payOrderDOList的outOrderSn都是相同的
        if receiptInitParam.payOrderDOList == None or len(receiptInitParam.payOrderDOList)<=0:
            raise Exception("payOrderDOList为空")
        stdPayOrderDO = receiptInitParam.payOrderDOList[0]
        for payOrderDO in receiptInitParam.payOrderDOList:
            if payOrderDO.outOrderSn != stdPayOrderDO.outOrderSn:
                raise Exception("outOrderSn必须一致")

        orderInfoDO = receiptInitParam.orderInfoDO
        # orderReceipt =  receiptInitParam.orderReceiptDict[orderInfoDO.orderSn]
        #初始化orderReceipt数据
        orderReceipt =  self.initOrderReceiptInfo4Entry(receiptInitParam)

        if orderReceipt is None:
            raise Exception("orderReceipt数据未初始化,orderId = "+ orderInfoDO.id)


        receiptType = self.receiptTypeJuge(receiptInitParam)

        if ReceiptConfig.isDebug:
            print "匹配应收动作:%s," %(receiptType),"orderSn="+orderInfoDO.orderSn


        if receiptType == self.ONLINE_RECEIVED_PROCESS:
            receiptRecord4ReceivedList = self.doOnlineReceipt4OnlineReceived(orderReceipt,receiptInitParam)
        elif receiptType == self.MERGE_ORDER_ORI_INVALID_PROCESS:
            receiptRecord4ReceivedList = self.doOnlineReceipt4MergeOrderOriInvalid(orderReceipt,receiptInitParam)

        elif receiptType == self.ONLINE_CANCEL_PROCESS:
            receiptRecord4ReceivedList = self.doOnlineReceipt4OnlineCancel(orderReceipt,receiptInitParam)
        elif receiptType == self.ONLINE_CANCEL_RETURN_PROCESS:
            receiptRecord4ReceivedList = self.doOnlineReceipt4CancelRefund(orderReceipt,receiptInitParam)
        elif receiptType == self.ONLINE_OUT_STOCK_PROCESS:
            receiptRecord4ReceivedList = self.doOnlineSuccessReceipt(orderReceipt,receiptInitParam)
        elif receiptType == self.ONLINE_REJECT_PROCESS:
            receiptRecord4ReceivedList = self.doOnlineReceipt4Reject(orderReceipt,receiptInitParam)
        elif receiptType == self.ONLINE_REJECT_REFUND_PROCESS:
            receiptRecord4ReceivedList = self.doOlineReceipt4RejectRefund(orderReceipt,receiptInitParam)
        elif receiptType == self.RETURN_GOODS_PROCESS:
            receiptRecord4ReceivedList = self.doOlineReceipt4ReturnGoods(orderReceipt,receiptInitParam)
        elif receiptType == self.RETURN_GOODS_RERUND_PROCESS:
            receiptRecord4ReceivedList = self.doOnlineReceipt4ReturnGoodsRefund(orderReceipt,receiptInitParam)
        elif receiptType == self.SPLIT_ORDER_ORI_INVALID_PROCESS:
            receiptRecord4ReceivedList = self.doOnlineReceipt4SplitOrder(orderReceipt,receiptInitParam)

        elif receiptType == self.COD_CASH_ALL_REJECT_PROCESS:
            receiptRecord4ReceivedList = self.doCodCashReceipt4AllReject(orderReceipt,receiptInitParam)
        elif receiptType == self.COD_CASH_PART_REJECT_PAID_CONFIRM_PROCESS:
            receiptRecord4ReceivedList = self.doCodCashReceipt4PartRejectPaidConfirm(orderReceipt,receiptInitParam)
        elif receiptType == self.COD_CASH_PART_REJECT_PROCESS:
            receiptRecord4ReceivedList = self.doCodCashReceipt4PartReject(orderReceipt,receiptInitParam)
        elif receiptType == self.COD_CASH_PAID_CONFIRM_PROCESS:
            receiptRecord4ReceivedList = self.doCodCashReceipt4CodPaidConfirm(orderReceipt,receiptInitParam)
        elif receiptType == self.COD_OUT_STOCK_PROCESS:
            receiptRecord4ReceivedList = self.doCodCashReceipt4OutStock(orderReceipt,receiptInitParam)

        elif receiptType == self.COD_POS_PAID_PROCESS:
            receiptRecord4ReceivedList = self.doCodPosReceipt4PosPaid(orderReceipt,receiptInitParam)
        elif receiptType == self.COD_POS_PART_REJECT_PAID_CONFIRM_PROCESS:
            receiptRecord4ReceivedList = self.doCodPosReceipt4PRPPConfirm(orderReceipt,receiptInitParam)
        elif receiptType == self.COD_POS_PART_REJECT_PART_PAID_PROCESS:
            receiptRecord4ReceivedList = self.doCodPosReceipt4PartRejectPartPaid(orderReceipt,receiptInitParam)
        elif receiptType == self.COD_POS_PART_REJECT_PROCESS:
            receiptRecord4ReceivedList = self.doCodPosReceipt4PartReject(orderReceipt,receiptInitParam)
        elif receiptType == self.COD_POS_PART_PAID_CONFRIM_PROCESS:
            receiptRecord4ReceivedList = self.doCodPosReceipt4PartPaidConfirm(orderReceipt,receiptInitParam)
        elif receiptType == self.COD_POS_PART_PAID_PROCESS:
            receiptRecord4ReceivedList = self.doCodPosReceipt4PartPaid(orderReceipt,receiptInitParam)
        elif receiptType == self.COD_POS_OUT_STOCK_PROCESS:
            receiptRecord4ReceivedList = self.doCodPosReceipt4CodOutStock(orderReceipt,receiptInitParam)

        elif receiptType == self.FINANCE_SPLIT_ORI_INVALID_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4SplitOriInvalid(orderReceipt,receiptInitParam)

        elif receiptType == self.FINANCE_SPLIT_CHILED_ORDER_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4SplitChildOrder(orderReceipt,receiptInitParam)

        elif receiptType == self.FINANCE_CONFIRMED_NO_OUTSTOCK_PROCESS:
            receiptRecord4ReceivedList = self.doFinance4ConfirmedNoOutstock(orderReceipt,receiptInitParam)

        elif receiptType == self.FINANCE_CONFIRMED_RECEIVED_OUT_STOCK_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4ConfirmedReceivedOutStock(orderReceipt,receiptInitParam)

        elif receiptType == self.FINANCE_SPLIT_NEW_ORDER_RETURN_GOODS_REFUND_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4SplitNewOrderReturnGoodsRefund(orderReceipt,receiptInitParam)

        elif receiptType == self.FINANCE_COMMON_RETURN_GOODS_REFUND_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4CommonReturnGoodsRefund(orderReceipt,receiptInitParam)

        elif receiptType == self.FINANCE_SPLIT_NEW_ORDER_RETURN_GOODS_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4SplitNewOrderReturnGoods(orderReceipt,receiptInitParam)

        elif receiptType == self.FINANCE_COMMON_RETURN_GOODS_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4CommonReturnGoods(orderReceipt,receiptInitParam)

        elif receiptType == self.FINANCE_SPLIT_CHILD_ORDER_OUTSTOCK_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4SplitChildOrderOutStock(orderReceipt,receiptInitParam)

        elif receiptType == self.FINANCE_CONFIRMED_RECEIVED_OUTSTOCK_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4ConfirmedReceivedOutStock(orderReceipt,receiptInitParam)

        elif receiptType == self.EXCHANGE_PAID_CONFIRM_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4ExchangePaidConfirm(orderReceipt,receiptInitParam)

        elif receiptType == self.EXCHANGE_OUTSTOCK_PROCESS:
            receiptRecord4ReceivedList = self.doFinanceReceipt4ExchangeOutStock(orderReceipt,receiptInitParam)
        elif receiptType == self.DO_NOTHING:
            print "订单orderId = %d匹配后不做任何应收初始化" %orderInfoDO.id
            self.receiptErrorLogTool.write(orderInfoDO)
            return None,[]
        else:
            raise Exception("订单未知应收流程:orderId = " + orderInfoDO.id)

        self.doReceipt4ReturnProcess(receiptRecord4ReceivedList,orderReceipt,receiptInitParam)




        return orderReceipt,receiptRecord4ReceivedList


    def receiptTypeJuge(self,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        orderFlags = ","+orderInfoDO.orderFlags+"," if orderInfoDO.orderFlags else ""
        if ",HHDD," in orderFlags:
            return self.receiptTypeJuge4ExchangeOrder(receiptInitParam)

        payId = orderInfoDO.payId
        payType = self.checkPayType(payId)
        if (payType == self.ONLINE_PAY_TYPE):
            return self.receiptTypeJuge4Online(receiptInitParam)

        if (payType == self.COD_CASH_PAY_TYPE):
            return self.receiptTypeJuge4CodCash(receiptInitParam)

        if (payType == self.COD_POS_PAY_TYPE):
            return self.receiptTypeJuge4CodPOS(receiptInitParam)

        if (payType == self.FINANCE_PAY_TYPE):
            return self.receiptTypeJuge4Finance(receiptInitParam)
        raise Exception("Error Pay Status!!!")

    # 线上支付在预收流程
    def doOnlineReceipt4OnlineReceived(self,orderReceipt,receiptInitParam):
        # self.checkReceipt4Online(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList.append(self.doOnline4Recevied(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # 线上支付在出库流程,其实隐含包含了财务确认收款
    def doOnlineSuccessReceipt(self,orderReceipt,receiptInitParam):
        # self.checkReceipt4Online(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doOnlineReceipt4OnlineReceived(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doOnline4OutStock(orderReceipt,receiptInitParam))
        # receiptRecord4ReceivedList.append(self.doOnline4PaidConfirm(orderReceipt,payOrder,orderInfo,payOrderItem))

        return receiptRecord4ReceivedList

    # 线上支付在取消路程
    def doOnlineReceipt4OnlineCancel(self,orderReceipt,receiptInitParam):
        # self.checkReceipt4Online(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doOnlineReceipt4OnlineReceived(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doOnline4Cancel(orderReceipt,receiptInitParam))

        return receiptRecord4ReceivedList

    # 线上支付在订单取消的退款路程
    def doOnlineReceipt4CancelRefund(self,orderReceipt,receiptInitParam):
        # self.checkReceipt4Online(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doOnlineReceipt4OnlineCancel(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doOnline4CancelRefund(orderReceipt,receiptInitParam))

        return receiptRecord4ReceivedList

    # 线上支付在订单部分拒收流程
    def doOnlineReceipt4Reject(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doOnlineSuccessReceipt(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doOnline4Reject(orderReceipt,receiptInitParam))

        return receiptRecord4ReceivedList

    # 线上支付在订单部分拒收退款流程
    def doOlineReceipt4RejectRefund(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doOnlineReceipt4Reject(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doOnline4PartRefund(orderReceipt,receiptInitParam))


        return receiptRecord4ReceivedList

    # 线上支付流程在部分拒收退货流程
    def doOlineReceipt4ReturnGoods(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList + self.doOlineReceipt4RejectRefund(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.do4ReturnGoods(orderReceipt,receiptInitParam))

        return receiptRecord4ReceivedList

    # 线上支付在部分拒收退货退款流程
    def doOnlineReceipt4ReturnGoodsRefund(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doOlineReceipt4ReturnGoods(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.do4ReturnGoodsRefund(orderReceipt,receiptInitParam))


        return receiptRecord4ReceivedList

    # 线上支付在拆单失效流程
    def doOnlineReceipt4SplitOrder(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doOnlineReceipt4OnlineReceived(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.do4SplitOrderOriInvalid(orderReceipt,receiptInitParam))

        return receiptRecord4ReceivedList

    def doOnlineReceipt4MergeOrderOriInvalid(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doOnlineReceipt4OnlineReceived(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.do4MergeOrderOriInvalid(orderReceipt,receiptInitParam))

        return receiptRecord4ReceivedList

    # 在线预收
    def doOnline4Recevied(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        if orderInfoDO.parentId is not None and orderInfoDO.parentId>0 and orderInfoDO.orderStatus!=-3:
            receiptRecord.receiptAction = 'split_order_child'
        else:
            receiptRecord.receiptAction = 'online_received'

        receiptRecord.hasReceivedAmount = orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 在线出库
    def doOnline4OutStock(self,orderReceipt,receiptInitParam):

        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'out_stock'
        receiptRecord.needReceiveAmount = orderInfoDO.orderAmount

        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 在线财务确认收款
    def doOnline4PaidConfirm(self,orderReceipt,receiptInitParam):
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        # 目前什么也不做

        return receiptRecord

    # 部分拒收
    def doOnline4Reject(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        if orderInfoDO.returnAmount != orderInfoDO.orderAmount:
            receiptRecord.receiptAction = 'online_part_reject'
        else:
            receiptRecord.receiptAction = 'online_all_reject'
        receiptRecord.rejectAmount = orderInfoDO.returnAmount
        receiptRecord.needReceiveAmount = 0-orderInfoDO.returnAmount

        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # 拒收退款
    def doOnline4PartRefund(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'online_reject_refund'
        receiptRecord.hasReceivedAmount = 0-orderInfoDO.returnAmount

        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # FIXME 金额不对 退货
    def do4ReturnGoods(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'return_goods'
        receiptRecord.needReceiveAmount = 0-orderInfoDO.returnAmount

        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # FIXME 金额不对 退货退款
    def do4ReturnGoodsRefund(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'return_goods_refund'
        receiptRecord.hasReceivedAmount = 0-orderInfoDO.returnAmount

        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 拆单失效
    def do4SplitOrderOriInvalid(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'split_order_ori_invalid'
        receiptRecord.hasReceivedAmount = 0-orderInfoDO.orderAmount

        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 合单失效
    def do4MergeOrderOriInvalid(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'merge_order_ori_invalid'
        receiptRecord.hasReceivedAmount = 0-orderInfoDO.orderAmount

        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # 取消订单
    def doOnline4Cancel(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'online_cancel'
        receiptRecord.rejectAmount = orderInfoDO.orderAmount

        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 取消退款
    def doOnline4CancelRefund(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'online_cancel_refund'
        receiptRecord.hasReceivedAmount =0- orderInfoDO.orderAmount

        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    #========================货到付款-现金=================================
    # 货到付款现金支付出库流程
    def doCodCashReceipt4OutStock(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList.append(self.doCodCash4OutStock(orderReceipt,receiptInitParam))

        return receiptRecord4ReceivedList

    # 货到付款现金支付财务确认收款流程
    def doCodCashReceipt4CodPaidConfirm(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCodCashReceipt4OutStock(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doCodCash4CodPaidConfirm(orderReceipt,receiptInitParam))

        return receiptRecord4ReceivedList

    # 货到付款现金支付部分拒收流程
    def doCodCashReceipt4PartReject(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCodCashReceipt4OutStock(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doCodCash4CodPartReject(orderReceipt,receiptInitParam))

        return receiptRecord4ReceivedList

    # 货到付款现金支付部分拒收后的财务确认收款流程
    def doCodCashReceipt4PartRejectPaidConfirm(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCodCashReceipt4PartReject(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doCodCash4CodPaidConfirm(orderReceipt,receiptInitParam))

        return receiptRecord4ReceivedList

    # 货到付款现金支付全部拒收流程
    def doCodCashReceipt4AllReject(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCodCashReceipt4OutStock(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doCodCash4CodAllReject(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList



    #货到付款现金支付 出库
    def doCodCash4OutStock(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'out_stock'
        receiptRecord.needReceiveAmount =orderInfoDO.orderAmount

        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 货到付款现金支付 财务确认收款
    def doCodCash4CodPaidConfirm(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'cod_paid_confirm'
        receiptRecord.hasReceivedAmount =orderInfoDO.receiveAmount if orderInfoDO.receiveAmount is not None else 0
        # orderReceipt.hasReceivedCashAmount = orderInfoDO.receiveAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 货到付款现金支付 部分拒收
    def doCodCash4CodPartReject(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'cod_part_reject'
        receiptRecord.rejectAmount = orderInfoDO.returnAmount
        receiptRecord.needReceiveAmount =0-orderInfoDO.returnAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 货到付款现金支付 全部拒收
    def doCodCash4CodAllReject(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'cod_all_reject'
        receiptRecord.rejectAmount = orderInfoDO.orderAmount
        receiptRecord.needReceiveAmount =0-orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    #========================货到付款-POS=================================
    # 货到付款POS支付 出库流程
    def doCodPosReceipt4CodOutStock(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList.append(self.doCodPos4CodOutStock(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # 货到付款POS支付 Pos全部支付流程
    def doCodPosReceipt4PosPaid(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCodPosReceipt4CodOutStock(orderReceipt,receiptInitParam)
        # 历史数据问题，初始化时不计
        receiptRecord4ReceivedList.append(self.doCodPos4PosPaidConfirm(orderReceipt,receiptInitParam))
        # receiptRecord4ReceivedList.append(self.doCodPos4PosPaid(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # 货到付款POS支付 Pos部分支付流程
    def doCodPosReceipt4PartPaid(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCodPosReceipt4CodOutStock(orderReceipt,receiptInitParam)
        # receiptRecord4ReceivedList.append(self.doCodPos4PosPartPaid(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # 货到付款POS支付 POS部分支付财务确认收款
    def doCodPosReceipt4PartPaidConfirm(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCodPosReceipt4PartPaid(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doCodPos4PosPaidConfirm(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # 货到付款POS支付 部分支付
    def doCodPosReceipt4PartRejectPartPaid(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCodPosReceipt4CodOutStock(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doCodPos4PosPartPaid(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # 货到付款POS支付 部分拒收
    def doCodPosReceipt4PartReject(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCodPosReceipt4PartRejectPartPaid(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doCodPos4CodPartReject(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    def doCodPosReceipt4PRPPConfirm(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCodPosReceipt4PartRejectPartPaid(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doCodPos4PosPaidConfirm(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList



    # 货到付款POS支付 出库
    def doCodPos4CodOutStock(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'out_stock'
        receiptRecord.needReceiveAmount =orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 货到付款POS支付 Pos全部支付
    def doCodPos4PosPaid(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'pos_paid'
        receiptRecord.hasReceivedAmount =orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 货到付款POS支付 pos部分支付
    def doCodPos4PosPartPaid(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'pos_part_paid'
        receiptRecord.hasReceivedAmount =orderInfoDO.payFee
        self.doProcessReceipt(orderReceipt,receiptRecord)

        return receiptRecord

    # 货到付款POS支付 财务确认收款
    def doCodPos4PosPaidConfirm(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'pos_paid'
        # receiptRecord.hasReceivedAmount =orderInfoDO.receiveAmount-orderInfoDO.payFee
        receiptRecord.hasReceivedAmount =orderInfoDO.receiveAmount if orderInfoDO.receiveAmount is not None else 0
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # 货到付款POS支付 部分拒收
    def doCodPos4CodPartReject(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'cod_part_reject'
        receiptRecord.rejectAmount = orderInfoDO.returnAmount
        receiptRecord.needReceiveAmount =0-orderInfoDO.returnAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord


    #========================金融订单=================================

    # 金融订单 实收流程
    def doFinanceReceipt4ConfirmedNoOutstock(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList.append(self.doFinance4ConfirmedNoOutstock(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # FINANCE_CONFIRMED_RECEIVED_OUTSTOCK_PROCESS = "FINANCE_CONFIRMED_RECEIVED_OUTSTOCK_PROCESS"
    # 金融订单 实收出库流程
    def doFinanceReceipt4ConfirmedOutstock(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doFinanceReceipt4ConfirmedNoOutstock(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doFinance4OutStock(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList


    # FINANCE_CONFIRMED_RECEIVED_OUT_STOCK_PROCESS = "FINANCE_CONFIRMED_RECEIVED_OUT_STOCK_PROCESS"
    # 金融订单 预收出库流程
    def doFinanceReceipt4ConfirmedReceivedOutStock(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList.append(self.doFinance4OutStock(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # 金融订单 预收流程
    def doFinanceReceipt4ConfirmedReceived(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doFinanceReceipt4ConfirmedReceivedOutStock(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doFinance4OutStock(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # FINANCE_SPLIT_ORI_INVALID_PROCESS = "FINANCE_SPLIT_ORI_INVALID_PROCESS"
    # 金融订单 拆单失效流程
    def doFinanceReceipt4SplitOriInvalid(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doFinanceReceipt4ConfirmedNoOutstock(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doFinance4SplitOriInvalid(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # FINANCE_SPLIT_CHILED_ORDER_PROCESS = "FINANCE_SPLIT_CHILED_ORDER_PROCESS"
    # 金融订单 拆单新单流程
    def doFinanceReceipt4SplitChildOrder(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList.append(self.doFinance4SplitChildOrder(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList


    # FINANCE_SPLIT_CHILD_ORDER_OUTSTOCK_PROCESS = "FINANCE_SPLIT_CHILD_ORDER_OUTSTOCK_PROCESS"
    # 金融订单 拆单新单出库流程
    def doFinanceReceipt4SplitChildOrderOutStock(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doFinanceReceipt4SplitChildOrder(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doFinance4OutStock(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList


    # FINANCE_COMMON_RETURN_GOODS_PROCESS = "FINANCE_COMMON_RETURN_GOODS_PROCESS"
    #金融订单 正常单退货流程
    def doFinanceReceipt4CommonReturnGoods(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doFinanceReceipt4ConfirmedReceivedOutStock(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doFinance4ReturnGoods(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # FINANCE_COMMON_RETURN_GOODS_REFUND_PROCESS = "FINANCE_COMMON_RETURN_GOODS_REFUND_PROCESS"
    #金融订单 正常单退货退款流程
    def doFinanceReceipt4CommonReturnGoodsRefund(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doFinanceReceipt4CommonReturnGoods(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doFinance4ReturnGoodsRefund(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # FINANCE_SPLIT_NEW_ORDER_RETURN_GOODS_PROCESS = "FINANCE_SPLIT_NEW_ORDER_RETURN_GOODS_PROCESS"
    #金融订单 拆单子单的退货流程
    def doFinanceReceipt4SplitNewOrderReturnGoods(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doFinanceReceipt4SplitChildOrderOutStock(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doFinance4ReturnGoods(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # FINANCE_SPLIT_NEW_ORDER_RETURN_GOODS_REFUND_PROCESS = "FINANCE_SPLIT_NEW_ORDER_RETURN_GOODS_REFUND_PROCESS"
    #金融订单 拆单子单退货退款流程
    def doFinanceReceipt4SplitNewOrderReturnGoodsRefund(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doFinanceReceipt4SplitNewOrderReturnGoods(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doFinance4ReturnGoodsRefund(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # 金融订单 预收
    def doFinance4ConfirmedNoOutstock(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'finance_order_tq_confirmed_no_outstock'
        receiptRecord.hasReceivedAmount =orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # 金融订单 实收
    def doFinance4ConfirmedReceived(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'finance_order_tq_confirmed_received'
        receiptRecord.hasReceivedAmount =orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # 金融订单 出库
    def doFinance4OutStock(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'out_stock'
        receiptRecord.needReceiveAmount = orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # 金融订单 拆单失效
    def doFinance4SplitOriInvalid(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'split_order_ori_invalid'
        receiptRecord.hasReceivedAmount = 0-orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # 金融订单 拆单新单
    def doFinance4SplitChildOrder(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'split_order_child'
        receiptRecord.hasReceivedAmount = orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # FIXME 金额不对 金融订单 退货
    def doFinance4ReturnGoods(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'finance_return_goods'
        receiptRecord.needReceiveAmount = 0-orderInfoDO.returnAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    # FIXME 金额不对 金融订单 退货退款
    def doFinance4ReturnGoodsRefund(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'finance_return_goods_refund'
        receiptRecord.hasReceivedAmount = 0-orderInfoDO.returnAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    #========================换货订单=================================

    #金融订单 换货出库流程
    def doFinanceReceipt4ExchangeOutStock(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList.append(self.doFinance4ExchangeOutStock(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    #金融订单 换货财务确认收款
    def doFinanceReceipt4ExchangePaidConfirm(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doFinanceReceipt4ExchangeOutStock(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doFinance4ExchangePaidConfirm(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # 换货订单 换货出库
    def doFinance4ExchangeOutStock(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'out_stock'
        receiptRecord.needReceiveAmount = orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord


    # 换货订单 换货出库
    def doFinance4ExchangePaidConfirm(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        receiptRecord.receiptAction = 'cod_paid_confirm'
        receiptRecord.hasReceivedAmount = orderInfoDO.orderAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    def initOrderReceiptRecordDO(self,orderReceipt,receiptInitParam):
        payOrderDO = receiptInitParam.payOrderDOList[0]
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = OrderReceiptRecordDO()
        receiptRecord.gmtCreate = orderInfoDO.gmtCreate
        receiptRecord.creator = orderInfoDO.creator
        receiptRecord.gmtModified = orderInfoDO.gmtCreate
        receiptRecord.modifier = orderInfoDO.modifier
        receiptRecord.financeAccountId = payOrderDO.financeAccountId
        receiptRecord.platformId = payOrderDO.platformId
        receiptRecord.platformName = payOrderDO.platformName
        receiptRecord.outOrderSn = payOrderDO.outOrderSn

        receiptRecord.rejectAmount = 0
        receiptRecord.refundAmount = 0
        receiptRecord.needReceiveAmount = 0
        receiptRecord.receiptRecord = 0
        receiptRecord.remainingAmount = 0
        receiptRecord.hasReceivedAmount = 0
        return receiptRecord

    def doProcessReceipt(self, orderReceipt, receiptRecord):
        orderReceipt.rejectAmount = orderReceipt.rejectAmount+receiptRecord.rejectAmount
        orderReceipt.needReceiveAmount = orderReceipt.needReceiveAmount + receiptRecord.needReceiveAmount
        orderReceipt.hasReceivedAmount = orderReceipt.hasReceivedAmount + receiptRecord.hasReceivedAmount
        orderReceipt.refundAmount = orderReceipt.refundAmount+receiptRecord.refundAmount
        orderReceipt.remainingAmount = orderReceipt.needReceiveAmount - orderReceipt.hasReceivedAmount
        receiptRecord.remainingAmount = orderReceipt.remainingAmount

    def checkReceipt4Online(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        if receiptInitParam.payOrderDOList == None or len(receiptInitParam.payOrderDOList)!=1:
            raise Exception("在上支付预收流水,其支付订单数量必须为1,orderId="+str(orderInfoDO.id))
        payOrderDO = receiptInitParam.payOrderDOList[0]
        payOrderItemDOList = receiptInitParam.payOrderItemDict.get(payOrderDO.id,None)
        if payOrderItemDOList == None or len(payOrderItemDOList)!=1:
            raise Exception("在上支付预收流水,其支付订单数量必须为1,orderId="+orderInfoDO.id)

    def checkPayType(self, payId):
        if payId in self.ONLINE_PAY_TYPE_LIST:
            return self.ONLINE_PAY_TYPE

        if payId in self.COD_CASH_PAY_TYPE_LIST:
            return self.COD_CASH_PAY_TYPE

        if payId in self.COD_POS_PAY_TYPE_LIST:
            return self.COD_POS_PAY_TYPE

        if payId in self.FINANCE_PAY_TYPE_LIST:
            return self.FINANCE_PAY_TYPE



    def receiptTypeJuge4Online(self, receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        returnOrderInfoDO = receiptInitParam.returnOrderInfoDO
        saleReturnExchangeDOList = receiptInitParam.saleReturnExchangeDOList
        returnGoodsBillDOList = receiptInitParam.returnGoodsBillDOList


        if orderInfoDO.payStatus == 2:
            if orderInfoDO.tradeStatus == "HDSX":
                return self.MERGE_ORDER_ORI_INVALID_PROCESS

            if orderInfoDO.tradeStatus == "FDSX":
                return self.SPLIT_ORDER_ORI_INVALID_PROCESS

            if orderInfoDO.tradeStatus == "QXDD":
                if returnOrderInfoDO is not None and returnOrderInfoDO.haveRefund == 1:
                    return self.ONLINE_CANCEL_RETURN_PROCESS
                return self.ONLINE_CANCEL_PROCESS

            if orderInfoDO.deliveryNo is not None and orderInfoDO.deliveryNo.strip()!="":
                if orderInfoDO.returnAmount is not None and orderInfoDO.returnAmount > 0:
                    return self.ONLINE_REJECT_PROCESS
                return self.ONLINE_OUT_STOCK_PROCESS

            return self.ONLINE_RECEIVED_PROCESS

        return self.DO_NOTHING



    def receiptTypeJuge4CodCash(self, receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        returnOrderInfoDO = receiptInitParam.returnOrderInfoDO
        saleReturnExchangeDOList = receiptInitParam.saleReturnExchangeDOList
        returnGoodsBillDOList = receiptInitParam.returnGoodsBillDOList

        #if orderInfoDO.deliveryNo is not None and orderInfoDO.deliveryNo.strip()!="":
        if orderInfoDO.tradeStatus == "DDJS":
            return self.COD_CASH_ALL_REJECT_PROCESS
        if orderInfoDO.returnAmount is not None and orderInfoDO.returnAmount >0 and orderInfoDO.returnAmount != orderInfoDO.orderAmount:
            if orderInfoDO.tradeStatus == "CWQRSK" or self.isDDTHOrder(receiptInitParam):
                return self.COD_CASH_PART_REJECT_PAID_CONFIRM_PROCESS
            return self.COD_CASH_PART_REJECT_PROCESS

        # if orderInfoDO.receiveAmount is not None and orderInfoDO.receiveAmount == orderInfoDO.orderAmount:
        if orderInfoDO.tradeStatus == "CWQRSK" or self.isDDTHOrder(receiptInitParam):
            return self.COD_CASH_PAID_CONFIRM_PROCESS

        if orderInfoDO.deliveryNo is not None and orderInfoDO.deliveryNo.strip()!="":
            # if (orderInfoDO.returnAmount is None or orderInfoDO.returnAmount==0) and (orderInfoDO.receiveAmount is None or orderInfoDO.receiveAmount == 0):
                return self.COD_OUT_STOCK_PROCESS
        #异常订单要记一下
        # raise Exception("异常订单,orderId = "+orderInfoDO.id)

        return self.DO_NOTHING



    def receiptTypeJuge4CodPOS(self, receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        returnOrderInfoDO = receiptInitParam.returnOrderInfoDO
        saleReturnExchangeDOList = receiptInitParam.saleReturnExchangeDOList
        returnGoodsBillDOList = receiptInitParam.returnGoodsBillDOList

        if self.isOutStockOrder(orderInfoDO) :


            if orderInfoDO.returnAmount is not None and orderInfoDO.returnAmount>0:
                # if orderInfoDO.payFee is not None and orderInfoDO.payFee > 0:
                if orderInfoDO.payStatus==2:
                    if orderInfoDO.tradeStatus == "CWQRSK" or self.isDDTHOrder(receiptInitParam):
                        return self.COD_POS_PART_REJECT_PAID_CONFIRM_PROCESS
                    return self.COD_POS_PART_REJECT_PART_PAID_PROCESS

                return self.COD_POS_PART_REJECT_PROCESS

            if orderInfoDO.payFee is not None and orderInfoDO.payFee!=0 and orderInfoDO.payFee != orderInfoDO.orderAmount:
                if orderInfoDO.tradeStatus == "CWQRSK" or self.isDDTHOrder(receiptInitParam):
                    return self.COD_POS_PART_PAID_CONFRIM_PROCESS

                return self.COD_POS_PART_PAID_PROCESS

            # if orderInfoDO.payFee is not None and orderInfoDO.payFee>0 and orderInfoDO.payFee == orderInfoDO.orderAmount:
            if orderInfoDO.tradeStatus == "CWQRSK" or self.isDDTHOrder(receiptInitParam):
                return self.COD_POS_PAID_PROCESS

            # if (orderInfoDO.payFee is None or orderInfoDO.payFee == 0) and (orderInfoDO.returnAmount is None or orderInfoDO.returnAmount == 0):

            return self.COD_POS_OUT_STOCK_PROCESS

            #异常订单要记一下
            # raise Exception("异常订单,orderId = "+str(orderInfoDO.id))

        return self.DO_NOTHING

    def isOutStockOrder(self, orderInfoDO):
        return (orderInfoDO.deliveryNo is not None and orderInfoDO.deliveryNo.strip()!="") or orderInfoDO.outWareTime is not None

    def receiptTypeJuge4ExchangeOrder(self, receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        returnOrderInfoDO = receiptInitParam.returnOrderInfoDO
        saleReturnExchangeDOList = receiptInitParam.saleReturnExchangeDOList
        returnGoodsBillDOList = receiptInitParam.returnGoodsBillDOList
        if orderInfoDO.deliveryNo is not None and orderInfoDO.deliveryNo.strip()!="":
            if orderInfoDO.tradeStatus == "CWQRSK" or self.isDDTHOrder(receiptInitParam):
                return self.EXCHANGE_PAID_CONFIRM_PROCESS
            return self.EXCHANGE_OUTSTOCK_PROCESS

        return self.DO_NOTHING


    def receiptTypeJuge4Finance(self, receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        returnOrderInfoDO = receiptInitParam.returnOrderInfoDO
        saleReturnExchangeDOList = receiptInitParam.saleReturnExchangeDOList
        returnGoodsBillDOList = receiptInitParam.returnGoodsBillDOList


        if (orderInfoDO.deliveryNo is None or orderInfoDO.deliveryNo.strip=="") and (orderInfoDO.tradeStatus == "CWQRSK" or self.isDDTHOrder(receiptInitParam)):
            if orderInfoDO.tradeStatus == "FDSX":
                return self.FINANCE_SPLIT_ORI_INVALID_PROCESS
            if orderInfoDO.parentId is not None and orderInfoDO.parentId>0:
                return self.FINANCE_SPLIT_CHILED_ORDER_PROCESS
            return self.FINANCE_CONFIRMED_NO_OUTSTOCK_PROCESS

        if (orderInfoDO.deliveryNo is not None and orderInfoDO.deliveryNo.strip!="") and (orderInfoDO.tradeStatus != "CWQRSK" and not self.isDDTHOrder(receiptInitParam)):
            return self.FINANCE_CONFIRMED_RECEIVED_OUT_STOCK_PROCESS

        if (orderInfoDO.deliveryNo is not None and orderInfoDO.deliveryNo.strip!="") and (orderInfoDO.tradeStatus == "CWQRSK" or self.isDDTHOrder(receiptInitParam)):

            if self.__isSplitChildOrder(orderInfoDO):
                return self.FINANCE_SPLIT_CHILD_ORDER_OUTSTOCK_PROCESS
            return self.FINANCE_CONFIRMED_RECEIVED_OUTSTOCK_PROCESS

        return self.DO_NOTHING


    def initOrderReceiptInfo4Entry(self, receiptInitParam):
        if receiptInitParam.payOrderDOList == None or len(receiptInitParam.payOrderDOList)<=0:
            raise Exception("payOrderDOList为空")
        stdPayOrderDO = receiptInitParam.payOrderDOList[0]
        for payOrderDO in receiptInitParam.payOrderDOList:
            if payOrderDO.outOrderSn != stdPayOrderDO.outOrderSn:
                raise Exception("outOrderSn必须一致")

        orderInfoDO = receiptInitParam.orderInfoDO
        orderReceipt =  OrderReceiptDO()
        # orderInfoDO = OrderInfoDO()
        # payOrderItem = PayOrderItemDO()
        orderReceipt.gmtCreate = orderInfoDO.gmtCreate
        orderReceipt.creator = orderInfoDO.creator
        orderReceipt.gmtModified = orderInfoDO.gmtCreate
        orderReceipt.modifier = orderInfoDO.modifier
        orderReceipt.financeAccountId = stdPayOrderDO.financeAccountId
        orderReceipt.platformId = stdPayOrderDO.platformId
        orderReceipt.platformName = stdPayOrderDO.platformName
        orderReceipt.outOrderSn = orderInfoDO.orderSn
        orderReceipt.payId = orderInfoDO.payId
        orderReceipt.orderAmount = orderInfoDO.orderAmount

        orderReceipt.rejectAmount=0
        orderReceipt.refundAmount=0
        orderReceipt.needReceiveAmount=0
        orderReceipt.hasReceivedAmount=0
        orderReceipt.hasReceivedCashAmount=0
        orderReceipt.hasReceivedBankAmount=0
        orderReceipt.remainingAmount=0
        orderReceipt.shippingAmount=0
        orderReceipt.taxAmount=0
        orderReceipt.loansAmount=0
        orderReceipt.othersAmount=0

        return orderReceipt

    def __isSplitChildOrder(self,orderInfoDO):
        return orderInfoDO.parentId is not None and orderInfoDO.parentId>0

    def doFilterOrder(self, orderInfoDOList):
        newOrderInfoDOList = []
        for orderInfoDO in orderInfoDOList:
            if not self.isFDSXOrderNotPaid(orderInfoDO)\
                and not self.isHDSXORderNotPaid(orderInfoDO)\
                    and not self.isXEQRCod(orderInfoDO):
                newOrderInfoDOList.append(orderInfoDO)

        return newOrderInfoDOList


    def isFDSXOrderNotPaid(self, orderInfoDO):
        return orderInfoDO.payStatus<2 and orderInfoDO.tradeStatus=="FDSX"

    def isHDSXORderNotPaid(self, orderInfoDO):
        return orderInfoDO.payStatus<2 and orderInfoDO.tradeStatus=="HDSX"

    def isXEQRCod(self, orderInfoDO):
        return orderInfoDO.payId==3 and orderInfoDO.tradeStatus=="XEQR"

    def doFilterOrder4Test(self, orderInfoDOList):
        newOrderInfoDOList = []
        for orderInfoDO in orderInfoDOList:
            if not self.isDDJSOrder4Test(orderInfoDO) \
                    and not self.isDDTHOrder4Test(orderInfoDO):
                newOrderInfoDOList.append(orderInfoDO)

        return newOrderInfoDOList

    def isDDJSOrder4Test(self, orderInfoDO):
        return orderInfoDO.tradeStatus == "DDJS"

    def isDDTHOrder4Test(self, orderInfoDO):
        return orderInfoDO.tradeStatus == "DDTH"

    def doReceipt4ReturnProcess(self, receiptRecord4ReceivedList, orderReceipt, receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        # returnOrderInfoDO = receiptInitParam.returnOrderInfoDO
        saleReturnExchangeDOList = receiptInitParam.saleReturnExchangeDOList
        returnGoodsBillDOList = receiptInitParam.returnGoodsBillDOList
        saleReturnExchangeEntryDOList = receiptInitParam.saleReturnExchangeBillEntryDOList
        returnGoodsBillEntryDOList = receiptInitParam.returnGoodsBillEntryDOList
        refundBillDOList = receiptInitParam.refundBillDOList

        if refundBillDOList is not None and len(refundBillDOList)!=0:
            receiptRecord4ReceivedList += self.doCommonReceipt4RefundGoodsRefund(orderReceipt,receiptInitParam)
            return

        if (saleReturnExchangeDOList is not None and len(saleReturnExchangeDOList)!=0) \
            and (returnGoodsBillEntryDOList is not None and len(returnGoodsBillEntryDOList)!=0):
            receiptRecord4ReceivedList +=self.doCommonReceipt4RefundGoods(orderReceipt,receiptInitParam)

    def doCommonReceipt4RefundGoods(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList.append(self.doCommon4ReturnGoods(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    def doCommonReceipt4RefundGoodsRefund(self,orderReceipt,receiptInitParam):
        receiptRecord4ReceivedList = []
        receiptRecord4ReceivedList += self.doCommonReceipt4RefundGoods(orderReceipt,receiptInitParam)
        receiptRecord4ReceivedList.append(self.doCommon4ReturnGoodsRefund(orderReceipt,receiptInitParam))
        return receiptRecord4ReceivedList

    # 退货
    def doCommon4ReturnGoods(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        saleReturnExchangeDOList = receiptInitParam.saleReturnExchangeDOList
        returnGoodsBillDOList = receiptInitParam.returnGoodsBillDOList
        saleReturnExchangeEntryDOList = receiptInitParam.saleReturnExchangeBillEntryDOList
        returnGoodsBillEntryDOList = receiptInitParam.returnGoodsBillEntryDOList
        refundBillDOList = receiptInitParam.refundBillDOList
        returnGoodsAmount = self.calReturnGoodsAmount(receiptInitParam)
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        if (orderInfoDO.payId in self.FINANCE_PAY_TYPE_LIST):
            receiptRecord.receiptAction = 'finance_return_goods'
        else:
            receiptRecord.receiptAction = 'return_goods'
        receiptRecord.needReceiveAmount = 0-returnGoodsAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    #  退货退款
    def doCommon4ReturnGoodsRefund(self,orderReceipt,receiptInitParam):
        orderInfoDO = receiptInitParam.orderInfoDO
        receiptRecord = self.initOrderReceiptRecordDO(orderReceipt,receiptInitParam)
        returnGoodsRefundAmount = self.calReturnGoodsRefundAmount(receiptInitParam)
        if (orderInfoDO.payId in self.FINANCE_PAY_TYPE_LIST):
            receiptRecord.receiptAction = 'finance_return_goods_refund'
        else:
            receiptRecord.receiptAction = 'return_goods_refund'
        receiptRecord.hasReceivedAmount = 0-returnGoodsRefundAmount
        receiptRecord.refundAmount = returnGoodsRefundAmount
        self.doProcessReceipt(orderReceipt,receiptRecord)
        return receiptRecord

    def calReturnGoodsAmount(self, receiptInitParam):
        saleReturnExchangeDOList = receiptInitParam.saleReturnExchangeDOList
        returnGoodsBillDOList = receiptInitParam.returnGoodsBillDOList
        saleReturnExchangeEntryDOList = receiptInitParam.saleReturnExchangeBillEntryDOList
        returnGoodsBillEntryDOList = receiptInitParam.returnGoodsBillEntryDOList
        refundBillDOList = receiptInitParam.refundBillDOList

        returnGoodsAmount = 0
        for saleReturnExchangeEntryDO in saleReturnExchangeEntryDOList:
            # saleReturnExchangeEntryDO = SaleReturnExchangeBillEntryDO()

            returnGoodsAmount += saleReturnExchangeEntryDO.returnQty*saleReturnExchangeEntryDO.returnPrice


        return returnGoodsAmount

    def calReturnGoodsRefundAmount(self,receiptInitParam):
        saleReturnExchangeDOList = receiptInitParam.saleReturnExchangeDOList
        returnGoodsBillDOList = receiptInitParam.returnGoodsBillDOList
        saleReturnExchangeEntryDOList = receiptInitParam.saleReturnExchangeBillEntryDOList
        returnGoodsBillEntryDOList = receiptInitParam.returnGoodsBillEntryDOList
        refundBillDOList = receiptInitParam.refundBillDOList

        returnGoodsRefundAmount = 0

        for refundBillDO in refundBillDOList:
            returnGoodsRefundAmount += refundBillDO.realReturnAmount

        return returnGoodsRefundAmount


    def isDDTHOrder(self,receiptInitParam):
        saleReturnExchangeDOList = receiptInitParam.saleReturnExchangeDOList
        returnGoodsBillDOList = receiptInitParam.returnGoodsBillDOList
        saleReturnExchangeEntryDOList = receiptInitParam.saleReturnExchangeBillEntryDOList
        returnGoodsBillEntryDOList = receiptInitParam.returnGoodsBillEntryDOList
        refundBillDOList = receiptInitParam.refundBillDOList

        return saleReturnExchangeDOList is not None and len(saleReturnExchangeDOList)!=0




