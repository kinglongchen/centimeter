# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.WishListActionReasonDO import WishListActionReasonDO

"""
WishListActionReasonMapper数据库操作接口类
"""

class WishListActionReasonMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(WishListActionReasonDO).filter(WishListActionReasonDO.id==id).one()

	def selectByWishListIdList(self, wishListIdList):
		return self.session.query(WishListActionReasonDO).\
			filter(WishListActionReasonDO.wishListId.in_(wishListIdList))\
			.filter(WishListActionReasonDO.isDeleted == "N").all()
