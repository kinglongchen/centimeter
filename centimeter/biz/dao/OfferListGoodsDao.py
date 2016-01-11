from dal.mapper.OfferListGoodsMapper import OfferListGoodsMapper

__author__ = 'chenjinlong'
class OfferListGoodsDao(object):
    offerListGoodsMapper = OfferListGoodsMapper()

    def getByOfferListIdList(self, offerListIdList):
        if len(offerListIdList) == 0:
            return []
        offerListGoodsDOList = self.offerListGoodsMapper.selectSelectedByOfferListIdList(offerListIdList)
        return offerListGoodsDOList

    def getInfoDictOfferListIdKeyByOfferListIdList(self,offerListIdList):
        offerListGoodsList = self.getByOfferListIdList(offerListIdList)
        olgInfoOfferListIdKeyDict = {}
        for offerListGoods in offerListGoodsList:
            olgInfo = olgInfoOfferListIdKeyDict.get(offerListGoods.offerListId, None)
            olgInfo = "" if olgInfo == None else olgInfo + ";"
            curGoodsInfo = "%s %s %s" % (offerListGoods.goodsName,offerListGoods.goodsPrice, offerListGoods.goodsNumber)
            olgInfo = "%s%s" % (olgInfo, curGoodsInfo)
            olgInfoOfferListIdKeyDict[offerListGoods.offerListId] = olgInfo
        return olgInfoOfferListIdKeyDict

    def countOfferNumber(self, offerListIdList):
        offerListGoodsList = self.offerListGoodsMapper.listOfferCount(offerListIdList);
        olgOfferCountDict = {}
        for offerListGoods in offerListGoodsList:
            olgOfferCount = olgOfferCountDict.get(offerListGoods.offerListId,0)
            olgOfferCount += 1
            olgOfferCountDict[offerListGoods.offerListId] = olgOfferCount

        return olgOfferCountDict