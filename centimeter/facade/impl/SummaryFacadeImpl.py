# coding=utf-8
from biz.dao.OfferListDao import OfferListDao
from biz.dao.UserDao import UserDao
from biz.dao.WishListDao import WishListDao
from common.config.Config import Config
from facade.SummaryFacade import SummaryFacade

__author__ = 'chenjinlong'


class SummaryFacadeImpl(SummaryFacade):
    wishListDao = WishListDao()
    userDao = UserDao()
    offerListDao = OfferListDao()

    def getDetailReport(self, excelTool):
        headers = [["需求单客户总数","countUserId"],
                   ["需求单提交总数","wishListCount"],
                   ["订单转化数","orderCount"],
                   ["订单转化率","orderConversionRate"],
                   ["订单总金额","orderAmountSum"],
                   ["历史订单转化数","historyOrderCount"],
                   ["历史订单总金额","historyOrderAmountSum"],
                   ["待报价需求单","dbjWishListCount"],
                   ["已报价需求单","ybjWishListCount"],
                   ["已取消需求单","yxqWishListCount"],
                   ["确认报价需求单","qrbjWishListCount"],
                   ["待付款订单","dfkOrderCount"],
                   ["已付款订单","yfkOrderCount"],
                   ["部分发货订单","bffhOrderCount"],
                   ["已发货订单","yfhOrderCount"],
                   ["已签收订单","yqsOrderCount"],
                   ["已结算订单","yjsOrderCount"]]
        userIdList = self.userDao.getExcludeUserIdList()

        dateFrom, dateTo = Config.getDateSpan()
        wishListBOList = self.wishListDao.getWishListByDateSpanExcludeUserIdList(dateFrom, dateTo, userIdList)
        orderList = self.offerListDao.getOrderByDateSpanExcludeUserIdList(dateFrom, dateTo, userIdList)

        historyDateFrom, historyDateTo = Config.getHistoryDateSpan()
        historyOrderList = self.offerListDao. \
            getOrderByDateSpanExcludeUserIdList(historyDateFrom, historyDateTo, userIdList)
        userSet = set()

        wishListCount = len(wishListBOList)
        orderCount = len(orderList)
        orderConversionRate = (float(orderCount) / float(wishListCount)) if wishListCount else None
        orderAmountSum = float(0)
        historyOrderCount = len(historyOrderList)
        historyOrderAmountSum = float(0)

        dbjWishListCount = 0
        ybjWishListCount = 0
        yxqWishListCount = 0
        qrbjWishListCount = 0
        dfkOrderCount = 0
        yfkOrderCount = 0
        bffhOrderCount = 0
        yfhOrderCount = 0
        yqsOrderCount = 0
        yjsOrderCount = 0
        for wishListBO in wishListBOList:
            userSet.add(wishListBO.userId)
            if wishListBO.status == "XDBJ":
                dbjWishListCount += 1
            if wishListBO.status == "XYBJ":
                ybjWishListCount += 1
            if wishListBO.status == "XYQX" or wishListBO.status == "BYQX":
                yxqWishListCount += 1
            if wishListBO.status == "XQRBJ":
                qrbjWishListCount += 1
        for order in orderList:
            if order.status == "BDFK":
                dfkOrderCount += 1
            if order.status == "BYFK":
                yfkOrderCount += 1
            if order.status == "BBFFH":
                bffhOrderCount += 1
            if order.status == "BYFH":
                yfhOrderCount += 1
            if order.status == "BYQS":
                yqsOrderCount += 1
            if order.status == "BYJS":
                yjsOrderCount +=1

            orderAmountSum+=int(0 if not order.paidOfferAmount else order.paidOfferAmount)
        for historyOrder in historyOrderList:
            historyOrderAmountSum += int(0 if not historyOrder.paidOfferAmount else historyOrder.paidOfferAmount)

        detailReportDictList = []
        detailReportDict = {}
        detailReportDict["countUserId"] = len(userSet)
        detailReportDict["wishListCount"] = wishListCount
        detailReportDict["orderCount"] = orderCount
        detailReportDict["orderConversionRate"] = ("{:.2%}".format(orderConversionRate)) if orderConversionRate else ""
        detailReportDict["orderAmountSum"] = "{:.2f}".format(orderAmountSum)
        detailReportDict["historyOrderCount"] = historyOrderCount
        detailReportDict["historyOrderAmountSum"] = "{:.2f}".format(historyOrderAmountSum)
        detailReportDict["dbjWishListCount"] = dbjWishListCount
        detailReportDict["ybjWishListCount"] = ybjWishListCount
        detailReportDict["yxqWishListCount"] = yxqWishListCount
        detailReportDict["qrbjWishListCount"] = qrbjWishListCount
        detailReportDict["dfkOrderCount"] = dfkOrderCount
        detailReportDict["yfkOrderCount"] = yfkOrderCount
        detailReportDict["bffhOrderCount"] = bffhOrderCount
        detailReportDict["yfhOrderCount"] = yfhOrderCount
        detailReportDict["yqsOrderCount"] = yqsOrderCount
        detailReportDict["yjsOrderCount"] = yjsOrderCount
        detailReportDictList.append(detailReportDict)
        excelTool.export(headers,detailReportDictList,"汇总明细报表")

    def getStatReport(self, excelTool):
        headers = [["需求单客户总数","countUserId"],
                   ["需求单提交总数","wishListCount"],
                   ["订单总金额","orderAmountSum"],
                   ["已报价需求单","ybjWishListCount"],
                   ["确认报价需求单","qrbjWishListCount"],
                   ["已付款订单","yfkOrderCount"],
                   ["已发货订单","yfhOrderCount"],
                   ["历史订单转化数","historyOrderCount"],
                   ["历史订单总金额","historyOrderAmountSum"],
                   ["客单价","wishListAvrgPrice"]]

        userIdList = self.userDao.getExcludeUserIdList()

        dateFrom, dateTo = Config.getDateSpan()
        wishListBOList = self.wishListDao.getWishListByDateSpanExcludeUserIdList(dateFrom, dateTo, userIdList)
        orderList = self.offerListDao.getOrderByDateSpanExcludeUserIdList(dateFrom, dateTo, userIdList)

        historyDateFrom, historyDateTo = Config.getHistoryDateSpan()
        historyOrderList = self.offerListDao. \
            getOrderByDateSpanExcludeUserIdList(historyDateFrom, historyDateTo, userIdList)
        userSet = set()

        wishListCount = len(wishListBOList)
        orderAmountSum = float(0)
        historyOrderCount = len(historyOrderList)
        historyOrderAmountSum = float(0)

        ybjWishListCount = 0
        qrbjWishListCount = 0
        yfkOrderCount = 0
        yfhOrderCount = 0
        for wishListBO in wishListBOList:
            userSet.add(wishListBO.userId)
            if wishListBO.status == "XYBJ":
                ybjWishListCount += 1
            if wishListBO.status == "XQRBJ":
                qrbjWishListCount += 1
        for order in orderList:
            if order.status == "BYFK":
                yfkOrderCount += 1
            if order.status == "BYFH":
                yfhOrderCount += 1

            orderAmountSum+=int(0 if not order.paidOfferAmount else order.paidOfferAmount)
        for historyOrder in historyOrderList:
            historyOrderAmountSum += int(0 if not historyOrder.paidOfferAmount else historyOrder.paidOfferAmount)

        detailReportDictList = []
        detailReportDict = {}
        detailReportDict["countUserId"] = len(userSet)
        detailReportDict["wishListCount"] = wishListCount
        detailReportDict["orderAmountSum"] = "{:.2f}".format(orderAmountSum)
        detailReportDict["historyOrderCount"] = historyOrderCount
        detailReportDict["historyOrderAmountSum"] = "{:.2f}".format(historyOrderAmountSum)
        detailReportDict["ybjWishListCount"] = ybjWishListCount
        detailReportDict["qrbjWishListCount"] = qrbjWishListCount
        detailReportDict["yfkOrderCount"] = yfkOrderCount
        detailReportDict["yfhOrderCount"] = yfhOrderCount
        detailReportDict['wishListAvrgPrice'] = "{:.2f}".format(historyOrderAmountSum/historyOrderCount)
        detailReportDictList.append(detailReportDict)
        excelTool.export(headers,detailReportDictList,"统计汇总表")