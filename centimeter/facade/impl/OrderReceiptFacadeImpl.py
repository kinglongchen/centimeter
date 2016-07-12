# coding=utf-8
from dal.domain.do.OrderReceiptDO import OrderReceiptDO
from dal.mapper.OrderReceiptMapper import OrderReceiptMapper
from dal.mapper.OrderReceiptRecordMapper import OrderReceiptRecordMapper
from dal.util.conn.MySqlConn import MySqlConn
from facade.OrderReceiptFacade import OrderReceiptFacade

__author__ = 'chenjinlong'

class OrderReceiptFacadeImpl(OrderReceiptFacade):


    def __init__(self):
        self.orderReceiptRecordMapper = OrderReceiptRecordMapper()
        self.orderReceiptMapper = OrderReceiptMapper()
        self.orderReceiptMapper = OrderReceiptMapper()

    @MySqlConn.transaction
    def doOrderReceiptDataInit(self, orderReceipt4InsertList, orderReceiptRecord4InsertList, session):
        print "正在执行插入操作。。。"
        self.orderReceiptMapper.batchInsert2(orderReceipt4InsertList,session)
        self.orderReceiptRecordMapper.batchInsert2(orderReceiptRecord4InsertList,session)
        print "插入操作完成！！！"


    @MySqlConn.transaction
    def doOrderReceiptBatchInit(self, orderReceiptList, session):
        self.orderReceiptMapper.batchInsert(orderReceiptList,session)

    @MySqlConn.transaction
    def doOrderReceiptBatchInit2(self, orderReceiptList, session):
        self.orderReceiptMapper.batchInsert2(orderReceiptList,session)

    @MySqlConn.transaction
    def doBatchUpdateById(self,session):

        orderReceiptDOList = []
        # for i in range(1,100):
        #     orderReceiptDO = OrderReceiptDO()
        #     orderReceiptDO.outOrderSn = "out_order_sn"+str(i)
        #     orderReceiptDOList.append(orderReceiptDO)
        #
        # self.orderReceiptMapper.batchInsert(orderReceiptDOList,session)

        for i in range(1,100):
            orderReceiptDO = OrderReceiptDO()
            orderReceiptDO.id = 198+i
            orderReceiptDO.memo = "memo"+str(i)
            orderReceiptDOList.append(orderReceiptDO)


        self.orderReceiptMapper.batchUpdateById(orderReceiptDOList,session)

