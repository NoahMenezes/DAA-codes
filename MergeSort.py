import time
import random
def show_cuts(arr, cuts):
    res = []
    for k, v in enumerate(arr):
        res.append(str(v))
        if k in sorted(cuts):
            res.append("|")
    print(" ".join(res))


def merge(arr, low, mid, high):
    temp = []
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    temp.extend(arr[i : mid + 1])
    temp.extend(arr[j : high + 1])
    arr[low : high + 1] = temp


def merge_sort(arr, low, high, cuts):
    if low >= high:
        return
    mid = (low + high) // 2
    cuts.add(mid)
    show_cuts(arr, cuts)

    merge_sort(arr, low, mid, cuts)
    merge_sort(arr, mid + 1, high, cuts)
    merge(arr, low, mid, high)

    cuts.discard(mid)
    show_cuts(arr, cuts)




arr=[random.randint(0,10000) for i in range(1,1000)]
start=time.time()
a_M = ['a', 'b','b','e','z','b']
print("Original Array:", "".join(a_M))
merge_sort(a_M, 0, len(a_M) - 1, set())
print("Final Sorted Array:", "".join(a_M))
end=time.time()
print(end-start)