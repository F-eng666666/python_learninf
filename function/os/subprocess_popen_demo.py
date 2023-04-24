'''
Author: FF fengfan1@lixiang.com
Date: 2023-03-23 15:40:00
LastEditors: FF fengfan1@lixiang.com
LastEditTime: 2023-03-23 15:47:47
FilePath: \pythonlearning\learning\os\subprocess_popen_demo.py
Description:

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
'''

import subprocess
import os

res = subprocess.Popen('cmd.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # 使用管道

#print (res.stdout.read())  # 标准输出

for line in iter(res.stdout.readline, b''):
    print (line)
    line = str(line.decode(encoding="gbk", errors='ignore').strip())
    print (line)
res.stdout.close()         # 关闭
