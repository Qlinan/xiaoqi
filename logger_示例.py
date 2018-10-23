# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:44:20 2018

@author: Tarena
"""

import logging
import sys

#获取logger的实例
logger = logging.getLogger("testLog")
#指定logger格式
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
#创建具体的日志handler
file_handler = logging.FileHandler("testLog.log",encoding="utf-8")
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
#设置日志的级别
#高于等于这个级别的日志才会被写
logger.setLevel(logging.INFO)
#把日志的handler添加到logger实例中
logger.addHandler(file_handler)
logger.addHandler(console_handler)

#写日志
logger.error("test error log")
logger.error("test info log")
logger.error("test debug log")
#清空日志handler
logger.removeHandler(file_handler)
logger.removeHandler(console_handler)