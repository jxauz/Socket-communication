import socket

# 创建服务端socket对象
# 前一个参数表示网络地址类型，此处为IPV4；后一个参数为套接字类型，此处为tcp协议套接字
Object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Object.connect(("10.100.9.202", 10096))
while True:
    sdate = input("请输入：")
    if not sdate:
        continue
    Object.send(sdate.encode('utf-8'))
    rdate = Object.recv(1024)
    print(rdate.decode('utf-8'))
Object.close()
