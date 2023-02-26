import os
import pyximport

pyximport.install(reload_support=True, build_dir=os.path.join(os.getcwd(), '.pyxbld'), language_level=3)

from random import shuffle
import insertion_sort

if __name__ == "__main__":
    random_list_of_nums = list(range(0, 10000))
    shuffle(random_list_of_nums)
    insertion_sort.insertion_sort(random_list_of_nums)
