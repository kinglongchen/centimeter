# -*- coding: utf-8 -*-
from sqlalchemy import not_, and_

__author__ = 'chenjinlong'

from dal.domain.do.OrderInfoDO import OrderInfoDO

"""
OrderInfoMapper数据库操作接口类
"""

class OrderInfoMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(OrderInfoDO).filter(OrderInfoDO.id==id).one()

	def selectByOutOrderSnList(self, outOrderSnList):
		return self.session.query(OrderInfoDO).filter(OrderInfoDO.isDeleted=='N')\
			.filter(OrderInfoDO.orderSn.in_(outOrderSnList)).filter(OrderInfoDO.tradeStatus.notin_(["DDJS"]))\
			.filter(OrderInfoDO.orderSn.notin_(["B15082915001224","B15082915001258","B15082915001262","B15082915001310"])).all()

	def selectBatch(self, start, number):
		# filter(not_(and_(OrderInfoDO.tradeStatus=="HDSX",OrderInfoDO.payStatus<2))). \
		return self.session.query(OrderInfoDO).filter(OrderInfoDO.isDeleted=="N").\
				   filter(OrderInfoDO.tradeStatus.notin_(["WXDD","DDGB","QXDD","CWQRTK","HDSX","FDSX","DDJS"])).filter(OrderInfoDO.payId!=31).\
				   filter(OrderInfoDO.sellerId==1).filter(OrderInfoDO.shopId.notin_([16507,296068,137035,274225,296066,136686,291857,23,291857,18,132497,86290,177427,278555,56,12943,120220,86290,177427,40631,274629,278555,290801,234238,309906,67627,287302])).\
				   filter(OrderInfoDO.orderSn.notilike("%S%")).filter(OrderInfoDO.orderAmount>0).order_by(OrderInfoDO.id)[start:start+number]

		# .filter(OrderInfoDO.gmtCreate<'2016-01-01 00:00:00')

