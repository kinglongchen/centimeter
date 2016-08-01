# coding=utf-8
from flask import json
import xlrd
from common.util import PathUtil

__author__ = 'chenjinlong'

class ReceiptTool4Gift():
    filePath = ""

    def __init__(self):
        self.filePath = PathUtil.getResourcePath()+"/未扣减赠品订单.xlsx"

    def getGiftInfoMap(self):
        workbook = xlrd.open_workbook(self.filePath)
        sheet = workbook.sheet_by_index(0)
        nrows = sheet.nrows

        giftInfoMap = {}

        for i in range(nrows):
            if i == 0:
                continue
            orderSn = "%s" %sheet.cell(i,0).value
            newGiftAmount = sheet.cell(i,3).value

            giftAmount = giftInfoMap.get(orderSn,0)

            giftAmount+=newGiftAmount

            giftInfoMap[orderSn]= giftAmount

        return giftInfoMap



if __name__ == "__main__":
    receiptTool4Gift = ReceiptTool4Gift()
    giftInfoMap = receiptTool4Gift.getGiftInfoMap()
    giftInfoJsonStr = json.dumps(giftInfoMap)
    print "订单数量:%d" %len(giftInfoMap)
    print giftInfoJsonStr


