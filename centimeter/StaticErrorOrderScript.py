# coding=utf-8
__author__ = 'chenjinlong'
#fileInput = open("../output/receipt/retryfile.txt","r")
fileInput = open("../output/receipt/result/select_receipt_order.txt","r")
line = fileInput.readline()
count = 0
while line:
    count += line.count('",')
    line = fileInput.readline()

print "异常订单数:%s" %count