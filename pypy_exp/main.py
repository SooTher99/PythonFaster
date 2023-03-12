from random import shuffle


def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


if __name__ == '__main__':
    random_list_of_nums = list(range(0, 10000))
    shuffle(random_list_of_nums)
    insertion_sort(random_list_of_nums)
