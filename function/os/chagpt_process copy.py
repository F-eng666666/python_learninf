import subprocess
import threading
import time
import os

lock = threading.Lock()
def run_cmd(cmd, timeout):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def target():
        while proc.poll() is None:
            lock.acquire()   # 加锁
            line = proc.stdout.readline()
            lock.release()   # 解锁
            if line:
                print(line.decode('utf-8'))
                output.append(line.decode('utf-8'))
            else:
                time.sleep(0.1)

    output = []
    thread = threading.Thread(target=target)
    thread.start()

    try:
        print('111111111111111111111')
        stdout, stderr = proc.communicate(timeout=timeout)

        return {'stdout': stdout.decode(), 'stderr': stderr.decode(), 'returncode': proc.returncode}
    except:
        proc.kill()
        print('22222222222222222222')
    print('333333333333333333333')

    return output


if __name__=='__main__':
    ret = run_cmd('cmd.exe', 100)
    """for line in ret['stdout'].split('\r\n'):
        print(line.strip())"""
    print(ret)
    print("fffffffffffffff")