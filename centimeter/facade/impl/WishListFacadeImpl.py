# coding=utf-8
from biz.dao.OfferListDao import OfferListDao
from biz.dao.UserDao import UserDao
from biz.dao.WishListActionReasonDao import WishListActionReasonDao
from biz.dao.WishListGoodsDao import WishListGoodsDao
from common.config.Config import Config
from datetime import timedelta

__author__ = 'chenjinlong'
from facade.WishListFacade import WishListFacade
from biz.dao.WishListDao import WishListDao


class WishListFacadeImpl(WishListFacade):
    wishListDao = WishListDao()
    userDao = UserDao()
    offerListDao = OfferListDao()
    wishListActionReasonDao = WishListActionReasonDao()
    wishListGoodsDao = WishListGoodsDao()

    def getReport(self, excelTool):
        headers = [["需求单号", "wishListSn"],
                   ["需求单状态", "status"],
                   ["需求单提交的时间", "gmtCreate"],
                   ["首次报价的时间", "olGmtCreate"],
                   ["维修店名称", "companyName"],
                   ["填单人", "wishListMaker"],
                   ["填单人手机", "wishListMakerTel"],
                   ["对应供应商", "sellerName"],
                   ["供应商对接人手机", "telephone"],
                   ["备注（取消原因）", "reason"]]

        userIdList = self.userDao.getExcludeUserIdList()

        dateFrom, dateTo = Config.getDateSpan()

        wishListBOList = self.wishListDao.getWishListByDateSpanExcludeUserIdList(dateFrom, dateTo, userIdList)
        if len(wishListBOList) == 0:
            return
        wishListIdList = [wl.id for wl in wishListBOList]
        offerListBOList = self.offerListDao.getByWishListIdList(wishListIdList)
        offerListWishListIdKeyDict = {}
        for offerList in offerListBOList:
            offerListWishListIdKeyDict[offerList.wishListId] = offerList
        wishListActionReasonBOList = self.wishListActionReasonDao.getByWishListIdList(wishListIdList)
        wishListActionReasonBOWishListIdKeyDict = {}
        for wishListActionReasonBO in wishListActionReasonBOList:
            wishListActionReasonBOWishListIdKeyDict[wishListActionReasonBO.wishListId] = wishListActionReasonBO
        wishListReportDictList = []
        for wishListBO in wishListBOList:
            wishListReportDict = {}
            wishListId = wishListBO.id
            wishListReportDict["wishListSn"] = wishListBO.wishListSn
            wishListReportDict["status"] = Config.statusDict[wishListBO.status]
            wishListReportDict["gmtCreate"] = wishListBO.gmtCreate.strftime('%Y-%m-%d %H:%M:%S')
            wishListReportDict["companyName"] = wishListBO.companyName
            wishListReportDict["wishListMaker"] = wishListBO.wishListMaker
            wishListReportDict["wishListMakerTel"] = wishListBO.wishListMakerTel
            wishListReportDict["olGmtCreate"] = ""
            wishListReportDict["sellerName"] = ""
            wishListReportDict["telephone"] = ""
            wishListReportDict["reason"] = ""
            offerListBO = offerListWishListIdKeyDict.get(wishListId, None)
            if offerListBO != None:
                wishListReportDict["olGmtCreate"] = offerListBO.gmtCreate.strftime('%Y-%m-%d %H:%M:%S')
                wishListReportDict["sellerName"] = offerListBO.sellerName
                wishListReportDict["telephone"] = offerListBO.telephone
            wishListActionReasonBO = wishListActionReasonBOWishListIdKeyDict.get(wishListId, None)
            if wishListActionReasonBO != None:
                wishListReportDict["reason"] = wishListActionReasonBO.reason
            wishListReportDictList.append(wishListReportDict)
        excelTool.export(headers, wishListReportDictList, "需求单报表")

    def getDetailReport(self, excelTool):

        headers = [["需求单号", "wishListSn"],
                   ["需求单配件信息","goodsInfo"],
                   ["需求单状态", "status"],
                   ["需求单提交的时间", "gmtCreate"],
                   ["首次报价的时间", "olGmtCreate"],
                   ["首次报价间隔(分钟)","firstQuoteDiff"],
                   ["维修店名称", "companyName"],
                   ["填单人", "wishListMaker"],
                   ["填单人手机", "wishListMakerTel"],
                   ["对应供应商", "sellerName"],
                   ["供应商对接人手机", "telephone"],
                   ["备注（取消原因）", "reason"]]

        userIdList = self.userDao.getExcludeUserIdList()

        dateFrom, dateTo = Config.getDateSpan()

        wishListBOList = self.wishListDao.getWishListByDateSpanExcludeUserIdList(dateFrom, dateTo, userIdList)

        if len(wishListBOList) == 0:
            return
        wishListIdList = [wl.id for wl in wishListBOList]
        offerListBOList = self.offerListDao.getByWishListIdList(wishListIdList)
        offerListWishListIdKeyDict = {}
        for offerList in offerListBOList:
            offerListWishListIdKeyDict[offerList.wishListId] = offerList
        wishListActionReasonBOList = self.wishListActionReasonDao.getByWishListIdList(wishListIdList)
        wishListActionReasonBOWishListIdKeyDict = {}
        for wishListActionReasonBO in wishListActionReasonBOList:
            wishListActionReasonBOWishListIdKeyDict[wishListActionReasonBO.wishListId] = wishListActionReasonBO
        wlgInfoWishListIdKeyDict = self.wishListGoodsDao.getInfoWishListIdKeyByWishListIdList(wishListIdList)

        detailReportDictList = []
        for wishListBO in wishListBOList:
            detailReportDict = {}
            wishListId = wishListBO.id
            detailReportDict["wishListSn"] = wishListBO.wishListSn
            detailReportDict["goodsInfo"] = wlgInfoWishListIdKeyDict.get(wishListId,"")
            detailReportDict["status"] = Config.statusDict[wishListBO.status]
            detailReportDict["gmtCreate"] = wishListBO.gmtCreate.strftime('%Y-%m-%d %H:%M:%S')
            detailReportDict["olGmtCreate"] = ""
            detailReportDict["firstQuoteDiff"] = ""
            detailReportDict["companyName"] = wishListBO.companyName
            detailReportDict["wishListMaker"] = wishListBO.wishListMaker
            detailReportDict["wishListMakerTel"] = wishListBO.wishListMakerTel
            detailReportDict["sellerName"] = ""
            detailReportDict["telephone"] = ""
            detailReportDict["reason"] = ""
            offerListBO = offerListWishListIdKeyDict.get(wishListId, None)
            if offerListBO != None:
                detailReportDict["olGmtCreate"] = offerListBO.gmtCreate.strftime('%Y-%m-%d %H:%M:%S')
                detailReportDict["sellerName"] = offerListBO.sellerName
                detailReportDict["telephone"] = offerListBO.telephone
                firstQuoteDiff = offerListBO.gmtCreate-wishListBO.gmtCreate
                detailReportDict["firstQuoteDiff"] = firstQuoteDiff.seconds/60
            wishListActionReasonBO = wishListActionReasonBOWishListIdKeyDict.get(wishListId, None)
            if wishListActionReasonBO != None:
                detailReportDict["reason"] = wishListActionReasonBO.reason
            detailReportDictList.append(detailReportDict)
        excelTool.export(headers, detailReportDictList, "需求单明细报表")

    def getById(self, id):
        wishListDO = self.wishListDao.getById(id)
        return wishListDO


if __name__ == "__main__":
    timespan = timedelta(minutes=29).seconds/60
    print(timespan)
