# coding=utf-8
import xlrd

__author__ = 'chenjinlong'
workbook = xlrd.open_workbook(r'/Users/chenjinlong/tempfile/淘汽云配-批量导入商品表.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.row_values(3)
cols = sheet.col_values(2)
print cols
