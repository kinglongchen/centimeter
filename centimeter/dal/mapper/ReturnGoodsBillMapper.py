# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.ReturnGoodsBillDO import ReturnGoodsBillDO

"""
ReturnGoodsBillMapper数据库操作接口类
"""

class ReturnGoodsBillMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(ReturnGoodsBillDO).filter(ReturnGoodsBillDO.id==id).one()

	def selectReturnGoodsInfo(self, outOrderSnList):
		return self.session.query(ReturnGoodsBillDO).filter(ReturnGoodsBillDO.billStatus==3)\
			.filter(ReturnGoodsBillDO.isDeleted=="N").filter(ReturnGoodsBillDO.mainBillNo.in_(outOrderSnList))
