# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,String,DateTime,DateTime,SmallInteger,SmallInteger,SmallInteger,String,SmallInteger,String
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class WishListActionReasonDO(Base):

	# 表的名字:
	__tablename__ = 'db_wish_list_action_reason'

	#是否删除,Y删除，N未删除
	id=Column('id',SmallInteger,primary_key=True)
	#是否删除,Y删除，N未删除
	isDeleted=Column('is_deleted',String(1))

	#创建时间，入库时间
	gmtCreate=Column('gmt_create',DateTime)

	#修改时间
	gmtModified=Column('gmt_modified',DateTime)

	#创建人
	creator=Column('creator',SmallInteger)

	#修改人
	modifier=Column('modifier',SmallInteger)

	#需求单id
	wishListId=Column('wish_list_id',SmallInteger)

	#取消（QX）or退货（TH）
	type=Column('type',String(20))

	#原因id
	reasonId=Column('reason_id',SmallInteger)

	#原因
	reason=Column('reason',String(1000))


