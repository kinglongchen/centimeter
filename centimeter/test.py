#coding=utf-8
from common.config.Config import Config
from common.email.EmailTool import EmailTool
from server.SummaryServiceImpl import SummaryServiceImpl
from server.WishListServiceImpl import WishListServiceImpl

__author__ = 'chenjinlong'
from dal.util.conn.MySqlConn import MySqlConn
from dal.mapper.SellerBrandCityMapper import SellerBrandCityMapper
#初始化配置参数
Config.initConf()

#@SSHTunnel.sshWrapper
@MySqlConn.dbWrapper
def main():
    sellerBrandCityMapper = SellerBrandCityMapper()
    sellerBrandCityDOList = sellerBrandCityMapper.getBySellerId(10036);
    sql_item = "SELECT * FROM db_wish_list WHERE "

    sql = " union\n".join([sql_item+"city_id=%s AND series=%s \n" %(sellerBrandCityDO.cityId,sellerBrandCityDO.carCategoryId) for sellerBrandCityDO in sellerBrandCityDOList])

    sqlFile = open("sql.txt","w")

    sqlFile.write(sql)

main()

