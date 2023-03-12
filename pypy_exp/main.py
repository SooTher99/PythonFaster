from random import shuffle
from timeit import Timer


def insertion_sort(alist: list):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


if __name__ == '__main__':
    setup = """
random_list_of_nums = list(range(0, 10_000))
shuffle(random_list_of_nums)"""

    print(min(Timer('insertion_sort(random_list_of_nums)', setup=setup, globals=globals()).repeat(20, 1000)))
