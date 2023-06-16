import threading

count = 0

def increment():
    global count
    for i in range(1000000):
        count += 1

def decrement():
    global count
    for i in range(1000000):
        count -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=decrement)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Final count: {count}")
