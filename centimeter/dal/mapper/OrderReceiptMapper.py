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

	def insertSelective(self,OrderReceiptDO,session):
		if session is None:
			session = self.session
		rs = session.add(OrderReceiptDO)
		session.commit()
		return rs

	def batchInsert(self, orderReceipt4InsertList,session):
		rs = session.add_all(orderReceipt4InsertList)

	def batchUpdateById(self, orderReceipt4InsertList, session):
		for orderReceiptDO in orderReceipt4InsertList:

			session.query(OrderReceiptDO).filter(OrderReceiptDO.id == orderReceiptDO.id).update(self.buildUpdateDict(orderReceiptDO))

	def buildUpdateDict(self,orderReceiptDO):
		updateDict = {}
		for k,v in orderReceiptDO.__class__.__dict__.items():
			if not str(k).startswith("__") and not str(k).startswith("_") and orderReceiptDO.__getattribute__(k) is not None:
				updateDict[str(k)] =  orderReceiptDO.__getattribute__(k)

		return updateDict

	def batchInsert2(self, orderReceiptDOList,session):
		if session is None:
			session = self.session
		session.execute(OrderReceiptDO.__table__.insert(),[value.toInsertDict() for value in orderReceiptDOList])

	def selectRemainingAmountNotZearo(self):
		return self.session.query(OrderReceiptDO).filter(OrderReceiptDO.remainingAmount>0.5).all()

