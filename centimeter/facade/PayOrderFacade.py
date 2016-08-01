__author__ = 'chenjinlong'
from abc import ABCMeta,abstractmethod
class PayOrderFacade():
    __metaclass__ = ABCMeta

    @abstractmethod
    def updateAmount(self,updatePayOrderAmountInfo,updatePayOrderItemAmountInfo,session):
        pass