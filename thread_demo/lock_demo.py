import threading

lock = threading.Lock()

x=0
y=0

# 线程1的任务函数
def task1():
    lock.acquire()
    # 临界区操作，访问共享数据
    x=1
    y=0
    lock.release()

# 线程2的任务函数
def task2():
    lock.acquire()
    # 临界区操作，访问共享数据
    x=0
    y=1
    lock.release()

# 启动线程1和线程2
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()