'''
Author: FF fengfan1@lixiang.com
Date: 2023-03-23 14:41:42
LastEditors: FF fengfan1@lixiang.com
LastEditTime: 2023-03-23 17:08:36
FilePath: \pythonlearning\learning\os\os_popen_demo.py
Description:

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
'''

import os

result = os.popen('cmd.exe')   #os.popen是非阻塞的

print("os.popen is ending")

for i in range(10):
    print(result.readline())   #read可以变成阻塞

#print(result.readlines())   #read可以变成阻塞

result.close()