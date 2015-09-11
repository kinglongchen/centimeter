# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,DateTime,DateTime,SmallInteger,SmallInteger,String,SmallInteger,SmallInteger,SmallInteger,SmallInteger,SmallInteger,String,String,SmallInteger,SmallInteger,String,SmallInteger,String,Float,Float,Float,String,String,String,String,String,DateTime,String
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class OfferListGoodsDO(Base):

	# 表的名字:
	__tablename__ = 'db_offer_list_goods'

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

	#关联的报价单的id
	offerListId=Column('offer_list_id',SmallInteger)

	#关联的需求单的id
	wishListId=Column('wish_list_id',SmallInteger)

	#分组id，以确定是否是同一个商品
	groupId=Column('group_id',SmallInteger)

	#是否是用户选择付款的商品
	isUserSelectPay=Column('is_user_select_pay',SmallInteger)

	#db_goods的商品id
	goodsId=Column('goods_id',SmallInteger)

	#商品名称
	goodsName=Column('goods_name',String(255))

	#oe码
	goodsOe=Column('goods_oe',String(255))

	#品质
	goodsQualityType=Column('goods_quality_type',SmallInteger)

	#品牌id
	goodsBrandId=Column('goods_brand_id',SmallInteger)

	#品牌名称
	goodsBrand=Column('goods_brand',String(50))

	#数量
	goodsNumber=Column('goods_number',SmallInteger)

	#单位
	goodsMeasureUnit=Column('goods_measure_unit',String(10))

	#商品单价
	goodsPrice=Column('goods_price',Float)

	#商品总价
	goodsPriceAmount=Column('goods_price_amount',Float)

	#采购价
	purchasePrice=Column('purchase_price',Float)

	#发货状态
	shippingStatus=Column('shipping_status',String(20))

	#发货方式
	shippingType=Column('shipping_type',String(20))

	#快递物流公司
	shippingCompany=Column('shipping_company',String(50))

	#快递单号
	shippingNo=Column('shipping_no',String(255))

	#发货时拍摄的图片
	shippingImage=Column('shipping_image',String(255))

	#发货时间
	shippingTime=Column('shipping_time',DateTime)

	#SN编码
	goodsSn=Column('goods_sn',String(50))


