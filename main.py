#!/usr/bin/env python
# -*- coding:utf-8 -*-
from core.spidercore import Core


import time

def main():
    # 1. 定时发送请求
    engine = Core()
    while True:
        engine.start()
        time.sleep(3)



if __name__ == "__main__":
    main()