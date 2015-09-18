__author__ = 'chenjinlong'
from abc import ABCMeta, abstractmethod
class OfferListService():
    __metaclass__ = ABCMeta

    @abstractmethod
    def getReport(self,excelTool):
        pass

    @abstractmethod
    def getById(self,id):
        pass

    @abstractmethod
    def getDetailReport(self, excelTool):
        pass

    @abstractmethod
    def getFeatureReport(self,excelTool):
        pass
