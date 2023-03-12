import os
import pyximport
from timeit import timeit
from random import shuffle

pyximport.install(reload_support=True, build_dir=os.path.join(os.getcwd(), '.pyxbld'), language_level=3)

import insertion_sort

if __name__ == "__main__":
    random_list_of_nums = list(range(0, 10_000))
    shuffle(random_list_of_nums)

    print(timeit('insertion_sort.insertion_sort(random_list_of_nums)', globals=globals(), number=1))


