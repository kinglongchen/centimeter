__author__ = 'chenjinlong'
from dal.mapper.OfferListMapper import OfferListMapper


class OfferListDao(object):
    offerListMapper = OfferListMapper()

    def getById(self, id):
        if not id:
            return None
        offerListDO = self.offerListMapper.selectByPrimaryKey(id);
        return offerListDO

    def getOrderByDateSpanExcludeUserIdList(self, dateFrom, dateTo, userIdList):
        if dateFrom == None and dateTo == None:
            return []
        offerListDOList = self.offerListMapper.selectOrderByDateSpanExcludeUserIdList(dateFrom, dateTo, userIdList)
        return offerListDOList

    def getByWishListIdList(self, wishListIdList):
        if len(wishListIdList) == 0:
            return []
        offerListDOList = self.offerListMapper.selectByWishListIdList(wishListIdList)
        return offerListDOList

    def getByReciveTimeSpan(self, dateFrom, dateTo, exFilterSeller):
        if dateFrom == None and dateTo == None:
            return []
        if exFilterSeller == None:
            exFilterSeller = []
        offerListBOList = self.offerListMapper.selectByReciveTimeSpan(dateFrom, dateTo,exFilterSeller)
        return offerListBOList
