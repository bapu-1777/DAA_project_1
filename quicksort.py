def right_place(arr,s,e):
    a=arr[e]
    i=s-1
    for j in range(s,e):
        if arr[j]<=a:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[e]=arr[e],arr[i+1]
    return i+1
def quick_sort(arr,s,e):
    if s<e:
        m=right_place(arr,s,e)
        quick_sort(arr,s,m-1)
        quick_sort(arr,m+1,e)

    return arr

import time
numbers_files = [20, 100, 1000, 4000]





for n in numbers_files:
    data = []
    d_data = {}

    with open(f"arr{n}.txt", "r") as file1:
        file_datas = file1.readlines()
        for i in file_datas:
            row = i.split()
            sum_3 = int(row[3])
            d_data[sum_3] = row[:3]
            data.append(sum_3)

    with open(f"Output_files_Quick_sort/arrQK_O_{n}.txt", "w") as file:

        start_time = time.time()
        data = quick_sort(data,0,len(data)-1)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"time taken for {n} size arr using quick sort(in seconds) = {total_time}")

        for i in data:
            p = d_data[i]
            file.write(f"{p[0]} {p[1]} {p[2]}\t{i}\n")
