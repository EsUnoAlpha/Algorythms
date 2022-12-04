"""Сложность: О(n)
Алгоритм ищет совпадения в строках и прибавляет единицу если найдено совпадение"""

def jewelry(jewels, stones):
    counter = 0 #Вводится счетчик
    for i in jewels: #Поиск в первом списке
        for n in stones: #Поиск во втором списке
            if i == n:
                counter += 1
    return counter

print(jewelry('z', 'ZZ'))

