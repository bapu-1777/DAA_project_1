def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    l = arr[:mid]
    r = arr[mid:]

    merge_sort(l)
    merge_sort(r)

    merge_two_list(l, r, arr)

    return arr

def merge_two_list(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

import random

numbers_files = [20, 100, 1000, 4000]




for n in numbers_files:
    data = []
    d_data = {}
    with open(f"arr{str(n)}.txt", "w") as file1:
        for i in range(n):
            randomlist = random.sample(range(1, 999), 3)
            last_e = sum(randomlist)
            d_data[last_e] = randomlist
            data.append(last_e)
            file1.write(f"{randomlist[0]} {randomlist[1]} {randomlist[2]}\t{last_e}\n")

    with open(f"Output_files_Merge_sort/arrMR_O_{n}.txt", "w") as file:
        for i in merge_sort(data):
            p = d_data[i]
            file.write(f"{p[0]} {p[1]} {p[2]}\t{i}\n")