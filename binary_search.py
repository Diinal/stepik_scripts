def search(array, k):
    l = 1
    r = len(array)
    while l <= r:
        m = (l+r) // 2
        print(l, r, m)
        if m == len(array):
            return -1
        if array[m] == k:
            return m + 1
        elif array[m] > k:
            r = m - 1
        else:
            l = m + 1
    return -1

array = [1, 5, 8, 12, 13]
k = 1
print(search(array, k))