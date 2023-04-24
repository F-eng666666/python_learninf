import socket

HOST  = '10.245.16.39'
PORT = 50007
s =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #定义socket类型，网络通信，TCP
s.bind((HOST,PORT))    #套接字绑定的IP与端口
s.listen(5)          #开始TCP监听
while True:
        conn,addr = s.accept()    #接受TCP连接，并返回新的套接字与IP地址
        print ('Connected by')     #输出客户端的IP地址
        data = conn.recv( 1024 )     #把接收的数据实例化
        print(data)
conn.close()      #关闭连接