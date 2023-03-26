# 服务端
import socket

# 创建服务端socket对象
# 前一个参数表示网络地址类型，此处为IPV4；后一个参数为套接字类型，此处为tcp协议套接字
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定自己的ip及端口号（动态端口号1024~65535）
# bind()参数为元组(ip,port)
# sever.bind(("10.100.15.0", 10098))
sever.bind(("10.100.9.202", 10096))

# 设置监听模式，设置最大连接数
sever.listen(5)

# 等待连接 accept()返回两个值：socket对象，连接的客户端的IP地址及端口号
sever1, address = sever.accept()

while True:
    try:
        # 接受，发送 数据
        rdate = sever1.recv(1024)
        print(rdate.decode('utf-8'))
        sdate = input('请输入数据：')
        sever1.send(sdate.encode("utf-8"))
    except ConnectionError:
        break
# 关闭连接
sever1.close()
sever.close()
