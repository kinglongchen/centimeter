# -*- coding:utf-8 -*-
from DBConn import DBConn
from common.config.Config import Config
from common.util.log.Logger import Logger

__author__ = 'chenjinlong'


@Logger
class MySqlConn(DBConn):
    __schemeHeader = 'mysql+mysqlconnector://'

    connection = None

    def __init__(self, db_host, db_user, db_passwd, db_name, db_port='3306'):
        self.__class__.schemeParam = {
            'header': self.__schemeHeader,
            'db_host': db_host,
            'db_user': db_user,
            'db_passwd': db_passwd,
            'db_name': db_name,
            'db_port': db_port
        }

    def sqlScheme(self):
        return '%(header)s%(db_user)s:%(db_passwd)s@%(db_host)s:%(db_port)s/%(db_name)s' % self.schemeParam

    @classmethod
    def factory(cls):
        if not cls.connection :
            cls.connection = cls(Config.dbHost, Config.dbUser, Config.dbPasswd, Config.dbName, Config.dbPort)
            cls.connection.conn()
        cls.connection.setMapperPath("dal.mapper")
        return cls.connection

    @classmethod
    def dbWrapper(cls, fun):
        def _wrapper(*args, **kwargs):
            conn = None
            try:
                conn = cls.factory()
                rs = fun(*args, **kwargs)
            finally:
                if conn:
                    conn.close()
            return rs

        return _wrapper

    # 用于事务的注解
    @classmethod
    def transaction(cls,fun):
        if not cls.connection:
            cls.connection = cls(Config.dbHost, Config.dbUser, Config.dbPasswd, Config.dbName, Config.dbPort)
            cls.connection.conn()
        def __wrapper(*args,**kwargs):
            session = cls.connection.DBSession()
            kwargs["session"]= session
            try:
                rs = fun(*args,**kwargs)
                session.commit()
            except Exception,e:
                session.rollback()
                raise e
            finally:
                session.close()
            return rs
        return __wrapper


if __name__ == '__main__':
    print "%(name)s,%(sex)s" % dict
