from dal.mapper.WishListGoodsMapper import WishListGoodsMapper

__author__ = 'chenjinlong'
class WishListGoodsDao(object):
    wishListGoodsMapper = WishListGoodsMapper()

    def getByWishListIdList(self, wishListIdList):
        if len(wishListIdList) == 0:
            return []
        wishListGoodsDOList = self.wishListGoodsMapper.selectByWishListIdList(wishListIdList)
        return wishListGoodsDOList

    def getInfoWishListIdKeyByWishListIdList(self,wishListIdList):
        wishListGoodsList = self.getByWishListIdList(wishListIdList)
        wlgInfoWishListIdKeyDict = {}
        for wishListGoods in wishListGoodsList:
            wlgInfo = wlgInfoWishListIdKeyDict.get(wishListGoods.wishListId, None)
            wlgInfo = "" if wlgInfo == None else wlgInfo + ";"
            curGoodsInfo = "%s %s" % (wishListGoods.goodsName, wishListGoods.goodsNumber)
            wlgInfo = "%s%s" % (wlgInfo, curGoodsInfo)
            wlgInfoWishListIdKeyDict[wishListGoods.wishListId] = wlgInfo
        return wlgInfoWishListIdKeyDict