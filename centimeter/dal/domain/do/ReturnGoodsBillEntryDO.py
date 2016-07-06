# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,SmallInteger,DateTime,SmallInteger,DateTime,String,SmallInteger,SmallInteger,SmallInteger,SmallInteger,SmallInteger,SmallInteger,SmallInteger,SmallInteger,String,SmallInteger,String,SmallInteger,String,SmallInteger,SmallInteger,String,SmallInteger,Float,Float
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class ReturnGoodsBillEntryDO(Base):

	# 表的名字:
	__tablename__ = 'erp_return_goods_bill_entry'

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

	#单据ID
	billId=Column('bill_id',SmallInteger)

	#单据类型
	billTypeId=Column('bill_type_id',SmallInteger)

	#来源单据类型
	sourceBillTypeId=Column('source_bill_type_id',SmallInteger)

	#来源单据ID
	sourceBillId=Column('source_bill_id',SmallInteger)

	#来源单据分录ID
	sourceBillEntryId=Column('source_bill_entry_id',SmallInteger)

	#分录状态
	billEntryStatus=Column('bill_entry_status',SmallInteger)

	#主订单类型
	mainBillTypeId=Column('main_bill_type_id',SmallInteger)

	#主订单ID
	mainBillId=Column('main_bill_id',SmallInteger)

	#主订单号
	mainBillNo=Column('main_bill_no',String(80))

	#发货仓库ID
	warehouseId=Column('warehouse_id',SmallInteger)

	#仓库名
	warehouseName=Column('warehouse_name',String(50))

	#退货货仓库ID
	returnWarehouseId=Column('return_warehouse_id',SmallInteger)

	#退货仓库名
	returnWarehouseName=Column('return_warehouse_name',String(50))

	#退货数量
	returnQty=Column('return_qty',SmallInteger)

	#商品id
	goodsId=Column('goods_id',SmallInteger)

	#商品编码
	goodsSn=Column('goods_sn',String(20))

	#应发数量
	sendQty=Column('send_qty',SmallInteger)

	#退货单价
	returnPrice=Column('return_price',Float)

	#退货金额
	returnAmount=Column('return_amount',Float)


