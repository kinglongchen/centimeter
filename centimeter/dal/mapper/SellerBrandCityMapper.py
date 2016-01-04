# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.SellerBrandCityDO import SellerBrandCityDO

"""
SellerBrandCityMapper数据库操作接口类
"""

class SellerBrandCityMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(SellerBrandCityDO).filter(SellerBrandCityDO.id==id).one()

	def getBySellerId(self,sellerId):
		return self.session.query(SellerBrandCityDO).filter(SellerBrandCityDO.isDeleted=='N').\
			filter(SellerBrandCityDO.sellerId==sellerId).all()
