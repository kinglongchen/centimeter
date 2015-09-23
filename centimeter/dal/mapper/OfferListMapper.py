# -*- coding: utf-8 -*-
from common.config.Config import Config

__author__ = 'chenjinlong'

from dal.domain.do.OfferListDO import OfferListDO

"""
OfferListMapper数据库操作接口类
"""

class OfferListMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(OfferListDO).filter(OfferListDO.id==id).one()

	"""
	根据时间段查询订单
	"""
	def selectOrderByDateSpanExcludeUserIdList(self,dateFrom,dateTo,userIdList):
		return self.session.query(OfferListDO).filter(OfferListDO.gmtCreate>=dateFrom)\
			.filter(OfferListDO.gmtCreate<dateTo)\
			.filter(OfferListDO.status.in_(Config.isOrderFilter))\
			.filter(OfferListDO.isDeleted=='N').filter(~OfferListDO.userId.in_(userIdList))\
			.filter(~OfferListDO.companyName.like("%测试%")).all()

	def selectByWishListIdList(self, wishListIdList):
		return self.session.query(OfferListDO).filter(OfferListDO.wishListId.in_(wishListIdList)) \
			.filter(OfferListDO.isDeleted=='N').all()

	def selectByReciveTimeSpan(self, dateFrom, dateTo,exFilterSeller):
		return self.session.query(OfferListDO).filter(OfferListDO.receiveTime>=dateFrom).\
			filter(OfferListDO.receiveTime<dateTo).filter(OfferListDO.isDeleted=="N").\
			filter(~OfferListDO.sellerId.in_(exFilterSeller)).all()
