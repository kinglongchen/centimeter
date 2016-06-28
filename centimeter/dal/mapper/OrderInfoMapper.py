# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.OrderInfoDO import OrderInfoDO

"""
OrderInfoMapper数据库操作接口类
"""

class OrderInfoMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(OrderInfoDO).filter(OrderInfoDO.id==id).one()

	def selectByOutOrderSnList(self, outOrderSnList):
		return self.session.query(OrderInfoDO).filter(OrderInfoDO.isDeleted=='N')\
			.filter(OrderInfoDO.orderSn.in_(outOrderSnList)).all()

	def selectBatch(self, start, number):
		return self.session.query(OrderInfoDO).order_by(OrderInfoDO.id)[start:start+number]

