# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,String,SmallInteger,DateTime,SmallInteger,DateTime,SmallInteger,SmallInteger,SmallInteger,SmallInteger,String,SmallInteger,SmallInteger,SmallInteger,String,SmallInteger,String,SmallInteger,String,SmallInteger,Float,SmallInteger,String,String,SmallInteger,SmallInteger,String,DateTime,SmallInteger,String,DateTime,SmallInteger,String,DateTime,SmallInteger,String,DateTime,String,SmallInteger,DateTime,String,String,String,String,String,SmallInteger,String,String,SmallInteger,String,SmallInteger,SmallInteger,SmallInteger,String,SmallInteger,String,String,DateTime,SmallInteger,SmallInteger,String
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class SaleReturnExchangeBillDO(Base):

	# 表的名字:
	__tablename__ = 'erp_sale_return_exchange_bill'

	#是否已删除
	id=Column('id',SmallInteger,primary_key=True)
	#是否已删除
	isDeleted=Column('is_deleted',String(1))

	#创建人
	creator=Column('creator',SmallInteger)

	#创建时间
	gmtCreate=Column('gmt_create',DateTime)

	#修改人
	modifier=Column('modifier',SmallInteger)

	#修改时间
	gmtModified=Column('gmt_modified',DateTime)

	#申请单类型
	billTypeId=Column('bill_type_id',SmallInteger)

	#申请类型:1.退货 2.换货
	billApplyType=Column('bill_apply_type',SmallInteger)

	#源单类型
	sourceBillTypeId=Column('source_bill_type_id',SmallInteger)

	#源单ID
	sourceBillId=Column('source_bill_id',SmallInteger)

	#申请单号
	billNo=Column('bill_no',String(64))

	#申请单状态，1:已保存; 2:已提交; 3:一审通过；4:已退回；5: 作废 6:被退回；8:部分入库; 9:全部入库完毕; 10:部分入库完毕; 11:三审通过; 12:二审通过; 103:财务审核通过15 出库完结 16 入库完结 17出库入库完结;30:小二发货;31:客户签收;32:订单拒收;34:再次派送
	billStatus=Column('bill_status',SmallInteger)

	#主订单类型
	mainBillTypeId=Column('main_bill_type_id',SmallInteger)

	#主订单ID
	mainBillId=Column('main_bill_id',SmallInteger)

	#主订单编号
	mainBillNo=Column('main_bill_no',String(64))

	#发货仓库ID
	warehouseId=Column('warehouse_id',SmallInteger)

	#发货仓库名称
	warehouseName=Column('warehouse_name',String(64))

	#退货仓库ID
	returnWarehouseId=Column('return_warehouse_id',SmallInteger)

	#退货仓库名称
	returnWarehouseName=Column('return_warehouse_name',String(64))

	#运输方式 0：供应商承运 1：第三方物流 2：客户自提
	transportStyle=Column('transport_style',SmallInteger)

	#退换货运费
	shippingFee=Column('shipping_fee',Float)

	#运费承担方
	shippingFeeBearer=Column('shipping_fee_bearer',SmallInteger)

	#客户名称
	customerName=Column('customer_name',String(64))

	#退货原因
	reason=Column('reason',String(255))

	#一审人ID
	auditor=Column('auditor',SmallInteger)

	#客户联系方式
	phone=Column('phone',SmallInteger)

	#一审人
	firstAuditorName=Column('first_auditor_name',String(64))

	#一审时间
	gmtAudit=Column('gmt_audit',DateTime)

	#二审人ID
	secondAuditor=Column('second_auditor',SmallInteger)

	#二审人
	secondAuditorName=Column('second_auditor_name',String(64))

	#二审时间
	gmtSecondAudit=Column('gmt_second_audit',DateTime)

	#三审人ID
	threeAuditor=Column('three_auditor',SmallInteger)

	#三审人
	threeAuditorName=Column('three_auditor_name',String(64))

	#三审时间
	gmtThreeAudit=Column('gmt_three_audit',DateTime)

	#作废人ID
	revokePerson=Column('revoke_person',SmallInteger)

	#作废人
	revokePersonName=Column('revoke_person_name',String(64))

	#作废时间
	gmtRevoke=Column('gmt_revoke',DateTime)

	#作废原因
	revokeReason=Column('revoke_reason',String(255))

	#财务确认人ID
	financialAuditor=Column('financial_auditor',SmallInteger)

	#财务确认时间
	gmtFinancialAudit=Column('gmt_financial_audit',DateTime)

	#财务备忘录
	financeComment=Column('finance_comment',String(255))

	#备注
	comment=Column('comment',String(255))

	#制单人
	createName=Column('create_name',String(64))

	#自定义属性
	attributes=Column('attributes',String(1000))

	#上传图片URL
	cardUrl=Column('card_url',String(1000))

	#到货状态，默认为0（未到货），1已到货
	arrivalStatus=Column('arrival_status',SmallInteger)

	#财务确认人
	financialAuditorName=Column('financial_auditor_name',String(64))

	#WMS出库状态
	tradeStatus=Column('trade_status',String(10))

	#临时拣货仓位
	stockAllocationId=Column('stock_allocation_id',SmallInteger)

	#是否取消
	isCanceled=Column('is_canceled',String(1))

	#打包区仓位
	packAreaAllocationId=Column('pack_area_allocation_id',SmallInteger)

	#待发区货位ID
	stockDeliveryAllocationId=Column('stock_delivery_allocation_id',SmallInteger)

	#货站id
	stationId=Column('station_id',SmallInteger)

	#货站名称
	stationName=Column('station_name',String(255))

	#物流公司id
	logisticsId=Column('logistics_id',SmallInteger)

	#物流公司名称
	logisticsName=Column('logistics_name',String(255))

	#换货订单号
	exchangeOrderSn=Column('exchange_order_sn',String(64))

	#退货商品上架时间
	onShelvesTime=Column('on_shelves_time',DateTime)

	#0:非wms,1:wms
	isWms=Column('is_wms',SmallInteger)

	#0:未退款,1:已退款
	haveRefund=Column('have_refund',SmallInteger)

	#金融订单发起的批次号
	batchNoForFinance=Column('batch_no_for_finance',String(64))


