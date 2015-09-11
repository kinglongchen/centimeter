from dal.mapper.WishListActionReasonMapper import WishListActionReasonMapper

__author__ = 'chenjinlong'
class WishListActionReasonDao(object):
    wishListActionReasonMapper = WishListActionReasonMapper()

    def getByWishListIdList(self, wishListIdList):
        if len(wishListIdList) == 0:
            return []
        wishListActionReasonDO = self.wishListActionReasonMapper.selectByWishListIdList(wishListIdList)
        return wishListActionReasonDO