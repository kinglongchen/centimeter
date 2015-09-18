# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.OfferListActionReasonDO import OfferListActionReasonDO

"""
OfferListActionReasonMapper数据库操作接口类
"""

class OfferListActionReasonMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(OfferListActionReasonDO).filter(OfferListActionReasonDO.id==id).one()

	def selectByOfferListIdList(self, offerListIdList):
		return self.session.query(OfferListActionReasonDO).\
			filter(OfferListActionReasonDO.offerListId.in_(offerListIdList)).\
			filter(OfferListActionReasonDO.isDeleted=="N").all()
