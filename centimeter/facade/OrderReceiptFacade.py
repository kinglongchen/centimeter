__author__ = 'chenjinlong'
from abc import ABCMeta,abstractmethod
class OrderReceiptFacade():
    __metaclass__ = ABCMeta

    @abstractmethod
    def doOrderReceiptDataInit(self,orderReceipt4InsertList,orderReceiptRecord4InsertList,session):
        pass

