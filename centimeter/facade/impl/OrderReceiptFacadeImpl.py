from dal.mapper.OrderReceiptMapper import OrderReceiptMapper
from dal.mapper.OrderReceiptRecordMapper import OrderReceiptRecordMapper
from dal.util.conn.MySqlConn import MySqlConn
from facade.OrderReceiptFacade import OrderReceiptFacade

__author__ = 'chenjinlong'

class OrderReceiptFacadeImpl(OrderReceiptFacade):


    def __init__(self):
        self.orderReceiptRecordMapper = OrderReceiptRecordMapper()
        self.orderReceiptMapper = OrderReceiptMapper()

    @MySqlConn.transaction
    def doOrderReceiptDataInit(self, orderReceipt4InsertList, orderReceiptRecord4InsertList, session):
        self.orderReceiptMapper.batchInsert(orderReceipt4InsertList,session)
        self.orderReceiptRecordMapper.batchInsert(orderReceiptRecord4InsertList,session)
