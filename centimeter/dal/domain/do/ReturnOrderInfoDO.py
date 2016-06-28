# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,String,SmallInteger,DateTime,SmallInteger,DateTime,SmallInteger,String,SmallInteger,String,SmallInteger,Float,Float,SmallInteger,String,DateTime,SmallInteger
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class ReturnOrderInfoDO(Base):

	# 表的名字:
	__tablename__ = 'erp_return_order_info'

	#是否已删除 N:未删除，Y:删除
	id=Column('id',SmallInteger,primary_key=True)
	#是否已删除 N:未删除，Y:删除
	isDeleted=Column('is_deleted',String(1))

	#创建人
	creator=Column('creator',SmallInteger)

	#创建时间
	gmtCreate=Column('gmt_create',DateTime)

	#修改人
	modifier=Column('modifier',SmallInteger)

	#修改时间
	gmtModified=Column('gmt_modified',DateTime)

	#单据ID
	billId=Column('bill_id',SmallInteger)

	#单据编号
	billNo=Column('bill_no',String(64))

	#退款类型
	refundMode=Column('refund_mode',SmallInteger)

	#客户名称
	customerName=Column('customer_name',String(64))

	#客户id
	customerId=Column('customer_id',SmallInteger)

	#订单金额
	orderAmount=Column('order_amount',Float)

	#退货金额
	returnAmount=Column('return_amount',Float)

	#退货仓库ID
	returnWarehouseId=Column('return_warehouse_id',SmallInteger)

	#退货仓库名称
	refundWarehouseName=Column('refund_warehouse_name',String(64))

	#订单创建时间
	gmtBillCreate=Column('gmt_bill_create',DateTime)

	#0:未退款,1:已退款
	haveRefund=Column('have_refund',SmallInteger)


