# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.RefundBillDO import RefundBillDO

"""
RefundBillMapper数据库操作接口类
"""

class RefundBillMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(RefundBillDO).filter(RefundBillDO.id==id).one()

	def selectByReturnGoodsBillNoList(self, billNoList):
		return self.session.query(RefundBillDO).filter(RefundBillDO.isDeleted == "N").filter(RefundBillDO.billStatus!=5).\
			filter(RefundBillDO.returnGoodsBillNo.in_(billNoList)).all()
