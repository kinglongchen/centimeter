# coding=utf-8
import xlrd
from common.util import PathUtil
from server.domain.ExchangeOrderInfo import ExchangeOrderInfo

__author__ = 'chenjinlong'
class ReceiptTool4Exchange():
    filePath = ""

    def __init__(self):
        self.filePath = PathUtil.getResourcePath()+"/换货拒收订单0801_标记退货单号.xlsx"

    def getExchangeMapInfo(self):
        workbook = xlrd.open_workbook(self.filePath)
        sheet = workbook.sheet_by_index(3)
        #sheet = workbook.sheet_by_name('备注订单（有换货单）')
        nrows = sheet.nrows

        exchangeMapInfo = {}

        for i in range(nrows):
            if i == 0:
                continue
            newOrderSn = "%s" %sheet.cell(i,0).value
            newOrderAmount = sheet.cell(i,1).value
            needPaidAmount = sheet.cell(i,2).value

            returnOrderAmount = sheet.cell(i,3).value

            returnOrderSn ="%s" %sheet.cell(i,5).value

            exchangeOrderInfo = ExchangeOrderInfo()

            exchangeOrderInfo.newOrderSn = newOrderSn
            exchangeOrderInfo.newOrderAmount = newOrderAmount
            exchangeOrderInfo.needPaidAmount = needPaidAmount
            exchangeOrderInfo.returnOrderAmount = returnOrderAmount
            exchangeOrderInfo.returnOrderSn = returnOrderSn

            exchangeMapInfo[newOrderSn] = exchangeOrderInfo

        return exchangeMapInfo

    def getReturnSnSet(self):
        exchangeMapInfo = self.getExchangeMapInfo()
        returnSnSet = set()

        for key in exchangeMapInfo:
            exchangeOrderInfo = exchangeMapInfo.get(key)
            returnSnSet.add(exchangeOrderInfo.returnOrderSn)

        return returnSnSet

def getExchangeMapInfoTest():
    receiptTool4Exchange = ReceiptTool4Exchange()
    exchangeMapInfo = receiptTool4Exchange.getExchangeMapInfo()
    ddjsOrderSnList = []
    count = 0
    for key in exchangeMapInfo:
        exchangeInfo = exchangeMapInfo.get(key,None)
        needPaidAmount = exchangeInfo.needPaidAmount if exchangeInfo is not None else None
        if not (needPaidAmount is None or needPaidAmount!=0):
            count += 1
            ddjsOrderSnList.append(exchangeInfo.newOrderSn)
    print "数量:%s" %count
    print ddjsOrderSnList

def getReturnSnSetTest():
    receiptTool4Exchange = ReceiptTool4Exchange()
    returnSnSet = receiptTool4Exchange.getReturnSnSet()

    if "RT1606249100001" in returnSnSet:
        print "测试成功"

    if "testSn" not in returnSnSet:
        print "测试成功"

if __name__ == "__main__":
    getReturnSnSetTest()

