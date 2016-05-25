# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.OrderReceiptDO import OrderReceiptDO

"""
OrderReceiptMapper数据库操作接口类
"""

class OrderReceiptMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(OrderReceiptDO).filter(OrderReceiptDO.id==id).one()

	def insertSelective(self,OrderReceiptDO):
		rs = self.session.add(OrderReceiptDO)
		self.session.commit()
		return rs