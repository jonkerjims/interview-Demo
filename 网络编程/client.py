# -*- coding: utf-8 -*-
import socket  # 导入 socket 模块
import threading
import time

outString = "" # 发送的消息
nick = "" # 昵称
inString = "" # 接收的消息

def client_send(sock):
    global outString
    while True: # 一直监听输入
        outString = input('>>>') # 接受输入
        outString = nick + ":  " + outString
        sock.send(outString.encode('utf8'))

def client_accept(sock):
    global inString
    while True:
        try:
            inString = sock.recv(1024).decode('utf8') # 接收数据一次最多接收1024字节
            if not inString:
                break
            if outString != inString:
                print(inString)
        except:
            print('服务器连接失败~')
            # break

if __name__ == '__main__':
    nick = input("输入你的姓名：")
    # ip = input("输入服务器IP：")
    ip = '192.168.123.204'
    port = 8888
    sock = socket.socket()
    sock.connect((ip,port))

    sock.send(nick.encode('utf8'))
    th_accept = threading.Thread(target=client_accept, args=(sock,)).start()
    time.sleep(1)
    th_send = threading.Thread(target=client_send,args=(sock,)).start()


