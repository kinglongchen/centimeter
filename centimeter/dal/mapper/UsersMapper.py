# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.UsersDO import UsersDO

"""
UsersMapper数据库操作接口类
"""

class UsersMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(UsersDO).filter(UsersDO.id==id).one()

	"""
	根据一组userName查询user
	"""
	def selectByUserName(self,userNameList):
		return self.session.query(UsersDO).filter(UsersDO.userName.in_(userNameList)).all()
