# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.ReturnOrderInfoDO import ReturnOrderInfoDO

"""
ReturnOrderInfoMapper数据库操作接口类
"""

class ReturnOrderInfoMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(ReturnOrderInfoDO).filter(ReturnOrderInfoDO.id==id).one()

	def selectByOrderSnList(self, outOrderSnList):
		return self.session.query(ReturnOrderInfoDO).filter(ReturnOrderInfoDO.isDeleted=='N') \
			.filter(ReturnOrderInfoDO.billNo.in_(outOrderSnList)).all()
