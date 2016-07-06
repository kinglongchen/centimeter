# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.SaleReturnExchangeBillDO import SaleReturnExchangeBillDO

"""
SaleReturnExchangeBillMapper数据库操作接口类
"""

class SaleReturnExchangeBillMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(SaleReturnExchangeBillDO).filter(SaleReturnExchangeBillDO.id==id).one()

	def selectReturnGoods4PartReject(self, outOrderSnList):
		return self.session.query(SaleReturnExchangeBillDO).filter(SaleReturnExchangeBillDO.billStatus==27)\
			.filter(SaleReturnExchangeBillDO.isDeleted=="N").filter(SaleReturnExchangeBillDO.billApplyType == 1)\
			.filter(SaleReturnExchangeBillDO.mainBillNo.in_(outOrderSnList)).all()



	# .filter(SaleReturnExchangeBillDO.returnWarehouseId.in_([41,10035,10037,44,10003,10015,10033,10020,10008,10028,10031,1002,10161,7,26,39,6,22,23,25,69,10040,4,10013,95,98,10064,27,13,10194,1003,10193,1004]))\
