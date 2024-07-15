import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def time_sorts():
    lengths = [10, 100, 1000, 10000, 100000]
    results = []

    for length in lengths:
        arr = [random.randint(0, 100000) for _ in range(length)]
        arr_copy1 = arr.copy()
        arr_copy2 = arr.copy()
        arr_copy3 = arr.copy()

        merge_time = timeit.timeit(lambda: merge_sort(arr_copy1), number=1)
        insertion_time = timeit.timeit(lambda: insertion_sort(arr_copy2), number=1)
        timsort_time = timeit.timeit(lambda: sorted(arr_copy3), number=1)

        results.append((length, merge_time, insertion_time, timsort_time))

    return results

results = time_sorts()
for length, merge_time, insertion_time, timsort_time in results:
    print(f"Array Length: {length}")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    print(f"Timsort Time: {timsort_time:.6f} seconds\n")
