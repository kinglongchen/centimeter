# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,DateTime,SmallInteger,DateTime,SmallInteger,String,SmallInteger,SmallInteger,Float,SmallInteger,String,String,String,SmallInteger,SmallInteger,DateTime,DateTime,String,String,SmallInteger,String,SmallInteger,Float
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class PayOrderDO(Base):

	# 表的名字:
	__tablename__ = 'fc_pay_order'

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

	#如果是档口B账户，指的就是shopId
	foreignUserId=Column('foreign_user_id',SmallInteger)

	#资产账户id
	financeAccountId=Column('finance_account_id',SmallInteger)

	#支付金额
	payOrderAmount=Column('pay_order_amount',Float)

	#应用id
	platformId=Column('platform_id',SmallInteger)

	#应用名称,冗余字段
	platformName=Column('platform_name',String(50))

	#关联的外部业务编号,，比如订单指的就是orderSn
	outOrderSn=Column('out_order_sn',String(50))

	#支付订单流水号
	payOrderSn=Column('pay_order_sn',String(50))

	#0:未支付，1:支付中，2:已支付，3:已取消/已失效 4:部分支付
	payStatus=Column('pay_status',SmallInteger)

	#1:订单,2:退货订单,3:换货订单,4:充值订单,5:提现订单,6:冲销流水订单,7:pos机支付撤销
	orderType=Column('order_type',SmallInteger)

	#支付时间
	payTime=Column('pay_time',DateTime)

	#取消时间
	cancelTime=Column('cancel_time',DateTime)

	#备注,比如:记录商品名称
	memo=Column('memo',String(256))

	#对方资产账户名称
	toAccountName=Column('to_account_name',String(50))

	#操作方资产账户id
	fromAccountId=Column('from_account_id',SmallInteger)

	#操作方账户名称
	fromAccountName=Column('from_account_name',String(50))

	#对方资产账户id
	toAccountId=Column('to_account_id',SmallInteger)

	#已支付金额
	paidAmount=Column('paid_amount',Float)


