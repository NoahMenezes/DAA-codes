
import time
import random

def partition(a, m, p):

    v = a[m]

    i = m + 1
    j = p

    while True:

        while i <= p and a[i] >= v:
            i += 1

        while j >= m + 1 and a[j] <= v:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]

        else:
            break

    a[m], a[j] = a[j], a[m]

    return j


def quick_sort(a, p, q):

    if p < q:

        j = partition(a, p, q)

        quick_sort(a, p, j - 1)
        quick_sort(a, j + 1, q)


# Normal example
a = [94, 987, 495, 200, 765, 540, 182, 755, 209, 341, 517]

print("Original Array:", *a)

quick_sort(a, 0, len(a) - 1)

print("Final Sorted Array:", *a)


# Benchmark
arr = [random.randint(1, 10000) for i in range(1000)]

start = time.time()

quick_sort(arr, 0, len(arr) - 1)

end = time.time()

print("Quick Sort Time:", end - start)

