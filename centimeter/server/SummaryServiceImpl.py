from client.SummarysService import SummaryService
from facade.impl.SummaryFacadeImpl import SummaryFacadeImpl

__author__ = 'chenjinlong'


class SummaryServiceImpl(SummaryService):
    summaryFacade = SummaryFacadeImpl()

    def getDetailReport(self, excelTool):
        return self.summaryFacade.getDetailReport(excelTool)
