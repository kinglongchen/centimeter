# coding=utf-8
from common.util import PathUtil

__author__ = 'chenjinlong'
filePath = PathUtil.getOutputPath()+"/temp/orderSnFile.txt"

saveFilePath = PathUtil.getOutputPath()+"/receipt/result/orderSnFomat.txt"

fileInput = open(filePath,"r")
lines = fileInput.readlines()
formatOrderSnStr = ""
formatOrderSnSet = set()
count = 0
for line in lines:

    formatOrderSn =  '"%s",\n' %line.strip()
    if formatOrderSn in formatOrderSnSet:
        continue
    count+=1
    formatOrderSnSet.add(formatOrderSn)
    formatOrderSnStr +=formatOrderSn

saveInput = open(saveFilePath,'w')
saveInput.write(formatOrderSnStr)
print "处理完毕,数量:%s" %count



