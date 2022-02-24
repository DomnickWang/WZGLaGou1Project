#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/2/24 09:52
# @Author: WZG
# @File: tmp.py
import threading
import time


def task1():
    print("扔第二个苹果")
    time.sleep(5)


def task2():
    print("扔第三个苹果")
    time.sleep(5)


def main():
    # 开始时间
    start_time = time.time()
    # 第一个线程
    print("扔第一个苹果")
    # threading.Thread()创建了第二个线程和第三个线程
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    # 让线程执行，添加 .join()让其他线程等待自己执行完成
    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()
    # 结束时间
    end_time = time.time()
    print("总耗时： ", end_time - start_time)


if __name__ == "__main__":
    main()
