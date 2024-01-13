import asyncio
import time

start = time.time()
async def funct(car):
    print("Начало выполнения функции" + car)
    await asyncio.sleep(5)
    print("Функция завершилась")

async def main():
    await asyncio.gather(
        funct(car='impala'),
    )
asyncio.run(main())

end = time.time() - start

print(end)