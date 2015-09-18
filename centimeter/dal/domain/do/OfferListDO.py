# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,DateTime,DateTime,SmallInteger,SmallInteger,String,String,SmallInteger,String,String,String,String,String,String,String,SmallInteger,SmallInteger,String,String,Float,Float,DateTime,DateTime,String,DateTime,DateTime,SmallInteger,SmallInteger,SmallInteger,SmallInteger,String,SmallInteger,SmallInteger,String,String,DateTime,String,String,String,String,String,Float,Float,Float,Float,Float,String,String,String,SmallInteger
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class OfferListDO(Base):

	# 表的名字:
	__tablename__ = 'db_offer_list'

	#
	id=Column('id',SmallInteger,primary_key=True)
	#
	gmtCreate=Column('gmt_create',DateTime)

	#
	gmtModified=Column('gmt_modified',DateTime)

	#
	creator=Column('creator',SmallInteger)

	#
	modifier=Column('modifier',SmallInteger)

	#
	isDeleted=Column('is_deleted',String(1))

	#报价单编码
	offerListSn=Column('offer_list_sn',String(20))

	#关联的需求单id
	wishListId=Column('wish_list_id',SmallInteger)

	#报价单的状态（报价中、已支付、已发货、已签收、已结算）
	status=Column('status',String(10))

	#业务经理手机号
	saleTel=Column('sale_tel',String(20))

	#报价单的支付状态（WZF、ZFZ、YZF）
	payStatus=Column('pay_status',String(10))

	#报价单的发货状态（WFH、BFFH、YFH）
	shippingStatus=Column('shipping_status',String(10))

	#结算状态
	settleStatus=Column('settle_status',String(10))

	#结算状态
	receiveStatus=Column('receive_status',String(10))

	#
	# shipping=Column('shipping',String(255))

	#用户id
	userId=Column('user_id',SmallInteger)

	#商家id
	sellerId=Column('seller_id',SmallInteger)

	#商家名称
	sellerName=Column('seller_name',String(100))

	#商家qq
	sellerQq=Column('seller_qq',String(20))

	#报价单总金额
	offerAmount=Column('offer_amount',Float)

	#报价单已支付金额
	paidOfferAmount=Column('paid_offer_amount',Float)

	#用户发起支付的时间（点击跳到支付宝那一刹那的时间）
	payingTime=Column('paying_time',DateTime)

	#用户支付时间
	paidTime=Column('paid_time',DateTime)

	#
	payNo=Column('pay_no',String(50))

	#结算时间
	settleTime=Column('settle_time',DateTime)

	#结算时间
	receiveTime=Column('receive_time',DateTime)

	#省份
	province=Column('province',SmallInteger)

	#城市
	city=Column('city',SmallInteger)

	#区域
	district=Column('district',SmallInteger)

	#街道
	street=Column('street',SmallInteger)

	#详细地址
	address=Column('address',String(255))

	#付款方式
	payId=Column('pay_id',SmallInteger)

	#发货方式
	shippingType=Column('shipping_type',SmallInteger)

	#快递物流公司
	shippingCompany=Column('shipping_company',String(50))

	#快递单号
	shippingNo=Column('shipping_no',String(255))

	#系统自动给供应商打款的时间
	autoPayTime=Column('auto_pay_time',DateTime)

	#令牌
	token=Column('token',String(255))

	#临时保存商品报价的草稿 商品list的json的数据
	draft=Column('draft',String(4000))

	#联系人
	consignee=Column('consignee',String(50))

	#门店名称
	companyName=Column('company_name',String(255))

	#联系电话
	telephone=Column('telephone',String(20))

	#需要给供应商的结算金额
	needSettleAmount=Column('need_settle_amount',Float)

	#已经给供应商支付的结算金额
	hasSettleAmount=Column('has_settle_amount',Float)

	#需要给客户的退款金额
	needRefundAmount=Column('need_refund_amount',Float)

	#已经给客户支付的退款金额
	hasRefundAmount=Column('has_refund_amount',Float)

	#供应商佣金比率
	commissionRate=Column('commission_rate',Float)

	#报价单备注
	offerListMemo=Column('offer_list_memo',String(256))

	#
	isNew=Column('is_new',String(1))

	#扩展字段
	feature=Column('feature',String(1000))

	#erp虚拟订单状态
	erpOrderStatus=Column('erp_order_status',SmallInteger)


