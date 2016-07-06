__author__ = 'chenjinlong'
from dal.domain.do.OrderInfoDO import OrderInfoDO
class ReceiptErrorLogTool():
    SAVE_CAP_LIMIT = 100
    FILE_NAME_PRE = "receipt_error_log_4_"
    def __init__(self):
        self.errorInfoMap = {}
        self.fileDirPath = "../output/receipt/log/"

    def write(self,orderInfoDO):
        if orderInfoDO is None:
            return
        tradeStatus = "OTHER" if orderInfoDO.tradeStatus is None or orderInfoDO.tradeStatus == "" else orderInfoDO.tradeStatus
        dataEntry = self.errorInfoMap.get(tradeStatus,[])
        dataEntry.append(orderInfoDO.orderSn)
        if len(dataEntry)>=self.SAVE_CAP_LIMIT:
            self.__saveDate(tradeStatus,dataEntry)
            dataEntry = []
        self.errorInfoMap[tradeStatus] = dataEntry

    def flush(self):
        for tradeStatus in self.errorInfoMap:
            self.__saveDate(tradeStatus,self.errorInfoMap[tradeStatus])
            self.errorInfoMap[tradeStatus] = []

    def __saveDate(self, tradeStatus, dataEntry):
        if dataEntry is None or len(dataEntry) == 0:
            return

        fileInput = open(self.fileDirPath+self.FILE_NAME_PRE+tradeStatus+".txt","a")
        dataInfo = ""
        for data in dataEntry:
            dataInfo += '"'+str(data)+'",'

        dataInfo = dataInfo[0:-1]+"\n"
        fileInput.write(dataInfo)
        fileInput.close()


