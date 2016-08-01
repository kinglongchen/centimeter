# coding=utf-8
from dal.mapper.PayOrderItemMapper import PayOrderItemMapper
from dal.mapper.PayOrderMapper import PayOrderMapper
from dal.util.conn.MySqlConn import MySqlConn
from facade.PayOrderFacade import PayOrderFacade

__author__ = 'chenjinlong'
class PayOrderFacadeImpl(PayOrderFacade):
    payOrderMapper = PayOrderMapper()
    payOrderItemMapper = PayOrderItemMapper()

    @MySqlConn.transaction
    def updateAmount(self,updatePayOrderAmountInfo,updatePayOrderItemAmountInfo,session):
        print "正在执行修改操作。。。"
        self.payOrderMapper.updatePayOrderAmount(updatePayOrderAmountInfo,session)
        self.payOrderItemMapper.updatePayOrderItemAmount(updatePayOrderItemAmountInfo,session)
        print "修改操作执行完成!"