#cython: language_level=3
#distutils: extra_compile_args=-fopenmp
#distutils: extra_link_args=-fopenmp
import cython


@cython.boundscheck(False)
@cython.cdivision(True)
@cython.wraparound(False)
cpdef insertion_sort(list nums):
    cdef int item_to_insert
    cdef int j
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
