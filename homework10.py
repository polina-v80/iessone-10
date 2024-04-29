def f(arg):
    # Печать переданного значения дважды
    print(arg)
    print(arg, end = '\n\n')

# Вызов функции несколько раз
f("Пример строки")
f(123)
f([1, 2, 3])

#
# def say_hello(name):# Принимающая функция, в момент создания которой мы определяем какое-то значение,
# она будут принимать,
#     print('Hello', name)
#
# say_hello('Anna')
# say_hello('s')
#


# import random
#
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win = random.choice(tickets)
#     return win #  возвращающая функция
#
# win = lottery() * lottery()
# # print(win)
#
# import random
# def lottery(mon, thue):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     win2 = random.choice(tickets)
#     print(mon, thue)
#     return win1, win2
#
# win1, win2 = lottery('mon', 'thue')
# print(win1, win2, end = '\n\n')
#
# import random
# def lottery(*args, **kwargs):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(*args)
#     return win1, win2
#
# win1, win2 = lottery(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(win1, win2)