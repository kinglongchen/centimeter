# coding=utf-8
from biz.dao.OfferListGoodsDao import OfferListGoodsDao
from biz.dao.WishListGoodsDao import WishListGoodsDao
from common.config.Config import Config

__author__ = 'chenjinlong'
from datetime import datetime, timedelta, time

from facade.OfferListFacade import OfferListFacade
from biz.dao.OfferListDao import OfferListDao
from biz.dao.UserDao import UserDao
from biz.dao.WishListDao import WishListDao
from biz.dao.OfferListActionReasonDao import OfferListActionReasonDao


class OfferListFacadeImpl(OfferListFacade):
    offerListDao = OfferListDao()
    userDao = UserDao()
    wishListDao = WishListDao()
    offerListActionReasonDao = OfferListActionReasonDao()
    wishListGoodsDao = WishListGoodsDao()
    offerListGoodsDao = OfferListGoodsDao()

    def getReport(self, excelTool):
        headers = [["订单号", "offerListSn"],
                   ["订单状态", "status"],
                   ["报价次数","offerCount"],
                   ["维修店名称", "companyName"],
                   ["填单人", "wishListMaker"],
                   ["填单人手机", "wishListMakerTel"],
                   ["对应供应商", "sellerName"],
                   ["备注（取消原因）", "reason"]]

        userIdList = self.userDao.getExcludeUserIdList()

        dateFrom, dateTo = Config.getDateSpan()

        offerListBOList = self.offerListDao.getOrderByDateSpanExcludeUserIdList(dateFrom, dateTo, userIdList)
        if len(offerListBOList) == 0:
            return
        offerListIdList = []
        wishListIdList = []
        for offerListBO in offerListBOList:
            wishListIdList.append(offerListBO.wishListId)
            offerListIdList.append(offerListBO.id)
        # 根据offerListIdList获取wishListBOList信息
        wishListBOList = self.wishListDao.getByIdList(wishListIdList)
        wishListIdKeyDict = {}
        for wishList in wishListBOList:
            wishListIdKeyDict[wishList.id] = wishList

        # 获取取消原因
        offerListActionReasonBOList = self.offerListActionReasonDao.getByOfferListIdList(offerListIdList)

        offerListActionReasonOfferListIdKeyDict = {}
        for offerListActionReasonBO in offerListActionReasonBOList:
            offerListActionReasonOfferListIdKeyDict[offerListActionReasonBO.offerListId] = offerListActionReasonBO

        #获取需求单报价次数
        olgOfferCountDict = self.offerListGoodsDao.countOfferNumber(offerListIdList);

        orderReportDictList = []

        for offerList in offerListBOList:
            orderReportDict = {}
            orderReportDict['offerListSn'] = offerList.offerListSn.strip()
            orderReportDict['offerCount'] = olgOfferCountDict.get(offerList.id,"")
            orderReportDict['sellerName'] = offerList.sellerName.strip()
            orderReportDict['status'] = Config.statusDict.get(offerList.status, "")
            wishList = wishListIdKeyDict.get(offerList.wishListId, None)
            if wishList != None:
                orderReportDict['companyName'] = wishList.companyName.strip()
                orderReportDict['wishListMaker'] = wishList.wishListMaker.strip()
                orderReportDict['wishListMakerTel'] = wishList.wishListMakerTel.strip()

            offerListActionReasonBO = offerListActionReasonOfferListIdKeyDict.get(offerList.id, None)
            if offerListActionReasonBO != None:
                orderReportDict['reason'] = offerListActionReasonBO.reason.strip()
            else:
                orderReportDict['reason'] = ""
            orderReportDictList.append(orderReportDict)

        excelTool.export(headers, orderReportDictList, "订单报表")

    def getById(self, id):
        offerListDO = self.offerListDao.getById(id)
        return offerListDO

    def getDetailReport(self, excelTool):
        headers = [["订单号", "offerListSn"],
                   ["订单状态", "status"],
                   ["报价次数","offerCount"],
                   ["需求单配件信息", "wishListGoodsInfo"],
                   ["订单配件信息", "offerListGoodsInfo"],
                   ["订单金额", "paidOfferAmount"],
                   ["维修店名称", "companyName"],
                   ["填单人", "wishListMaker"],
                   ["填单人手机", "wishListMakerTel"],
                   ["对应供应商", "sellerName"],
                   ["备注（取消原因）", "reason"]]

        userIdList = self.userDao.getExcludeUserIdList()

        dateFrom, dateTo = Config.getDateSpan()

        offerListBOList = self.offerListDao.getOrderByDateSpanExcludeUserIdList(dateFrom, dateTo, userIdList)
        if len(offerListBOList) == 0:
            return
        offerListIdList = []
        wishListIdList = []
        for offerListBO in offerListBOList:
            wishListIdList.append(offerListBO.wishListId)
            offerListIdList.append(offerListBO.id)
        # 根据offerListIdList获取wishListBOList信息
        wishListBOList = self.wishListDao.getByIdList(wishListIdList)
        wishListIdKeyDict = {}
        for wishList in wishListBOList:
            wishListIdKeyDict[wishList.id] = wishList

        # 获取取消原因
        offerListActionReasonBOList = self.offerListActionReasonDao.getByOfferListIdList(offerListIdList)

        offerListActionReasonOfferListIdKeyDict = {}
        for offerListActionReasonBO in offerListActionReasonBOList:
            offerListActionReasonOfferListIdKeyDict[offerListActionReasonBO.offerListId] = offerListActionReasonBO

        # 获取需求商品信息
        wlgInfoWishListIdKeyDict = self.wishListGoodsDao.getInfoWishListIdKeyByWishListIdList(wishListIdList)

        # 获取订单商品信息
        olgInfoOfferListIdKeyDict = self.offerListGoodsDao.getInfoDictOfferListIdKeyByOfferListIdList(offerListIdList)

        #获取需求单报价次数
        olgOfferCountDict = self.offerListGoodsDao.countOfferNumber(offerListIdList);

        orderDetailReportDictList = []

        for offerList in offerListBOList:
            orderDetailReportDict = {}
            wishListId = offerList.wishListId
            offerListId = offerList.id
            orderDetailReportDict['offerListSn'] = offerList.offerListSn.strip()
            orderDetailReportDict['offerCount'] = olgOfferCountDict.get(offerListId,"")
            orderDetailReportDict['sellerName'] = offerList.sellerName.strip()
            orderDetailReportDict['status'] = Config.statusDict.get(offerList.status, "")
            orderDetailReportDict["wishListGoodsInfo"] = wlgInfoWishListIdKeyDict.get(wishListId, "")
            orderDetailReportDict["offerListGoodsInfo"] = olgInfoOfferListIdKeyDict.get(offerListId, "")
            paidOfferAmount = offerList.paidOfferAmount
            orderDetailReportDict["paidOfferAmount"] = "" if not paidOfferAmount else paidOfferAmount
            orderDetailReportDict['companyName'] = ""
            orderDetailReportDict['wishListMaker'] = ""
            orderDetailReportDict['wishListMakerTel'] = ""
            orderDetailReportDict['reason'] = ""

            wishList = wishListIdKeyDict.get(wishListId, None)

            if wishList != None:
                orderDetailReportDict['companyName'] = wishList.companyName.strip()
                orderDetailReportDict['wishListMaker'] = wishList.wishListMaker.strip()
                orderDetailReportDict['wishListMakerTel'] = wishList.wishListMakerTel.strip()

            offerListActionReasonBO = offerListActionReasonOfferListIdKeyDict.get(offerList.id, None)
            if offerListActionReasonBO != None:
                orderDetailReportDict['reason'] = offerListActionReasonBO.reason.strip()
            orderDetailReportDictList.append(orderDetailReportDict)

        excelTool.export(headers, orderDetailReportDictList, "订单明细报表")

    def getFeatureReport(self, excelTool):
        headers = [["订单号", "offerListSn"],
                   ["feature", "feature"],
                   ["签收时间", "receiveTime"]]

        dateFrom, dateTo = Config.getDateSpan()
        exFileterSeller = Config.excludeFilterSeller

        offerListBOList = self.offerListDao.getByReciveTimeSpan(dateFrom, dateTo, exFileterSeller)
        if len(offerListBOList) == 0:
            return
        featureReportDictList = []
        for offerListBO in offerListBOList:
            featureReportDict = {}
            featureReportDict["offerListSn"] = offerListBO.offerListSn
            featureReportDict["feature"] = offerListBO.feature
            featureReportDict["receiveTime"] = offerListBO.receiveTime.strftime('%Y-%m-%d %H:%M:%S')
            featureReportDictList.append(featureReportDict)

        excelTool.export(headers, featureReportDictList, "金蝶号数据报表")
