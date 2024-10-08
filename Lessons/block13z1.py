import time, asyncio
from datetime import datetime


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    downlow = 10 / power # base coefficient
    for i in range(1, 6):
        start_time_1 = datetime.now()
        await asyncio.sleep(downlow)
        print(f'Силач {name} поднял {i} шар')
        end_time_1 = datetime.now()
        delta_time = end_time_1 - start_time_1
        t1 = i*downlow # изменение коэфициэнта усталости
        downlow += t1/power # чем больше усталость тем долше поднимаем
        print(f"Время выполнения: {delta_time} секунд")

async def start_tournament():

    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Dasha', 5))
    task_3 = asyncio.create_task(start_strongman('Yasha', 9))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())