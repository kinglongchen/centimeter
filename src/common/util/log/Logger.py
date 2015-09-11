# -*- coding: utf-8 -*-
import BaseConfig

__author__ = 'chenjinlong'
import logging

from biz.common.exception.CentimeterException import ErrorTypeException


def Logger(*args, **kwargs):
    def warp(cls, level=logging.INFO):
        logger = logging.getLogger(cls.__name__)
        BaseConfig.setLoger(logger, level)
        cls.logger = logger
        return cls
    if len(args)==0:
        level = kwargs['level']
        if not level:
            raise TypeError("参数错误")
        def _deco(cls):
            if not isinstance(cls,type):
                raise ErrorTypeException("装饰器只能用于类上")
            return warp(cls,level)
        return _deco

    if len(args) == 1:
        cls = args[0]
        if not isinstance(cls,type):
            raise ErrorTypeException("装饰器只能用于类上")
        return warp(cls)
    raise TypeError("参数错误")
