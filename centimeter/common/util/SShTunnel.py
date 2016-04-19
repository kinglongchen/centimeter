# coding=utf-8
# from common.config.Config import Config

__author__ = 'chenjinlong'
# import traceback
#
# from sshtunnel import SSHTunnelForwarder
#
# from log.Logger import Logger
#
#
# @Logger
# class SSHTunnel(object):
#     def __init__(self, username, password, host, port=22,
#                  localBindAddress='127.0.0.1', localBindPort=3309,
#                  remoteBindAddress='127.0.0.1', remoteBindPort=5598):
#         self.__host = host
#         self.__port = port
#         self.__username = username
#         self.__password = password
#         self.__localBindAddress = localBindAddress
#         self.__localBindPort = localBindPort
#         self.__remoteBindAddress = remoteBindAddress
#         self.__remoteBindPort = remoteBindPort
#         self.__server = None
#
#     def start(self):
#         if not self.__server:
#             server = SSHTunnelForwarder(
#                 (self.__host, self.__port),
#                 ssh_username=self.__username,
#                 ssh_password=self.__password,
#                 local_bind_address=(self.__localBindAddress, self.__localBindPort),
#                 remote_bind_address=(self.__remoteBindAddress, self.__remoteBindPort))
#             self.__server = server
#         self.logger.info("正在启动SSH通道...")
#         self.__server.start()
#         self.logger.info("已建立SSH通道!")
#
#     def stop(self):
#         if not self.__server:
#             return
#         self.logger.info("正在退出SSH通道...")
#         self.__server.stop()
#         self.logger.info("完成SSH通道退出!")
#
#     def restart(self):
#         self.stop()
#         self.start()
#
#     @classmethod
#     def launcher(cls, username, password, host, port=22,
#                  localBindAddress='127.0.0.1', localBindPort=3309,
#                  remoteBindAddress='127.0.0.1', remoteBindPort=5598):
#         def _deco(func):
#             def __deco(*args, **kwargs):
#                 try:
#                     sshTunnel = cls(username, password, host, port,
#                                     localBindAddress, localBindPort,
#                                     remoteBindAddress, remoteBindPort)
#                     sshTunnel.start()
#                     rs = func(*args, **kwargs)
#                 except Exception, e:
#                     traceback.print_exc()
#                 finally:
#                     sshTunnel.stop()
#                 return rs
#
#             return __deco
#
#         return _deco
#
#     @classmethod
#     def factory(cls):
#         sshTunnel = cls(Config.sshUserName, Config.sshPassword, Config.sshHost, Config.sshPort,
#                         Config.localBindAddress, Config.localBindPort,
#                         Config.remoteBindAddress, Config.remoteBindPort)
#         return sshTunnel
#
#     @classmethod
#     def sshWrapper(cls, fun):
#         def _wrap(*args, **kwargs):
#             sshTunnel = None
#             try:
#                 sshTunnel = cls.factory()
#                 sshTunnel.start()
#                 rs = fun(*args, **kwargs)
#             finally:
#                 if sshTunnel:
#                     sshTunnel.stop()
#             return rs
#
#         return _wrap
