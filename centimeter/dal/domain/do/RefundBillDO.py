# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,String,DateTime,DateTime,SmallInteger,SmallInteger,String,SmallInteger,SmallInteger,DateTime,String,String,String,String,SmallInteger,SmallInteger,DateTime,Float,Float,Float,String,String,Float,String
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class RefundBillDO(Base):

	# 表的名字:
	__tablename__ = 'erp_refund_bill'

	#是否删除,N:未删除，Y:删除
	id=Column('id',SmallInteger,primary_key=True)
	#是否删除,N:未删除，Y:删除
	isDeleted=Column('is_deleted',String(1))

	#记录创建时间
	gmtCreate=Column('gmt_create',DateTime)

	#记录修改时间,如果时间是1970年则表示纪录未修改
	gmtModified=Column('gmt_modified',DateTime)

	#创建人，0表示无创建人值
	creator=Column('creator',SmallInteger)

	#修改人,如果为0则表示纪录未修改
	modifier=Column('modifier',SmallInteger)

	#订单号
	billNo=Column('bill_no',String(80))

	#订单状态,1表示保存状态
	billStatus=Column('bill_status',SmallInteger)

	#审核人,0表示无审核人值
	auditor=Column('auditor',SmallInteger)

	#审核时间
	gmtAudit=Column('gmt_audit',DateTime)

	#退货单号
	returnGoodsBillNo=Column('return_goods_bill_no',String(80))

	#订单号
	saleOrderBillNo=Column('sale_order_bill_no',String(80))

	#出库单号
	saleOutWareBillNo=Column('sale_out_ware_bill_no',String(80))

	#客户名称
	customerName=Column('customer_name',String(255))

	#退款类型:1:现金,2:银行转账,3:支付宝支付,4:微信支付,5:其他
	refundType=Column('refund_type',SmallInteger)

	#退款方式,1:退货款
	refundMode=Column('refund_mode',SmallInteger)

	#退款时间
	refundTime=Column('refund_time',DateTime)

	#退货金额
	returnGoodsAmount=Column('return_goods_amount',Float)

	#实退金额
	realReturnAmount=Column('real_return_amount',Float)

	#运费
	freightFee=Column('freight_fee',Float)

	#备注
	remarks=Column('remarks',String(255))

	#审核人姓名
	auditName=Column('audit_name',String(80))

	#订单金额
	orderAmount=Column('order_amount',Float)

	#订单号
	orderSn=Column('order_sn',String(80))


