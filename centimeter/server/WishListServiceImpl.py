__author__ = 'chenjinlong'
from client.WishListService import WishListService
from facade.impl.WishListFacadeImpl import WishListFacadeImpl
class WishListServiceImpl(WishListService):
    wishListFacade = WishListFacadeImpl()
    def getReport(self,excelTool):
        self.wishListFacade.getReport(excelTool)

    def getDetailReport(self,excelTool):
        self.wishListFacade.getDetailReport(excelTool)

    def getById(self,id):
        wishListDO = self.wishListFacade.getById(id)
        return wishListDO
