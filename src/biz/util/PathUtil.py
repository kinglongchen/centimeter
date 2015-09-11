__author__ = 'chenjinlong'
import sys
import os

__currentPath__=os.path.split(os.path.realpath(__file__))[0]

def getRootDirPath():
    return os.sep.join(__currentPath__.split(os.sep)[:-3])

def getLogDirPath():
    return os.sep.join([getRootDirPath(),'output','log'])

def getResourcePath():
    return os.sep.join([getRootDirPath(),"resource"])

def getConfigPath():
    return os.sep.join([getRootDirPath(),"conf"])

def getSorcePath():
    return os.sep.join([getRootDirPath(),'src'])

if __name__ == "__main__":
    print getRootDirPath()
    print getLogDirPath()
    print getSorcePath()