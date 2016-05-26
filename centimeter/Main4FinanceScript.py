# coding=utf-8
from common.config.Config import Config
from dal.util.conn.MySqlConn import MySqlConn
from server.Finance4ReceiptService import Finance4ReceiptService

__author__ = 'chenjinlong'

#初始化配置参数
Config.initConf()

@MySqlConn.dbWrapper
def main():
    fileInput = open("../output/receipt/retryfile.txt","w")
    try:
        service = Finance4ReceiptService(fileInput)

        payOrderList = service.selectBatch(0)
    except Exception,e:
        print e
    finally:
        fileInput.close()


    print len(payOrderList)

main()