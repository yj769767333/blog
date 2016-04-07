# coding:utf-8

import hashlib

def md5(password):
    return hashlib.md5(password).hexdigest()
