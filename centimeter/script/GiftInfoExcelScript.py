# coding=utf-8
from flask import json
import xlrd
from common.util import PathUtil

__author__ = 'chenjinlong'
filePath = PathUtil.getResourcePath()+"/未扣减赠品订单.xlsx"

saveFilePath = PathUtil.getConfigPath()+"/giftInfo.json"

workbook = xlrd.open_workbook(filePath)
sheet = workbook.sheet_by_index(0)
nrows = sheet.nrows

giftInfoMap = {}

orderSnStr = ""

sumGiftAmount = 0

outOrderSnList = []
for i in range(nrows):
    if i == 0:
        continue
    orderSn = "%s" %sheet.cell(i,0).value
    newGiftAmount = sheet.cell(i,3).value

    outOrderSnList.append(orderSn)

    giftAmount = giftInfoMap.get(orderSn,0)

    giftAmount+=newGiftAmount

    sumGiftAmount += newGiftAmount

    giftInfoMap[orderSn]= giftAmount

    orderSnStr += '"%s",' %orderSn

print sumGiftAmount
# print orderSnStr[0:-1]

# giftInfoJsonStr = json.dumps(giftInfoMap)
# print giftInfoJsonStr