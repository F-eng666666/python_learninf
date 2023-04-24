import subprocess
import threading
import time
import queue

def run_cmd(cmd, timeout):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def target(my_queue,error_flag):
        while proc.poll() is None:
            line = proc.stdout.readline()
            if line:
                print(line.decode('utf-8'))
                output.append(line.decode('utf-8'))
                if any(item in line.decode('utf-8') for item in error_flag):
                    my_queue.put('error')
                    break
            else:
                time.sleep(0.1)

    output = []
    time_counter = 0
    my_queue = queue.Queue(maxsize=10)
    error_flag = ['erroddr','faild']
    thread = threading.Thread(target=target,args = (my_queue,error_flag))
    thread.start()


    while proc.poll() is None:
        time.sleep(1)
        time_counter= time_counter+1
        if not my_queue.empty():
            print('5555555555555555')
            proc.kill()
            return False
        if time_counter >= timeout:
            print('33333333333333333333')
            proc.kill()
            return False

    """try:
        thread.join(timeout)
        print('111111111111111111111')
    except:
        proc.kill()
        thread.join()
        print('22222222222222222222')
    print('333333333333333333333')"""

    return output

    return {'stdout': proc.stdout.read().decode('utf-8'), 'stderr': proc.stderr.read().decode('utf-8')}

if __name__=='__main__':
    ret = run_cmd('cmd.exe', 100)
    """for line in ret['stdout'].split('\r\n'):
        print(line.strip())"""
    print(ret)
    print("fffffffffffffff")