import socket

serverSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
# socket.AF_INET：指定通过IPV4进行连接
# socket.SOCK_DGRAM: 通过udp进行通信
serverSocket.bind(('10.245.16.39',9997))
# 使用UDP协议进行socket通信，服务器不需要进行监听
while True:
    data , addr = serverSocket.recvfrom(1024)
    print('接收到客户端的信息：',data)
    print('客户端的地址为:',addr)
    recvdata = input('server >>').encode('utf-8')
    serverSocket.sendto(recvdata,addr)