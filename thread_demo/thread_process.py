import threading
import multiprocessing
import time
import random


def worker(id):
    print(f'Worker {id} started')
    t = random.randint(1, 5)
    time.sleep(t)
    print(f'Worker {id} finished in {t} seconds')


def third_thread_func():
    processes = []
    for i in range(1, 10):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


def second_thread_func():
    # Wait for start of third thread
    event.wait()

    # Start third thread
    t = threading.Thread(target=third_thread_func)
    t.start()
    t.join()


def first_thread_func():
    # Start second thread
    t = threading.Thread(target=second_thread_func)
    t.start()

    # Wait for start of second thread
    event.wait()

    # Start third thread after the second thread
    t = threading.Thread(target=third_thread_func)
    t.start()
    t.join()


if __name__ == '__main__':
    event = threading.Event()

    # Start the first thread
    t = threading.Thread(target=first_thread_func)
    t.start()

    # Signal the event to start the second thread
    event.set()

    # Join the first thread
    t.join()