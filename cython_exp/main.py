import os
import pyximport
from timeit import Timer
from random import shuffle

pyximport.install(reload_support=True, build_dir=os.path.join(os.getcwd(), '.pyxbld'), language_level=3)

import insertion_sort

if __name__ == "__main__":
    setup = """
random_list_of_nums = list(range(0, 10_000))
shuffle(random_list_of_nums)
"""

    print(min(Timer('insertion_sort.insertion_sort(random_list_of_nums)', setup=setup, globals=globals()).repeat(7, 1000)))

