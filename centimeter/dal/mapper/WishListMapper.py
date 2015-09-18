from common.config.Config import Config

__author__ = 'chenjinlong'
from dal.domain.do.WishListDO import WishListDO
class WishListMapper(object):
    def getById(self,id):
        wishListDOList = self.session.query(WishListDO).filter(WishListDO.id==id).one()
        return wishListDOList

    def getByIdList(self, wishListIdList):
        return self.session.query(WishListDO).\
            filter(WishListDO.id.in_(wishListIdList)).\
            filter(WishListDO.isDeleted=="N").all()

    def selectWishListByDateSpanExcludeUserIdList(self, dateFrom, dateTo, userIdList):
        return self.session.query(WishListDO).filter(WishListDO.gmtCreate>=dateFrom) \
            .filter(WishListDO.gmtCreate<dateTo) \
            .filter(WishListDO.status.in_(Config.wishListFilter)) \
            .filter(WishListDO.isDeleted=='N').filter(~WishListDO.userId.in_(userIdList)).all()
