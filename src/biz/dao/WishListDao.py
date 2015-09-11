__author__ = 'chenjinlong'
from dal.mapper.WishListMapper import WishListMapper
class WishListDao(object):
    wishListMapper = WishListMapper()

    def getById(self,id):
        if not id:
            return None
        wishListDO = self.wishListMapper.getById(id)
        return wishListDO

    def getByIdList(self, wishListIdList):
        if len(wishListIdList)==0:
            return []
        wishListDOList = self.wishListMapper.getByIdList(wishListIdList)
        return wishListDOList

    def getWishListByDateSpanExcludeUserIdList(self, dateFrom, dateTo, userIdList):
        if dateFrom==None and dateTo == None:
            return []
        wishListDOList = self.wishListMapper.selectWishListByDateSpanExcludeUserIdList(dateFrom,dateTo,userIdList)
        return wishListDOList


