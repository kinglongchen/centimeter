# -*- coding:utf-8 -*-
from DBConn import DBConn
from biz.util.log.Logger import Logger
from common.config.Config import Config

__author__ = 'chenjinlong'

@Logger
class MySqlConn(DBConn):
    __schemeHeader = 'mysql+mysqlconnector://'

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
        conn = cls(Config.dbHost, Config.dbUser, Config.dbPasswd, Config.dbName, Config.dbPort)
        conn.conn()
        conn.setMapperPath("dal.mapper")
        return conn

    @classmethod
    def dbWrapper(cls, fun):
        def _wrapper(*args, **kwargs):
            conn = None
            try:
                conn = cls.factory()
                rs = fun(*args, **kwargs)
            finally:
                if conn: conn.close()
            return rs

        return _wrapper


if __name__ == '__main__':
    print "%(name)s,%(sex)s" % dict
