import xlrd
from common.util import PathUtil

__author__ = 'chenjinlong'

filePath = PathUtil.getResourcePath()+"/fwb.xlsx"

workbook = xlrd.open_workbook(filePath)
sheet = workbook.sheet_by_index(0)
nrows = sheet.nrows

insertSqlPre = "insert into "

for i in range(nrows):
    if i == 0:
        continue
    id = "%s" %sheet.cell(i,0).value
    name = sheet.cell(i,1).value

    print id
    print name


