# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,DateTime,DateTime,SmallInteger,SmallInteger,String,SmallInteger,String,String,SmallInteger,SmallInteger,SmallInteger,String,String,String
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class WishListGoodsDO(Base):

	# 表的名字:
	__tablename__ = 'db_wish_list_goods'

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

	#关联的需求单的id
	wishListId=Column('wish_list_id',SmallInteger)

	#商品名称
	goodsName=Column('goods_name',String(255))

	#oe码
	goodsOe=Column('goods_oe',String(255))

	#品质
	goodsQualityType=Column('goods_quality_type',SmallInteger)

	#分组id，以确定是否是同一个商品
	groupId=Column('group_id',SmallInteger)

	#数量
	goodsNumber=Column('goods_number',SmallInteger)

	#单位
	goodsMeasureUnit=Column('goods_measure_unit',String(10))

	#图片列表
	goodsImages=Column('goods_images',String(1000))

	#备注
	goodsMemo=Column('goods_memo',String(1000))


