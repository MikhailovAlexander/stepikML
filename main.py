import re


def step5():
    with open('data/ping.txt', 'r') as file:
        text = file.read()
    pattern = '(?<=время=)\d+'
    values = [int(value) for value in re.findall(pattern, text)]
    print(min(values), int(round(sum(values)/len(values), 0)), max(values))


def step6():
    text = """Shall I compare thee to a summer’s day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer’s lease hath all too short a date:
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimmed;
And every fair from fair sometime declines,
By chance, or nature’s changing course, untrimmed:
But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow’st;
Nor shall Death brag thou wander’st in his shade
When in eternal lines to time thou grow’st:
So long as men can breathe or  . eyes can see,
So long lives this, and this gives life to - thee. наконец-то. слов1-
 слово2 наконец-то ! слово - слово"""
    pattern = '[\.\?\!,-:;](\n|\s)|\s'
    words = [word.lower() for word in re.split(pattern, text) if word and not word.isspace()]
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    for word in sorted(freq_dict.keys()):
        print(f'{word}: {freq_dict[word]}')


def home_task_1():
    # n, k = map(int, input().split())
    n = 5
    k = 3
    if n < 3:
        print(1)
    prev = 0
    result = 1
    for i in range(1, n):
        result, prev = result + prev, result * k
    print(result)


def home_task_2():
    n = int(input())
    numbers = list(map(float, input().split()))
    if n == 1:
        print(numbers[0])
    else:
        means = [str(numbers[0])]
        for i in range(1, n - 1):
            mean = round(sum(numbers[i - 1:i + 2]) / 3, 10)
            mean = int(mean) if round(mean) == mean else mean
            means.append(str(mean))
        means.append(str(numbers[-1]))
        print(' '.join(means))

def get_fib_list(n):
    fib_list = [None, 1, 1]
    if n < 3:
        return fib_list[1: n + 1]
    for _ in range(n - 2):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[1:]


def home_task_3():
    n = int(input())
    m = int(input())
    rabbits_list = [1, 1]
    die_offset = m + 1
    for i in range(2, n):
        if i < m:
            rabbits_list.append(rabbits_list[-1] + rabbits_list[-2])
        elif i == m:
            rabbits_list.append(rabbits_list[-1] + rabbits_list[-2] - 1)
        else:
            rabbits_list.append(rabbits_list[-1] + rabbits_list[-2] -
                                rabbits_list[-die_offset])
    print(rabbits_list[-1])





"""
User avatar
Евгений Орлов
7 дней назад

Снова динамическое программирование. Как и в прошлый раз, для нахождения нового состояния, нужно знать два предыдущих. Новое состояние - их сумма. Но здесь должна быть корректировка из состояния неизвестной глубины m. Родившиеся тогда кролики, скончаются сейчас. Следовательно, необходимо помнить все состояния на глубину m.

Создаем список из m нулей. Последние два состояния известны - это 1. Записываем их в переменные текущих состояний a и b, а также в последние значения списка. Теперь, когда нужно будет узнать, сколько кроликов собирается помирать в этом месяце, поднимаем и удаляем первое значение из списка. А в конец списка допишем новое значение - сколько родилось кроликов в этом месяце. Оно равно числу кроликов в предыдущем. Образуется очередь (deque). 

Сложность алгоритма O(n), быстрый. Памяти займет тоже немного: m состояний. По хорошему, при больших вычислениях, стоило бы импортировать collections.deque. Если последний элемент положить в список O(1), то вытащить первый - O(n). В deque такого не будет. O(1) с обеих сторон. Но кролики столько не живут :)

def din_fib(n, m):
    lst = [0] * m
    a = lst[-2] = lst[-1] = b = 1
    for i in range(2, n):
        a, b = b, a + b - lst.pop(0)
        lst.append(a)
    return b
"""
"""
import csv

with open('data/titanic_train_simplified.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader.__next__()
    age_sum = 0.
    age_cnt = 0
    classes = [None, 0, 0, 0]
    for row in reader:
        if row[2]:
            classes[int(row[2])] = classes[int(row[2])] + 1
        if row[5]:
            age_sum += float(row[5])
            age_cnt += 1
    print(round(age_sum / age_cnt))
    print(classes)
"""

"""
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
"""

"""
def is_perfect(n):
    factors = []
    for i in range(1, n - 1):
        if n % i == 0:
            factors.append(i)
    return sum(factors) == n
"""
"""
def gen_fib(n):
    numbers = [1, 1]
    for _ in range(2, n):
        numbers.append(numbers[-1] + numbers[-2])
    return numbers
"""
"""
import random as rnd

def play_game(change_choice: bool):
    doors = [1, 2, 3]
    win_door = rnd.choice(doors)
    first_choice = rnd.choice(doors)
    if not change_choice:
        return int(first_choice == win_door)
    monty_choice = rnd.choice([door for door in doors
                               if door != win_door and door != first_choice])
    changed_choice = 6 - first_choice - monty_choice
    return int(changed_choice == win_door)

change_choice = bool(input() != 'No')
games_cnt = 100000
result = 0
for _ in range(games_cnt):
    result += play_game(change_choice)
print(round(result/games_cnt, 2))
"""
"""
def _get_primes(n):
    primes = []
    for i in range(2, n + 1):
        if not any([j for j in range(2, i) if i % j == 0]):
            primes.append(i)
    return primes

n = int(input())
primes = [i for i in range(2, n + 1)
          if not any([j for j in range(2, i) if i % j == 0])]
print(int(sum(primes) * 100/len(primes) + 0.5)/100)
"""

"""
import requests

url = "https://raw.githubusercontent.com/bykov-alexei/data-science-course/master/Python3/earthquakes.csv"
r = requests.get(url)
max_val = 0.
max_date = ''
for row in r.text.splitlines():
    date, val = row.split(',')
    try:
        if float(val) > max_val:
            max_val = float(val)
            max_date = date
    except Exception as ex:
        print('parse error: ' + str(ex))

print(max_date, max_val)
"""
"""
import pandas as pd

url = 'https://raw.githubusercontent.com/bykov-alexei/data-science-course/master/Python3/moscow%20schools%20-%20winners.csv'

df = pd.read_csv(url)
print(df[df['magnitude'] == df['magnitude'].max()].index[0])
"""

"""
import numpy as np

n = int(input())
matrix = np.zeros((n, n))
for row in matrix:
    row[n - 1] = 1
    print(*map(int, row), end=' \n')
    n -= 1
"""

import pandas as pd

dt = pd.to_datetime(input())
print(dt)
