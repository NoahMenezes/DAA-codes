
def MinMax(a, low, high):
    if low == high:
        print("Single element:", a[low])
        return a[low], a[low]
    if high == low + 1:

        if a[low] < a[high]:
            minimum = a[low]
            maximum = a[high]
        else:
            minimum = a[high]
            maximum = a[low]
        print("Compare:", a[low], a[high])
        print("Min =", minimum, "Max =", maximum)
        return minimum, maximum
    mid = (low + high) // 2

    print("Partition:", a[low:mid + 1], "|", a[mid + 1:high + 1])
    min1, max1 = MinMax(a, low, mid)
    min2, max2 = MinMax(a, mid + 1, high)
    minimum = min(min1, min2)
    maximum = max(max1, max2)
    print("Combine:", a[low:high + 1])
    print("Min =", minimum, "Max =", maximum)
    return minimum, maximum


a = [-96, 55,76, -87, 71, -91, 64,16, 63, 3]

print("Original Array:", *a)
minimum, maximum = MinMax(a, 0, len(a) - 1)
print("Final Minimum:", minimum)
print("Final Maximum:", maximum)
