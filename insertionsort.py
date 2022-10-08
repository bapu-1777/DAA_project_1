def insertionsort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


import random
import time
random.seed(3)
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



    with open(f"Output_files_Insertion_sort/arrIS_O_{n}.txt", "w") as file:
        start_time = time.time()
        data = insertionsort(data)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"time taken for {n} size arr using insertion sort(in seconds) = {total_time}")
        for i in data:
            p = d_data[i]
            file.write(f"{p[0]} {p[1]} {p[2]}\t{i}\n")




