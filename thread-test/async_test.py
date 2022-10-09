#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   async_test.py
@Time    :   2022/05/08 14:18:38
@Author  :   boyi.zhang 
@Version :   1.0
@Contact :   boyi.zhang@shopee.com
@License :   (C)Copyright 2020-2022, ZhangBoyi
@Desc    :   None
'''

# here put the import lib

import asyncio
import random
import time
from utils.decorate import load_time

@load_time
async def func(i: int) -> int:
    # print(f'now excuting func with {3-i} seconds sleep')
    # 用asyncio.sleep来模拟I/O操作
    sleep_time = random.randint(0,4)
    await asyncio.sleep(sleep_time)
    print(f'func with {sleep_time} seconds sleep finished!')
    return i

@load_time
async def main() -> None:
    # 根据不同参数构建任务
    tasks = (func(i) for i in range(100))
    # 多个任务共同提交至事件循环，并发执行
    res = await asyncio.gather(*tasks)
    return res

if __name__ == "__main__":
    t1 = time.perf_counter()
    print(t1)
    res = asyncio.run(main())
    print(f'actual excution time is {time.perf_counter()-t1}')
    res
