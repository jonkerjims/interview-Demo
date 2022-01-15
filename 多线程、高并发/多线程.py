import threading
import time


def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")


def T2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():
    # 实例化一个线程
    added_thread = threading.Thread(target=thread_job,name='T1')
    thread2 = threading.Thread(target=T2_job,name='T2')
    # 开启线程
    added_thread.start()
    thread2.start()
    # 开启线程等待
    added_thread.join()

    print('all Done\n')
    # print(threading.active_count()) # 查看当前开启的线程数
    # print(threading.enumerate()) # 查看当先开启的线程有哪些
    # print(threading.current_thread()) # 查看当前程序运行的线程


if __name__ == '__main__':
    main()