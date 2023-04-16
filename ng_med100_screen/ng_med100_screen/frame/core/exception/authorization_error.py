# coding=UTF-8

'''
Created on 2016-7-4

@author: YRK
'''
from frame.core.exception.base import BaseError


class AuthorizationCodes(object):
    ACCESS_LIMIT = 60001


class AuthorizationError(BaseError):
    code = AuthorizationCodes.ACCESS_LIMIT
    desc = "JWT TOKEN 无效"
