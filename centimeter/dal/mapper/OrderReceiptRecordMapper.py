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

	def batchInsert(self, orderReceiptRecord4InsertList,session):
		rs = session.add_all(orderReceiptRecord4InsertList)
		return rs

	def batchInsert2(self, orderReceiptRecord4InsertList,session):
		if session is None :
			session = self.session
		session.execute(OrderReceiptRecordDO.__table__.insert(),[value.toInsertDict() for value in orderReceiptRecord4InsertList])
