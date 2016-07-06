# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.ReturnGoodsBillEntryDO import ReturnGoodsBillEntryDO

"""
ReturnGoodsBillEntryMapper数据库操作接口类
"""

class ReturnGoodsBillEntryMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(ReturnGoodsBillEntryDO).filter(ReturnGoodsBillEntryDO.id==id).one()

	def selectByBillIdList(self, returnGoodsBillIdList):
		return  self.session.query(ReturnGoodsBillEntryDO).filter(ReturnGoodsBillEntryDO.isDeleted=="N").\
			filter(ReturnGoodsBillEntryDO.billId.in_(returnGoodsBillIdList)).all()
