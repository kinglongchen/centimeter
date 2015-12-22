from common.config.Config import Config

__author__ = 'chenjinlong'
from dal.mapper.UsersMapper import UsersMapper
class UserDao(object):
    userMapper = UsersMapper()

    def getByUserNameList(self,userNameList):
        return self.userMapper.selectByUserName(userNameList)

    def getExcludeUserIdList(self):
        return Config.excludeFilterUserIdList;
        # excludeFilterList = Config.excludeFilterList
        # userList = self.getByUserNameList(excludeFilterList)
        # userIdList = []
        # for user in userList:
        #     userIdList.append(user.userId)
        # return userIdList
