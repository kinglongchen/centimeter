# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.OrderReceiptRecordDO import OrderReceiptRecordDO

"""
OrderReceiptRecordMapper数据库操作接口类
"""

class OrderReceiptRecordMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(OrderReceiptRecordDO).filter(OrderReceiptRecordDO.id==id).one()

	def insertSelective(self,OrderReceiptRecordDO):
		rs = self.session.add(OrderReceiptRecordDO)
		self.session.commit()
		return rs
