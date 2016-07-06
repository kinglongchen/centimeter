# coding=utf-8
import traceback
from common.config import ReceiptConfig

from helper.Finance4ReceiptHelper import Finance4ReceiptHelper

__author__ = 'chenjinlong'
class Finance4ReceiptService():


    BATCH_NUMBER = 5000

    retryOrderInfoSnList = []

    finance4ReceiptHelper = Finance4ReceiptHelper()

    RETRY_ID_CAPACITY = 100

    TEST_ORDER_LIMIT = 200000

    IS_SWITCH = False

    def __init__(self):
        self.fileInput = open("../output/receipt/retryfile.txt","w")

    def isOffSwitch(self,limtNum):
        return self.IS_SWITCH and limtNum>=self.TEST_ORDER_LIMIT

    def doFinanceReceiptDataInit(self):
        total = 0
        start = 0
        # orderInfoDOList = self.finance4ReceiptHelper.getProcessOrder(start,self.BATCH_NUMBER)
        orderInfoDOList = self.finance4ReceiptHelper.getProcessOrderTest(["B16063098001004"])

        receiptTypeMap = {}
        while orderInfoDOList != None:
            print "正在处理从%d到%d的数据" %(start,start+self.BATCH_NUMBER)
            try:
                errorOrderInfoList = self.finance4ReceiptHelper.batchDoProcessFinanceReceipt(orderInfoDOList)
                # errorOrderInfoList = self.finance4ReceiptHelper.batchDoProcessFinanceReceiptTest(orderInfoDOList,receiptTypeMap)
                if errorOrderInfoList:
                    print "异常订单数:%d" %(len(errorOrderInfoList))
                    self.doRetryProcess(errorOrderInfoList)
            except Exception,e:
                if ReceiptConfig.isDebug:
                    traceback.print_exc()
                print "处理第%d到%d数据出错(%s),忽略该组,准备尝试下一组。。。" %(start,start+self.BATCH_NUMBER,e.__str__())
                self.doRetryProcess(orderInfoDOList)

            total += len(orderInfoDOList)
            print "已处理订单数:total = %s " %total

            if self.isOffSwitch(total):
                break

            # 查询下一组数据
            start += self.BATCH_NUMBER
            try:
                orderInfoDOList = self.finance4ReceiptHelper.getProcessOrder(start,self.BATCH_NUMBER)
            except Exception:
                print "获取第%d到%d数据失败,程序停止!" %(start,start+self.BATCH_NUMBER)
                break
        # 最后要保存一下出错的信息
        self.finance4ReceiptHelper.flushErrorInfo()
        self.saveFailProcessInfo(self.retryOrderInfoSnList)
        print "历史脚本初始化完毕，处理总数total=%d" %total
        print receiptTypeMap


    def doFinanceReceiptData4ErrorOrder(self):
        fileInput = open("../output/temp/retryfile.txt","r")
        line = fileInput.readline()
        receiptTypeMap = {}
        lineNum = 1
        total = 0
        while line:
            orderSnStrList =  line[:-2].split(",")
            newOrderSnList = []

            for orderSnStr in orderSnStrList:
                newOrderSnList.append(orderSnStr[1:-1])
            orderInfoDOList = self.finance4ReceiptHelper.getProcessOrder4ErrorOrder(newOrderSnList)

            try:
                # self.finance4ReceiptHelper.batchDoProcessFinanceReceipt(orderInfoDOList)
                errorOrderInfoList = self.finance4ReceiptHelper.batchDoProcessFinanceReceiptTest(orderInfoDOList,receiptTypeMap)
                if errorOrderInfoList:
                    print "异常订单数:%d" %(len(errorOrderInfoList))
                    self.doRetryProcess(errorOrderInfoList)
            except Exception,e:
                if ReceiptConfig.isDebug:
                    traceback.print_exc()
                print "处理第%s数据出错(%s),忽略该组,准备尝试下一组。。。" %(lineNum,e.__str__())
                self.doRetryProcess(orderInfoDOList)
            lineNum +=1
            total += len(orderInfoDOList)

            line = fileInput.readline()

        # 最后要保存一下出错的信息
        self.saveFailProcessInfo(self.retryOrderInfoSnList)
        print "出错的初始化完毕，处理总数total=%d" %total
        print receiptTypeMap


    def doRetryProcess(self, orderInfoList):
        # 将初始化失败的payOrder记录一下
        self.retryOrderInfoSnList+=[orderInfo.orderSn for orderInfo in orderInfoList]
        if len(self.retryOrderInfoSnList) >= self.RETRY_ID_CAPACITY:
            self.saveFailProcessInfo(self.retryOrderInfoSnList)
            self.retryOrderInfoSnList=[]

    def saveFailProcessInfo(self, retryOrderInfoSnList):
        if (len(retryOrderInfoSnList)) <= 0:
            return
        saveInfo = ""
        for orderSn in retryOrderInfoSnList:
            saveInfo += '"'+str(orderSn)+'",'

        self.fileInput.write(saveInfo+"\n")

    def getFailInfoFileName(self):
        filePath = "../output/receipt/retryfile.txt"
        return filePath








