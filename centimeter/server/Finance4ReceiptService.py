from dal.domain.do.OrderReceiptDO import OrderReceiptDO
from dal.domain.do.OrderReceiptRecordDO import OrderReceiptRecordDO
from dal.mapper.OrderInfoMapper import OrderInfoMapper
from dal.mapper.OrderReceiptMapper import OrderReceiptMapper
from dal.mapper.OrderReceiptRecordMapper import OrderReceiptRecordMapper

__author__ = 'chenjinlong'
class Finance4ReceiptService():
    orderInfoMapper = OrderInfoMapper()

    orderReceiptMapper = OrderReceiptMapper()

    orderReceiptRecordMapper = OrderReceiptRecordMapper()

    def doScript(self):

        orderInfoDO = self.orderInfoMapper.selectByPrimaryKey(1)

        print  orderInfoDO.companyName

    def doInsert4Record(self):
        record = OrderReceiptRecordDO()
        rs = self.orderReceiptRecordMapper.insertSelective(record)
        return rs

    def doInsert4Receipt(self):
        receipt = OrderReceiptDO()
        rs = self.orderReceiptMapper.insertSelective(receipt)
        return rs


