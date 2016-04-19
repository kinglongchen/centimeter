# -*- coding: utf-8 -*-

__author__ = 'chenjinlong'

from dal.domain.do.OfferListGoodsDO import OfferListGoodsDO

"""
OfferListGoodsMapper数据库操作接口类
"""

class OfferListGoodsMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(OfferListGoodsDO).filter(OfferListGoodsDO.id==id).one()

	def selectSelectedByOfferListIdList(self, offerListIdList):
		return self.session.query(OfferListGoodsDO). \
			filter(OfferListGoodsDO.offerListId.in_(offerListIdList)). \
			filter(OfferListGoodsDO.isDeleted=="N").filter(OfferListGoodsDO.isUserSelectPay==1).all()

	def listOfferCount(self, offerListIdList):
		return self.session.query(OfferListGoodsDO).filter(OfferListGoodsDO.gmtCreate!=None).\
			filter(OfferListGoodsDO.offerListId.in_(offerListIdList)).\
			group_by(OfferListGoodsDO.offerListId,OfferListGoodsDO.gmtCreate).all()
