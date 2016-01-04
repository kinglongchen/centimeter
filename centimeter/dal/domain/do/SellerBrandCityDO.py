# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,DateTime,DateTime,SmallInteger,SmallInteger,String,SmallInteger,SmallInteger,SmallInteger
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class SellerBrandCityDO(Base):

	# 表的名字:
	__tablename__ = 'db_seller_brand_city'

	#创建时间
	id=Column('id',SmallInteger,primary_key=True)
	#创建时间
	gmtCreate=Column('gmt_create',DateTime)

	#修改时间
	gmtModified=Column('gmt_modified',DateTime)

	#创建人id
	creator=Column('creator',SmallInteger)

	#修改人id
	modifier=Column('modifier',SmallInteger)

	#N: 未删除，Y:已删除
	isDeleted=Column('is_deleted',String(1))

	#商家id
	sellerId=Column('seller_id',SmallInteger)

	#汽车品牌id
	carCategoryId=Column('car_category_id',SmallInteger)

	#城市id
	cityId=Column('city_id',SmallInteger)


