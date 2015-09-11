__author__ = 'chenjinlong'
from client.OfferListService import OfferListService
from facade.impl.OfferListFacadeImpl import OfferListFacadeImpl
class OfferListServiceImpl(OfferListService):
    offerListFacade = OfferListFacadeImpl()
    def getReport(self,excelTool):
        self.offerListFacade.getReport(excelTool)

    def getById(self,id):
        offerListDO = self.offerListFacade.getById(id)
        return offerListDO

    def getDetailReport(self, excelTool):
        self.offerListFacade.getDetailReport(excelTool)
