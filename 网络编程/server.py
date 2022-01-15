# -*- coding: utf-8 -*-
import socket  # 导入 socket 模块
import threading

con = threading.Condition() # 判断条件 锁 线程同步
host = '192.168.123.204'
port = 8888
data = ''


def NotifyAll(sss):  # 保证接受的原子性
    global data
    if con.acquire(): # 获取锁/设置锁
        data = sss
        con.notifyAll() # 表示当前线程放弃对资源的占有，通知其他线程
        con.release() # 释放锁


def threadOut(conn,nick): # 发送消息
    global data
    while True:
        if con.acquire(): # 加锁
            con.wait() # 会阻塞在这里 放弃对当前资源的占用 等待消息通知
            if data:
                try:
                    conn.send(data.encode('utf8'))
                    con.release()
                except:
                    con.release()
                    return


def threadIn(conn,nick): # 接收消息
    while True:
        try:
            temp = conn.recv(1024).decode('utf8')
            if not temp:
                conn.close()
                return
            NotifyAll(temp)
            print(data)
        except:
            NotifyAll(nick+',离开了房间~')
            print(data)
            return



if __name__ == '__main__':
    # host = input('输入被连接服务器IP：')

    s = socket.socket() # 建立Socket连接
    print("Socket created~")
    s.bind((host,port)) # 绑定端口
    s.listen(5) # 监听连接

    print('Socket new listening')

    while True:
        conn,addr = s.accept() # 接受到连接了
        print('Connected with '+addr[0]+':'+str(addr[1]))
        nick = conn.recv(1024).decode('utf8')
        NotifyAll('\n欢迎'+nick+'进入760聊天室！')
        print(data)
        conn.send(data.encode('utf8'))
        threading.Thread(target=threadOut,args=(conn,nick)).start()
        threading.Thread(target=threadIn,args=(conn,nick)).start()


