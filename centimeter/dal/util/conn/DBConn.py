# -*- coding:utf-8 -*-
import importlib

from biz.common.exception.CentimeterException import ErrorTypeException
from common.util.log.Logger import Logger

__author__ = 'chenjinlong'
from abc import ABCMeta, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


from common.util.PathUtil import getSorcePath

import os

import re
# 创建对象的基类:
Base = declarative_base()

@Logger
class DBConn():
    __metaclass__ = ABCMeta
    @abstractmethod
    def sqlScheme(self):
        pass

    def conn(self):
        # 初始化数据库连接:
        engine = create_engine(self.sqlScheme(),echo=True)
        # 创建DBSession类型:
        self.DBSession = sessionmaker(bind=engine)
        self.sessionClassList = []

    def session(self,cls):
        if (not isinstance(cls,type)):
            raise ErrorTypeException("装饰器只能用于类上")
        cls.session=self.DBSession()
        return cls

    def register(self,cls):
        if (not isinstance(cls,type)):
            raise ErrorTypeException("装饰器只能用于类上")
        self.logger.info("%s上正在构建session..." %cls.__name__)
        cls.session=self.DBSession()
        self.sessionClassList.append(cls)
        self.logger.info("%s上完成构建session!" %cls.__name__)

    def close(self):
        for sessionClass in self.sessionClassList:
            self.logger.info("%s正在释放session..." %sessionClass.__name__)
            sessionClass.session.close()
            self.logger.info("%s完成释放session!" %sessionClass.__name__)


    def setMapperPath(self,path):
        if path.startswith("."):
            path = path[1:]
        filePath = path.replace(".",os.sep)

        mapperPath = os.sep.join([getSorcePath(),filePath])

        pattern = re.compile(r"[\w]*Mapper.py$")

        for rt, dirs, files in os.walk(mapperPath):
            spPattern = re.compile(filePath+r"/"+r"([\w\W]+)")
            match = spPattern.findall(rt)
            subPackageName = ""
            if match:
                subPackageName = match[0].replace(os.sep,".")
            for f in files:
                match = pattern.match(f)
                if match:
                    if subPackageName:
                        moudel = importlib.import_module(".".join([path,subPackageName,f[:-3]]))
                    else:
                        moudel = importlib.import_module(".".join([path,f[:-3]]))
                    cls = getattr(moudel,f[:-3])
                    self.register(cls)





def getClassName(moduleName):
    moduleName = ""
    className = moduleName
    if ".py" not in moduleName:
        className = moduleName[:-3]
    return className

def mapperFileVisit(args,dirs,fis):
    print args
    fis = modelNameFilter(fis)
    for fi in fis:
        print fi

def modelNameFilter(fis):
    newfis = []
    pattern = re.compile(r"[\w]*DO.py$")
    for fi in fis:
        match = pattern.match(fi)
        if match:
            newfis.append(fi)
    return newfis





