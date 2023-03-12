import numba as nb
import numpy as np
from timeit import Timer


@nb.njit
def insertion_sort(alist: np.ndarray):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


@nb.njit
def get_shuffled_array(amount: int) -> np.ndarray:
    random_list_of_nums = np.arange(0, amount, dtype=np.int16)
    np.random.shuffle(random_list_of_nums)
    return random_list_of_nums


if __name__ == '__main__':
    setup = """
random_list_of_nums = np.arange(0, 100_000, dtype=np.int16)
np.random.shuffle(random_list_of_nums)
"""
    setup2 = """
random_list_of_nums = get_shuffled_array(100_000)
"""

    print(min(Timer('insertion_sort(random_list_of_nums)', setup=setup, globals=globals()).repeat(7, 1000)))
