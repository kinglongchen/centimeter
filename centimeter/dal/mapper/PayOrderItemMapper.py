# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.PayOrderItemDO import PayOrderItemDO

"""
PayOrderItemMapper数据库操作接口类
"""

class PayOrderItemMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(PayOrderItemDO).filter(PayOrderItemDO.id==id).one()

	def selectByOutOrderSnList(self, payOrderIdList):
		return self.session.query(PayOrderItemDO).filter(PayOrderItemDO.isDeleted=='N') \
			.filter(PayOrderItemDO.payOrderId.in_(payOrderIdList)).all()

	def selectByPayOrderIdList(self, payOrderIdList):
		if payOrderIdList is None or len(payOrderIdList) == 0:
			return []

		return self.session.query(PayOrderItemDO).filter(PayOrderItemDO.isDeleted == 'N') \
			.filter(PayOrderItemDO.payOrderId.in_(payOrderIdList)).all()

	def updatePayOrderItemAmount(self, updatePayOrderItemAmountInfo, session):
		if session is None:
			session = self.session

		for key,value in updatePayOrderItemAmountInfo:
			session.query(PayOrderItemDO).filter(PayOrderItemDO.payOrderId == key).update({
				PayOrderItemDO.itemAmount : value
			})
