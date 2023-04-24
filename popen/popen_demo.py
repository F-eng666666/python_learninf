import subprocess

cmd = "ping www.baidu.com -w 5"
pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1)

# 实时打印log
def print_log():
    # 当info为b''时停止
    for info in iter(pipe.stdout.readline, b''):
        print(info)
def print_log_1():
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        print (line)
    p.stdout.close()
    p.wait()

#print_log()
print_log_1()
