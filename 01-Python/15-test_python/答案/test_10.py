# @Author : 强小林
# @CreateDate : 2020/5/19 16:05
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription : 

"""
python打卡第十天

1、导入模块，导入模块中的类，导入模块中的方法，导入模块中的变量
import 模块名
from 模块名 import 类名
from 模块名 import 方法名
from 模块名 import 变量名

2、创建一个test.txt文件，向文件中写入几行内容，读取文件内容并打印出来

"""

import os
from datetime import datetime


with open("test_10.txt", "w", encoding="utf8") as fw:
    fw.writelines(["1\n", "2\n", "3\n"])

with open("test_10.txt", "r", encoding="utf8") as fr:
    content = fr.read()
    print(content)
