# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,SmallInteger,String,String,SmallInteger,SmallInteger,SmallInteger,String,String,String,String,SmallInteger,SmallInteger,SmallInteger,SmallInteger,String,String,String,String,SmallInteger,DateTime,Float,Float,SmallInteger,SmallInteger,SmallInteger,SmallInteger,String,SmallInteger,DateTime,SmallInteger,SmallInteger,SmallInteger,String,String,SmallInteger,SmallInteger,String,String,String,String,String,String,String,SmallInteger,Float,String,String,String,String,String,String,String,String,String,String,SmallInteger,SmallInteger,DateTime,DateTime,SmallInteger,String,String
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class UsersDO(Base):

	# 表的名字:
	__tablename__ = 'db_users'

	#所属门店id
	userId=Column('user_id',SmallInteger,primary_key=True)
	#所属门店id
	clientId=Column('client_id',SmallInteger)

	#客户编号（来自于CRM）
	clientNum=Column('client_num',String(128))

	#客户名称（来自于CRM）
	clientName=Column('client_name',String(255))

	#与该客户绑定的销售员
	saleId=Column('sale_id',SmallInteger)

	#销售人员跟客户绑定时间（来自于CRM）
	bindTime=Column('bind_time',SmallInteger)

	#绑定关系十分解除（0：未解除 1：已解除）
	isBindDelete=Column('is_bind_delete',SmallInteger)

	#
	email=Column('email',String(60))

	#
	userName=Column('user_name',String(60))

	#名称
	userTitle=Column('user_title',String(100))

	#联系人
	contact=Column('contact',String(20))

	#省份
	province=Column('province',SmallInteger)

	#城市
	city=Column('city',SmallInteger)

	#
	district=Column('district',SmallInteger)

	#街道
	street=Column('street',SmallInteger)

	#详细地址
	address=Column('address',String(200))

	#
	password=Column('password',String(32))

	#
	question=Column('question',String(255))

	#
	answer=Column('answer',String(255))

	#
	sex=Column('sex',SmallInteger)

	#
	birthday=Column('birthday',DateTime)

	#
	userMoney=Column('user_money',Float)

	#
	frozenMoney=Column('frozen_money',Float)

	#
	payPoints=Column('pay_points',SmallInteger)

	#
	rankPoints=Column('rank_points',SmallInteger)

	#
	addressId=Column('address_id',SmallInteger)

	#
	regTime=Column('reg_time',SmallInteger)

	#
	lastIp=Column('last_ip',String(15))

	#
	lastLogin=Column('last_login',SmallInteger)

	#
	lastTime=Column('last_time',DateTime)

	#
	visitCount=Column('visit_count',SmallInteger)

	#
	userRank=Column('user_rank',SmallInteger)

	#1：代表门店主帐号0：代表副帐号
	isSpecial=Column('is_special',SmallInteger)

	#
	ecSalt=Column('ec_salt',String(10))

	#
	salt=Column('salt',String(10))

	#
	parentId=Column('parent_id',SmallInteger)

	#
	flag=Column('flag',SmallInteger)

	#
	alias=Column('alias',String(60))

	#
	msn=Column('msn',String(60))

	#
	qq=Column('qq',String(20))

	#
	officePhone=Column('office_phone',String(20))

	#
	homePhone=Column('home_phone',String(20))

	#
	mobilePhone=Column('mobile_phone',String(20))

	#手机验证码
	verify=Column('verify',String(4))

	#
	isValidated=Column('is_validated',SmallInteger)

	#
	creditLine=Column('credit_line',Float)

	#
	passwdQuestion=Column('passwd_question',String(50))

	#
	passwdAnswer=Column('passwd_answer',String(255))

	#邮政编码
	zipcode=Column('zipcode',String(11))

	#客户端设备号
	deviceId=Column('device_id',String(128))

	#客户简称
	shortName=Column('short_name',String(128))

	#省份名称
	provinceName=Column('province_name',String(64))

	#城市名称
	cityName=Column('city_name',String(64))

	#地区名称
	districtName=Column('district_name',String(64))

	#销售员工号
	staffNo=Column('staff_no',String(64))

	#
	comment=Column('comment',String(255))

	#用户类型：1门店、2普通用户 
	userType=Column('user_type',SmallInteger)

	#认证状态（0:缺省－未认证；1:认证中；2认证成功；－1:认证失败）
	verifyStatus=Column('verify_status',SmallInteger)

	#认证时间
	verifyTime=Column('verify_time',DateTime)

	#修改时间
	gmtModifed=Column('gmt_modifed',DateTime)

	#CRM的客户ID
	customerId=Column('customer_id',SmallInteger)

	#crm同步主键
	userGlobalId=Column('user_global_id',String(32))

	#用户创建来源
	appReg=Column('app_reg',String(32))


