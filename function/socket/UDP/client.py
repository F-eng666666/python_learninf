import socket
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg = input('client >>:')
    msg = msg.encode()
    clientSocket.sendto(msg,('10.245.16.39',9997))
    print('接收到客户端的消息为:',clientSocket.recv(1024))