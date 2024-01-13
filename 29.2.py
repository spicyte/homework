import asyncio
import time

# третя

async def task1():
    print("Початок...")
    await asyncio.sleep(10)
    print("...Завершення")

# друга у черзi
    
async def task2():
    print("Новий початок....")
    await asyncio.sleep(5)
    print("...Нове завершення")

# виконуэться першою

async def task3():
    print("Останнiй початок...")
    await asyncio.sleep(2)
    print("...останне завершення")

async def main():
    await asyncio.gather(
        task1(),
        task2(),
        task3()
    )

asyncio.run(main())


