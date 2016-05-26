# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,DateTime,SmallInteger,DateTime,SmallInteger,String,SmallInteger,Float,String,SmallInteger,SmallInteger,DateTime,SmallInteger,String,SmallInteger,String
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class PayOrderItemDO(Base):

	# 表的名字:
	__tablename__ = 'fc_pay_order_item'

	#创建时间
	id=Column('id',SmallInteger,primary_key=True)
	#创建时间
	gmtCreate=Column('gmt_create',DateTime)

	#创建人ID
	creator=Column('creator',SmallInteger)

	#更新时间
	gmtModified=Column('gmt_modified',DateTime)

	#更新人ID
	modifier=Column('modifier',SmallInteger)

	#是否删除,Y删除,N未删除
	isDeleted=Column('is_deleted',String(1))

	#支付订单id
	payOrderId=Column('pay_order_id',SmallInteger)

	#明细金额
	itemAmount=Column('item_amount',Float)

	#外部支付流水号，比如：支付宝流水号
	outPayNo=Column('out_pay_no',String(50))

	#支付类型，参考db_payment
	payId=Column('pay_id',SmallInteger)

	#0:未支付，1:支付中，2:已支付，3:已取消,4:已失效
	payStatus=Column('pay_status',SmallInteger)

	#支付时间
	payTime=Column('pay_time',DateTime)

	#操作方资产账户id
	fromAccountId=Column('from_account_id',SmallInteger)

	#操作方账户名称
	fromAccountName=Column('from_account_name',String(50))

	#对方资产账户id
	toAccountId=Column('to_account_id',SmallInteger)

	#对方资产账户名称
	toAccountName=Column('to_account_name',String(50))


