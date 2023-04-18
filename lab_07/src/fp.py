import numpy as np
from typing import List , Tuple


# Лекция 8, стр. 20 (вместо 1 должны быть 10 как в табличках выше)
COEFS = np.array([
    [3,  4,  6],
    [4,  5,  7],
    [3,  4,  6],
    [7, 10, 15],
    [5,  7, 10],
])

# Лекция 8, стр. 40
LANGUAGES = np.array([
    320, 128, 106, 106,
    90, 64, 53, 53,
    49, 32, 34, 18,
    21, 54, 13, 56 
])


def calculateFP(func_types_matrix: List[List[int]]) -> Tuple[List[int], int]:
    func_types_matrix = np.array(func_types_matrix)

    product = COEFS * func_types_matrix
    sums = np.sum(product, 1)

    return sums.tolist(), np.sum(sums)


def adjustFP(fp: int, complexity_ratios: List[int]) -> float:
    # Скорректированное количество функциональных точек
    # Лекция 8, стр. 23
    vaf = 0.65 + 0.01 * sum(complexity_ratios)

    return fp * vaf


def getLocByFP(fp: float, language_percentage: List[float]) -> float:
    language_percentage = np.array(language_percentage) / 100
    fps_by_language = fp * language_percentage

    return int(round(np.sum(fps_by_language * LANGUAGES)))
