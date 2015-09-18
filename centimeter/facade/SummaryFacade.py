__author__ = 'chenjinlong'
from abc import ABCMeta,abstractmethod
class SummaryFacade():
    __metaclass__ = ABCMeta
    @abstractmethod
    def getDetailReport(self, excelTool):
        pass

