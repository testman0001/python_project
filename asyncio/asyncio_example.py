# 简单示例，使用事件循环驱动协程函数
import asyncio


async def coro1():
    print("coroutine1 start")
    await asyncio.sleep(1)
    print("coroutine1 end")


async def coro2():
    print("coroutine2 start")
    await asyncio.sleep(1)
    print("coroutine2 end")


async def main():
    print("main start")
    # 添加两个协程，并发执行
    await asyncio.gather(coro1(), coro2())
    print("main end")


if __name__ == '__main__':
    # 创建事件循环
    loop = asyncio.get_event_loop()
    # 驱动执行协程函数（main函数），并阻塞主线程，执行完后退出
    loop.run_until_complete(main())
    print("exit")