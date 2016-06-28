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

    TEST_ORDER_LIMIT = 5000

    IS_SWITCH = True

    def __init__(self):
        self.fileInput = open("../output/receipt/retryfile.txt","w")

    def isOffSwitch(self,limtNum):
        return self.IS_SWITCH and limtNum>=self.TEST_ORDER_LIMIT

    def doFinanceReceiptDataInit(self):
        total = 0
        start = 0
        # orderInfoDOList = self.finance4ReceiptHelper.getProcessOrder(start,self.BATCH_NUMBER)
        orderInfoDOList = self.finance4ReceiptHelper.getProcessOrderTest(["B16022534021020"])

        receiptTypeMap = {}
        while orderInfoDOList:
            print "正在处理从%d到%d的数据" %(start,start+self.BATCH_NUMBER)
            try:
                # self.finance4ReceiptHelper.batchDoProcessFinanceReceipt(orderInfoDOList)
                errorOrderInfoList = self.finance4ReceiptHelper.batchDoProcessFinanceReceiptTest(orderInfoDOList,receiptTypeMap)
                if errorOrderInfoList:
                    print "异常订单数:%d" %(len(errorOrderInfoList))
                    self.doRetryProcess(errorOrderInfoList)
            except Exception,e:
                if ReceiptConfig.isDebug:
                    traceback.print_exc()
                print "处理第%d到%d数据出错(%s),忽略该组,准备尝试下一组。。。" %(start,start+self.BATCH_NUMBER,e.__str__())
                self.doRetryProcess(orderInfoDOList)

            total += len(orderInfoDOList)

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
        self.saveFailProcessInfo(self.retryOrderInfoSnList)
        print "历史脚本初始化完毕，处理总数total=%d" %total
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








