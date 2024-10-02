"""
Задача "Асинхронные силачи":

Необходимо сделать имитацию соревнований по поднятию шаров Атласа.

Напишите асинхронную функцию start_strongman(name, power), где name - имя силача,
power - его подъёмная мощность. Реализуйте следующую логику в функции:

В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' с задержкой
обратно пропорциональной его силе power. Для каждого участника количество шаров одинаковое - 5.
В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'

Также напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций
start_strongman. Имена(name) и силу(power) для вызовов функции start_strongman можете
выбрать самостоятельно.
После поставьте каждую задачу в ожидание (await).
Запустите асинхронную функцию start_tournament методом run.

Пример результата выполнения программы:
Переданные аргументы в функции start_strongman:
'Pasha', 3
'Denis', 4
'Apollon', 5

Вывод на консоль:

Силач Pasha начал соревнования
Силач Denis начал соревнования
Силач Apollon начал соревнования
Силач Apollon поднял 1 шар
Силач Denis поднял 1 шар
Силач Pasha поднял 1 шар
Силач Apollon поднял 2 шар
Силач Denis поднял 2 шар
Силач Apollon поднял 3 шар
Силач Pasha поднял 2 шар
Силач Denis поднял 3 шар
Силач Apollon поднял 4 шар
Силач Pasha поднял 3 шар
Силач Apollon поднял 5 шар
Силач Apollon закончил соревнования
Силач Denis поднял 4 шар
Силач Denis поднял 5 шар
Силач Denis закончил соревнования
Силач Pasha поднял 4 шар
Силач Pasha поднял 5 шар
Силач Pasha закончил соревнования
Примечания:
Для обозначения асинхронной функции используйте оператор async.
Для постановки задачи в режим ожидания используйте оператор await.
Для задержки в асинхронной функции используйте функцию sleep из пакета asyncio.
Для запуска асинхронной функции используйте функцию run из пакета asyncio.

"""

import asyncio


async def start_strongman(name, power):
    ball_num = 1
    print(f"Силач {name} начал соревнования.")
    while ball_num <= 5:
        await asyncio.sleep(2/power)
        print(f"Силач {name} поднял {ball_num} шар")
        ball_num += 1
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    strongman_1 = start_strongman('Pasha', 3)
    strongman_2 = start_strongman('Denis', 4)
    strongman_3 = start_strongman("Apollon", 5)
    task_1 = asyncio.create_task(strongman_1)
    task_2 = asyncio.create_task(strongman_2)
    task_3 = asyncio.create_task(strongman_3)
    await task_1
    await task_2
    await task_3


if __name__ == '__main__':
    asyncio.run(start_tournament())
