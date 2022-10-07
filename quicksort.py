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


    with open(f"Output_files_Quick_sort/arrQK_O_{n}.txt", "w") as file:
        for i in quick_sort(data,0,len(data)-1):
            p = d_data[i]
            file.write(f"{p[0]} {p[1]} {p[2]}\t{i}\n")
