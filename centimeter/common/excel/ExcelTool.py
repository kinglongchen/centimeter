# coding=utf-8
from common.config.Config import Config
import os
from common.util import code

__author__ = 'chenjinlong'
import xlwt
from datetime import date, timedelta


class ExcelTool(object):
    def __init__(self, fileName):
        self.workbook = xlwt.Workbook(encoding='utf-8')

        self.fileName = self.fileNameProcesse(fileName) + ".xls"

    '''
    headers格式：[[标题1,headerKey1],[标题2,headerKey2],...]
    '''

    def export(self, headers, dataList, sheetName="Sheet1", ):
        headerName = []
        headerKey = []
        xmlDataList = []
        for header in headers:
            headerName.append(header[0])
            headerKey.append(header[1])
        xmlDataList.append(headerName)
        for data in dataList:
            xmlData = [data[key] for key in headerKey]
            xmlDataList.append(xmlData)

        booksheet = self.workbook.add_sheet(sheetName, cell_overwrite_ok=True)

        for i, row in enumerate(xmlDataList):
            for j, col in enumerate(row):
                booksheet.write(i, j, col)
        booksheet.col(0).width = 0x0fff
        self.workbook.save(self.fileName)

    def getFileName(self):
        if os.path.exists(self.fileName) and os.path.isfile(self.fileName):
            return self.fileName
        else:
            return None

    def fileNameProcesse(self, fileName):
        # now = date.today() - timedelta(days=1)
        now = Config.getDate().date() - timedelta(days=1)
        excelFilePath = code.encode2utf8(Config.excelFilePath)
        excelFilePath = excelFilePath + "/" if excelFilePath and not excelFilePath.endswith("/") else excelFilePath
        excelFilePath +=now.strftime("%Y年%m月报表")+"/"
        if not os.path.exists(excelFilePath) or not os.path.isdir(excelFilePath):
            os.makedirs(excelFilePath)
        return "%s%s%s" % (excelFilePath,fileName, now.strftime("%m%d"))





