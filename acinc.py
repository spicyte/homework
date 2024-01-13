import asyncio

async def funct(car):
    print("Начало выполнения функции" + car)
    await asyncio.sleep(2)
    print("Функция завершилась")

async def main():
    await asyncio.gather(
        funct(car='impala'),
    )
asyncio.run(main())
    