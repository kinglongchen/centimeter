# coding=utf-8
import os
import xlrd

__author__ = 'chenjinlong'
rootdir = r'/Users/chenjinlong/百度云同步盘/工作/淘气档口/金融相关订单退换货/可换货商品列表'


def countXlRows(fileFullName):
    workbook = xlrd.open_workbook(fileFullName)
    sheet = workbook.sheet_by_index(0)
    nrows = sheet.nrows
    return nrows-1
sqlPreFix = "update db_goods set exchange_type=%s where new_goods_sn in (%s);"
allNewGoodsSnList = []
xbjGoodsNumber = 0

def buidlInitSQL(fileFullName,fileName):
    exchangeType=fileName.split("-")[-1].split(".")[0]
    workbook = xlrd.open_workbook(fileFullName)
    sheet = workbook.sheet_by_index(0)
    nrows = sheet.nrows
    newGoodsSnSet = set()
    for i in range(nrows):
        if i == 0:
            continue
        newGoodsSn = "%s" %sheet.cell(i,2).value
        newGoodsSn2 = newGoodsSn.split(".")[0]
        newGoodsSnSet.add("'%s'" %newGoodsSn2)
    if exchangeType=="6":
        global xbjGoodsNumber
        xbjGoodsNumber = len(newGoodsSnSet)

    for e in newGoodsSnSet:
        allNewGoodsSnList.append(e)
    print sqlPreFix %(exchangeType,','.join(newGoodsSnSet))

check_record_rows_count = 0
newrootdir = r'/Users/chenjinlong/Desktop/可退换货数据整理/'
for parent,dirnames,filenames in os.walk(newrootdir):
    for filename in filenames:
        if filename == '.DS_Store':
            continue
        check_record_rows_count+=countXlRows(parent+"/"+filename)
        buidlInitSQL(parent+"/"+filename,filename)

record_rows_count = 0
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        if filename == '.DS_Store':
            continue
        record_rows_count+=countXlRows(parent+"/"+filename)
print "原来的记录数为:%s" %record_rows_count


print "总记录数:%s" %len(allNewGoodsSnList)
allNewGoodsSet = set(allNewGoodsSnList)
print "唯一总数记录:%s" %len(allNewGoodsSet)
print "整理后的原来的记录数为:%s" %xbjGoodsNumber




# workbook = xlrd.open_workbook(r'/Users/chenjinlong/百度云同步盘/工作/淘气档口/金融相关订单退换货/可换货商品列表/电瓶养护机油.xlsx')
# sheet = workbook.sheet_by_index(0)
# nrows = sheet.nrows
# ncols = sheet.ncols
# newGoodsSnList = []
# for i in range(nrows):
#     if i == 0:
#         continue
#     newGoodsSn = "%s" %sheet.cell(i,2).value
#     newGoodsSn2 = newGoodsSn[0:-2]
#     newGoodsSnList.append("'%s'" %newGoodsSn2)
# print ','.join(newGoodsSnList)




# rows = sheet.row_values(3)
# cols = sheet.col_values(2)
# print cols
