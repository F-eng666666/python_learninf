import sys
import time
 
"""
可以看到,我们通过指定stderr=subprocess.,
可以直接从标准输出中同时获取标准输出和标准错误的信息。
运行这个程序,我们会期待main.py会每秒输出一次信息到控制台,
但是事实上,我们直到等了10秒之后才一次性看到所有的10条输出。
产生这种现象的原因也非常简单，就是标准输出和标准错误有
一个缓存的概念，它不会立即将程序的标准输出内容返回，
而是会做一定的缓存，直到缓存满或者程序结束强制清空缓存时才输出。
了解到问题的原因，解决问题的方法也就一目了然了，我们只需要在子程序中，
每次输出后去手动清空一下缓存即可，
"""
for i in range(5):
    sys.stdout.write('Processing {}\n'.format(i))
    sys.stdout.flush()    #手动清空一下缓存
    time.sleep(1)
 
for i in range(5):
    sys.stderr.write('Error {}\n'.format(i))
    sys.stderr.flush()
    time.sleep(1)