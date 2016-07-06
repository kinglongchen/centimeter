# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.SaleReturnExchangeBillEntryDO import SaleReturnExchangeBillEntryDO

"""
SaleReturnExchangeBillEntryMapper数据库操作接口类
"""

class SaleReturnExchangeBillEntryMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(SaleReturnExchangeBillEntryDO).filter(SaleReturnExchangeBillEntryDO.id==id).one()

	def selectByBillIdList(self, saleReturnExchangeBillIdList):
		return self.session.query(SaleReturnExchangeBillEntryDO) \
			.filter(SaleReturnExchangeBillEntryDO.isDeleted=="N").filter(SaleReturnExchangeBillEntryDO.billId.in_(saleReturnExchangeBillIdList)).all()
