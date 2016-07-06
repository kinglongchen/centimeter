# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,DateTime,SmallInteger,DateTime,SmallInteger,String,SmallInteger,SmallInteger,String,String,String,Float,Float,Float,Float,Float,String
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class OrderReceiptRecordDO(Base):

	# 表的名字:
	__tablename__ = 'fc_order_receipt_record'

	#创建时间
	id=Column('id',SmallInteger,primary_key=True)
	#创建时间
	gmtCreate=Column('gmt_create',DateTime,default='1970-01-01 12:00:00')

	#创建人ID
	creator=Column('creator',SmallInteger,default=0)

	#更新时间
	gmtModified=Column('gmt_modified',DateTime,default='1970-01-01 12:00:00')

	#更新人ID
	modifier=Column('modifier',SmallInteger,default=0)

	#是否删除,Y删除,N未删除
	isDeleted=Column('is_deleted',String(1),default='N')

	#资产账户id
	financeAccountId=Column('finance_account_id',SmallInteger,default=0)

	#应用id
	platformId=Column('platform_id',SmallInteger,default=0)

	#应用名称,冗余字段
	platformName=Column('platform_name',String(50),default='')

	#关联的外部业务编号,比如订单指的就是orderSn
	outOrderSn=Column('out_order_sn',String(50),default='')

	#动作
	receiptAction=Column('receipt_action',String(50),default='')

	#拒收金额
	rejectAmount=Column('reject_amount',Float,default=0)

	#退货金额
	refundAmount=Column('refund_amount',Float,default=0)

	#应收金额
	needReceiveAmount=Column('need_receive_amount',Float,default=0)

	#实际收款金额
	hasReceivedAmount=Column('has_received_amount',Float,default=0)

	#余额（应收－实收）
	remainingAmount=Column('remaining_amount',Float,default=0)

	#备注
	receiptMemo=Column('receipt_memo',String(256),default='')


