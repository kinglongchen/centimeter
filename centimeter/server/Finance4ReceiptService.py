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

    IS_SWITCH = False

    def __init__(self):
        self.fileInput = open("../output/receipt/retryfile.txt","w")

    def isOffSwitch(self,limtNum):
        return self.IS_SWITCH and limtNum>=self.TEST_ORDER_LIMIT

    def doFinanceReceiptDataInit(self):
        total = 0
        start = 0
        # orderInfoDOList = self.finance4ReceiptHelper.getProcessOrder(start,self.BATCH_NUMBER)
        # orderInfoDOList = self.finance4ReceiptHelper.getProcessOrderTest(["B15072915001064","B15072919001069","B15073001001004","B15073001001058","B15073001001130","B15073019001012","B15073101001096","B15073101401043","B15073101401049","B15073101401066","B15073111001058","B15073119001067","B15073119001069","B15073123001055","B15073141001012","B15073141001085","B15073141001091","B15080107001019","B15080111001013","B15080111001060","B15080119001016","B15080141001141","B15080241001084","B15080301001101","B15080305001010","B15080305001016","B15080305001043","B15080307001066","B15080315001008","B15080315001009","B15080315001010","B15080315001011","B15080315001012","B15080319001018","B15080319001032","B15080319001058","B15080319001065","B15080319001075","B15080401301086","B15080405001048","B15080405001053","B15080407001059","B15080407001064","B15080417001039","B15080419001091","B15080427001022","B15080441001068","B15080501301023","B15080501301024","B15080501301065","B15080501301078","B15080519001039","B15080519001096","B15080601301073","B15080619001050","B15080623001021","B15080641001078","B15080701301023","B15080703001025","B15080703001059","B15080707001069","B15080715001076","B15080717001035","B15080717001051","B15080717001062","B15080719001028","B15080719001055","B15080741001019","B15080741001066","B15080801001205","B15080801301237","B15080801301240","B15080801301265","B15080805001030","B15080805001057","B15080805001087","B15080807001014","B15080807001307","B15080807001312","B15080813001100","B15080813001118","B15080813001122","B15080819001055","B15080819001139","B15080819001147","B15080823001117","B15080823001219","B15080841001165","B15080841001266","B15080841001286","B15080901301044","B15081001301023","B15081001301051","B15081001301068","B15081003001078","B15081005001016","B15081019001013","B15081019001021","B15081023001082","B15081041001078","B15081101001091","B15081101301037","B15081107001002","B15081115001024","B15081115001096","B15081117001005","B15081119001039","B15081119001050","B15081119001060","B15081123001158","B15081129001011","B15081129001027","B15081141001115","B15081141001122","B15081205001021","B15081219001013","B15081219001050","B15081219001059","B15081219001080","B15081219001086","B15081227001008","B15081229001025","B15081313001066","B15081317001022","B15081317001093","B15081319001029","B15081341001082","B15081406001018","B15081417001040","B15081429001033","B15081501001145","B15081501001233","B15081501001316","B15081503001128","B15081506001047","B15081506001067","B15081507001066","B15081507001168","B15081519001072","B15081519001120","B15081541001244","B15081601201025","B15081641001002","B15081701001052","B15081701001137","B15081701201034","B15081705001002","B15081719001008","B15081719001012","B15081719001015","B15081719001020","B15081719001047","B15081741001033","B15081741001073","B15081741001112","B15081801001092","B15081801201005","B15081806001006","B15081819001056","B15081829001020","B15081901001143","B15081901001144","B15081901001185","B15081901301096","B15081913001035","B15081913001061","B15081913001064","B15081927001051","B15081941001048","B15081941001051","B15081941001106","B15082001201011","B15082013001110","B15082015001070","B15082019001012","B15082027001052","B15082029001006","B15082029001016","B15082041001002","B15082101001077","B15082101001147","B15082101001153","B15082101301082","B15082115001010","B15082127001068","B15082129001002","B15082141001062","B15082215001103","B15082223001151","B15082341001039","B15082501001078","B15082501101016","B15082513001011","B15082513001077","B15082515001036","B15082515001040","B15082515001059","B15082515001065","B15082517001061","B15082523001089","B15082601301053","B15082615001025","B15082706001015","B15082713001075","B15082715001077","B15082715001105","B15082741001083","B15082803001043","B15082806001002","B15082817001026","B15082823001032","B15082827001227","B15082901001040","B15082901301316","B15082913001063","B15082915001019","B15082915001072","B15082915001211","B15082915001224","B15082915001258","B15082915001262","B15082915001297","B15082915001310","B15082917001093","B15082941001016","B15082941001040","B15082941001104","B15082941001197","B15083103001026","B16011510051260"])
        orderInfoDOList = self.finance4ReceiptHelper.getProcessOrderTest(self.getProcessOrderSnFromFile())

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
                # errorOrderInfoList = self.finance4ReceiptHelper.batchDoProcessFinanceReceipt(orderInfoDOList)
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
        self.finance4ReceiptHelper.flushErrorInfo()

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

    def getProcessOrderSnFromFile(self):
        fileInput = open("../output/temp/processFile.txt","r")
        line = fileInput.readline()
        newOrderSnList = []

        while line:
            orderSnStrList =  line[:-2].split(",")
            for orderSnStr in orderSnStrList:
                newOrderSnList.append(orderSnStr[1:-1])
            line = fileInput.readline()


        return newOrderSnList


if __name__ == "__main__":
    finance4ReceiptService = Finance4ReceiptService()
    print finance4ReceiptService.getProcessOrderSnFromFile()



