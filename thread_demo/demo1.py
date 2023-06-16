
import multiprocessing
import threading
import mmap
import os

def read_file(filename, file_lock, thread_lock):
    with file_lock:
        with open(filename, 'r') as f:
            content = f.read()
            with thread_lock:
                print(f"[Thread {threading.currentThread().name}] Read content from file: {content}")
        return content

def write_file(filename, content, file_lock, thread_lock):
    with file_lock:
        with open(filename, 'w') as f:
            f.write(content)
            with thread_lock:
                print(f"[Thread {threading.currentThread().name}] Wrote content to file: {content}")

if __name__ == '__main__':
    filename = 'test.txt'
    content = 'Hello World!'

    # 创建一个进程锁和一个线程锁
    file_lock = multiprocessing.Lock()
    thread_lock = threading.Lock()

    # 创建两个线程同时读写文件
    t1 = threading.Thread(target=read_file, args=(filename, file_lock, thread_lock))
    t2 = threading.Thread(target=write_file, args=(filename, content, file_lock, thread_lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()