__author__ = 'chenjinlong'
class Receipt4FileInput():
    SAVE_CAP_LIMIT = 100
    FILE_NAME_PRE = "select_receipt_order"
    def __init__(self):
        self.cashList = []
        self.fileDirPath = "../output/receipt/result/"
    def writeList(self,orderReceiptDOList):
        if orderReceiptDOList is None or len(orderReceiptDOList) == 0:
            return

        for orderReceiptDO in orderReceiptDOList:
            self.write(orderReceiptDO)

    def write(self,orderReceiptDO):
        if orderReceiptDO is None:
            return

        self.cashList.append(orderReceiptDO.outOrderSn)
        if len(self.cashList)>=self.SAVE_CAP_LIMIT:
            self.__saveDateOrderSnList()

    def flush(self):
        self.__saveDateOrderSnList()

    def __saveDateOrderSnList(self):
        if len(self.cashList) == 0:
            return

        fileInput = open(self.fileDirPath+self.FILE_NAME_PRE+".txt","a")
        dataInfo = ""
        for data in self.cashList:
            dataInfo += '"'+str(data)+'",'

        # dataInfo = dataInfo[0:-1]+"\n"
        fileInput.write(dataInfo)
        fileInput.close()
        self.cashList=[]
