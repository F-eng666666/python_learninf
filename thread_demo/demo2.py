import multiprocessing
import threading
import time

def process_func(queue):
    for i in range(3):
        # 进程需要发送的消息
        msg = f"Message from process {i}"
        queue.put(msg)
        time.sleep(1)

def thread1_func(queue):
    while True:
        if not queue.empty():
            msg = queue.get()
            print(f"Thread 1: {msg}")
        time.sleep(1)

def thread2_func(queue):
    while True:
        if not queue.empty():
            msg = queue.get()
            print(f"Thread 2: {msg}")
        time.sleep(1)

def thread3_func(queue):
    # 创建9个进程
    processes = []
    for i in range(9):
        process = multiprocessing.Process(target=process_func, args=(queue,))
        processes.append(process)
        process.start()
    # 等待所有进程结束
    for process in processes:
        process.join()

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    thread1 = threading.Thread(target=thread1_func, args=(queue,))
    thread2 = threading.Thread(target=thread2_func, args=(queue,))
    thread3 = threading.Thread(target=thread3_func, args=(queue,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()