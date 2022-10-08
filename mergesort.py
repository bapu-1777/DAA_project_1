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


import time
numbers_files = [20, 100, 1000, 4000]




for n in numbers_files:
    data = []
    d_data = {}
    with open(f"arr{n}.txt", "r") as file1:
        file_datas = file1.readlines()
        for i in file_datas:
            row = i.split()
            sum_3=int(row[3])
            d_data[sum_3] = row[:3]
            data.append(sum_3)
    with open(f"Output_files_Merge_sort/arrMR_O_{n}.txt", "w") as file:
        start_time = time.time()
        data = merge_sort(data)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"time taken for {n} size arr using mergesort sort(in seconds) = {total_time}")
        for i in data:
            p = d_data[i]
            file.write(f"{p[0]} {p[1]} {p[2]}\t{i}\n")
