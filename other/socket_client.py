#!/usr/bin/python3
# coding: utf-8

import socket

# 1. 创建socket
socket = socket.socket()

# 2. 连接服务器
socket.connect(('192.168.43.15', 8019))
#socket.send('connect')

# 3. 接收数据
msg = socket.recv(4096)  # 阻塞
print('Server： ', msg.decode('utf-8'))

# 4. 向服务端发送数据
socket.send('您好, 我想听首张学友的歌!'.encode('utf-8'))

# 关闭
socket.close()
