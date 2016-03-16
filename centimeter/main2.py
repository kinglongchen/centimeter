__author__ = 'chenjinlong'
import re

f = open("/Users/chenjinlong/Downloads/cpts_274_nz/css/font-awesome.css")
rex = r'^\.(fa-.+):'

l = []

for line in f:

    m = re.match(rex,line)
    if m:
        l.append('"'+m.group(1)+'"')

print("["+','.join(l)+"]")
f.close()