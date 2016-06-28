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
        self.orderReceiptMapper.batchInsert(orderReceipt4InsertList,session)
        self.orderReceiptRecordMapper.batchInsert(orderReceiptRecord4InsertList,session)

    @MySqlConn.transaction
    def doOrderReceiptBatchInit(self, orderReceiptList, session):
        self.orderReceiptMapper.batchInsert(orderReceiptList,session)

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

