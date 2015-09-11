# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()


class WishListDO(Base):
    # 表的名字:
    __tablename__ = 'db_wish_list'

    # 表的结构:
    id = Column('id',Integer, primary_key=True)
    gmtCreate = Column('gmt_create',DateTime)
    gmtModified = Column('gmt_modified',DateTime)
    creator = Column('creator',Integer)
    modifier = Column('modifier',Integer)
    isDeleted = Column('is_deleted',String(1))
    wishListSn = Column('wish_list_sn',String(20))
    status = Column('status',String(20))
    userId = Column('user_id',Integer)
    wishListMaker = Column('wish_list_maker',String(20))
    wishListMakerTel = Column('wish_list_maker_tel',String(20))
    vin = Column('vin',String(50))
    isDeckVehicle = Column('is_deck_vehicle',Integer)
    isModifiedVehicle = Column('is_modified_vehicle',Integer)
    isReceiptRrice = Column('is_receipt_price',Integer)
    brand = Column('brand',Integer)
    series = Column('series',Integer)
    model = Column('model',Integer)
    engine = Column('engine',Integer)
    year = Column('year',Integer)
    tqCarModelId = Column('tq_car_model_id',Integer)
    companyName = Column('company_name',String(255))
    telephone = Column('telephone',String(20))
    cityId = Column('city_id',Integer)
    wishListMemo = Column('wish_list_memo',String(1000))
    wishStartTime = Column('wish_start_time',DateTime)
    wishEndTime = Column('wish_end_time',DateTime)
    refer = Column('refer',String(100))
    deviceId = Column('device_id',String(255))
    token = Column('token',String(60))
    isNew = Column('is_new',String(1))
    sellerLastLlertTime = Column('seller_last_alert_time',DateTime)
