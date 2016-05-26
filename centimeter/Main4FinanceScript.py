# coding=utf-8
from common.config.Config import Config
from dal.util.conn.MySqlConn import MySqlConn
from server.Finance4ReceiptService import Finance4ReceiptService

__author__ = 'chenjinlong'

#初始化配置参数
Config.initConf()

@MySqlConn.dbWrapper
def main():
    service = Finance4ReceiptService()

    payOrderList = service.selectBatch(0)

    print len(payOrderList)

main()