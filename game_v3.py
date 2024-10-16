"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(secret_number: int = 1) -> int:
    """
    Функция угадывает загаданное число secret_number с помощью бинарного поиска.
    Аргументы:
        secret_number (int): загаданное число, которое нужно угадать. По умолчанию - 1

    Возвращает:
        attempts (int): количество затраченных попыток для угадывания загаданного числа
    """

    # по условию - диапазон загаданного числа от 1 до 100
    low = 1
    high = 100
    attempts = 0  # Счетчик попыток

    while low <= high:
        attempts += 1
        guess = (low + high) // 2 # Возможное загаданное число - середина диапазона

        if guess == secret_number: # отлично, нашли загаданное число, выход из цикла
            break
        elif guess < secret_number: # загаданное число больше, добавляем значение к нижней границе
            low = guess + 1
        else:
            high = guess - 1

    return attempts # Возвращаем количество попыток


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == '__main__':
    score_game(random_predict)