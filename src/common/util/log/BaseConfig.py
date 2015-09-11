# coding=utf-8
__author__ = 'chenjinlong'
import logging
from logging.handlers import TimedRotatingFileHandler

from common.util import PathUtil


def getLogFilePath():
    return '/'.join([PathUtil.getLogDirPath(),'common.log'])

# 创建一个handler，用于写入日志文件
fh = TimedRotatingFileHandler(getLogFilePath(),'D')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

# 定义handler的输出格式formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)

fh.setLevel(logging.DEBUG)

ch.setFormatter(formatter)

ch.setLevel(logging.DEBUG)


def setLoger(logger,level=logging.INFO):
    logger.setLevel(level)
    if ch not in logger.handlers:
        logger.addHandler(ch)

    if fh not in logger.handlers:
        logger.addHandler(fh)

if __name__=='__main__':
    logger = logging.getLogger("test");
    setLoger(logger)
    logger.info("this.is test")


