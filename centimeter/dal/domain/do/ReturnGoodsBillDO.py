# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,SmallInteger,DateTime,SmallInteger,DateTime,String,SmallInteger,SmallInteger,SmallInteger,String,SmallInteger,SmallInteger,DateTime,SmallInteger,SmallInteger,String,String,SmallInteger,String,SmallInteger,String,String,String,SmallInteger,DateTime,SmallInteger,String,Float,SmallInteger,String,String
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class ReturnGoodsBillDO(Base):

	# 表的名字:
	__tablename__ = 'erp_return_goods_bill'

	#操作人ID
	id=Column('id',SmallInteger,primary_key=True)
	#操作人ID
	creator=Column('creator',SmallInteger)

	#创建时间
	gmtCreate=Column('gmt_create',DateTime)

	#更新人
	modifier=Column('modifier',SmallInteger)

	#更新时间
	gmtModified=Column('gmt_modified',DateTime)

	#是否已删除
	isDeleted=Column('is_deleted',String(1))

	#订单类型
	billTypeId=Column('bill_type_id',SmallInteger)

	#源单类型
	sourceBillTypeId=Column('source_bill_type_id',SmallInteger)

	#源单ID
	sourceBillId=Column('source_bill_id',SmallInteger)

	#订单号
	billNo=Column('bill_no',String(80))

	#订单状态
	billStatus=Column('bill_status',SmallInteger)

	#审核人
	auditor=Column('auditor',SmallInteger)

	#审核时间
	gmtAudit=Column('gmt_audit',DateTime)

	#主订单类型
	mainBillTypeId=Column('main_bill_type_id',SmallInteger)

	#主订单ID
	mainBillId=Column('main_bill_id',SmallInteger)

	#主订单号
	mainBillNo=Column('main_bill_no',String(80))

	#出库单号
	saleOutWareBillNo=Column('sale_out_ware_bill_no',String(80))

	#发货仓库ID
	warehouseId=Column('warehouse_id',SmallInteger)

	#发货仓库名
	warehouseName=Column('warehouse_name',String(50))

	#退货仓库id
	returnWarehouseId=Column('return_warehouse_id',SmallInteger)

	#退货仓库名称
	returnWarehouseName=Column('return_warehouse_name',String(50))

	#客户名称
	customerName=Column('customer_name',String(255))

	#退货原因
	reason=Column('reason',String(1024))

	#期间id
	periodId=Column('period_id',SmallInteger)

	#订单创建时间
	orderCreateTime=Column('order_create_time',DateTime)

	#订单类型
	orderType=Column('order_type',SmallInteger)

	#制单人姓名
	creatorName=Column('creator_name',String(64))

	#
	returnAmount=Column('return_amount',Float)

	#0:未退款,1:已退款
	haveRefund=Column('have_refund',SmallInteger)

	#备注
	remark=Column('remark',String(255))

	#物流单号
	logisticsNo=Column('logistics_no',String(255))


