# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.WishListGoodsDO import WishListGoodsDO

"""
WishListGoodsMapper数据库操作接口类
"""

class WishListGoodsMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(WishListGoodsDO).filter(WishListGoodsDO.id==id).one()

	def selectByWishListIdList(self, wishListIdList):
		return self.session.query(WishListGoodsDO).\
			filter(WishListGoodsDO.wishListId.in_(wishListIdList)).\
			filter(WishListGoodsDO.isDeleted=="N").all()
