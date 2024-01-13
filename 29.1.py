import asyncio
import time

start = time.time()
async def task1():
    print('Початок...')
    await asyncio.sleep(3)
    print('...Завершення')

async def task2():
    print('Новий Початок...')
    await asyncio.sleep(2)
    print('...Нове завершення')

async def task3():
    print('Останiй початок...')
    await asyncio.sleep(1)
    print('...Останне завершення')

async def main():
    await asyncio.gather(
        task1(),
        task2(),
        task3()
    )

asyncio.run(main())

end = time.time() - start
print(end)