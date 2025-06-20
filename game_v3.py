"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число
    Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
    Алгоритм оптимизирован: на каждом шаге диапазон, в котором присутствует 
    рандомное число сужается.
       Функция принимает загаданное число и возвращает число попыток 
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Число попыток
    
    # Границы искотого числа
    min_num = 1  # Нижняя граница 
    max_num = 101 # Верхняя граница

    while True:
        count += 1
        predict_number = np.random.randint(min_num, max_num)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number: # Сужаем диапазон снизу
            min_num = predict_number + 1
        else:
            max_num = predict_number # Сужаем диапазон верху
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
