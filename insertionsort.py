"""
First part of code
In every ".py" file function is for sorting algorithm
Here,
Only one function is the insertion sort
start function
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


"""
end function
"""

import random  # for random integer
import time  # for calculate time

# random.seed(3) if its
numbers_files = [20, 100, 1000, 4000] # given in project question

for n in numbers_files:  # run loop number of files(4) times

    data = [] # to store sum random variable
    d_data = {} # data in key, value pair like key:'123' = value: ['100','20','3']

    """
    the following whole thing is to insert random data into a txt file and also in variable
    """
    with open(f"arr{str(n)}.txt", "w") as file1:
        for i in range(n):
            randomlist = random.sample(range(0, 99), 3)
            last_e = sum(randomlist)
            d_data[last_e] = randomlist
            data.append(last_e)
            file1.write(f"{randomlist[0]} {randomlist[1]} {randomlist[2]}   {last_e}\n")

    """
    in this part, call insertion sort function and generate output txt and calculate time unit 
    """
    with open(f"Output_files_Insertion_sort/arrIS_O_{n}.txt", "w") as file:
        start_time = time.time()
        data = insertion_sort(data)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"time taken for {n} size arr using insertion sort(in seconds) = {total_time}") # time
        for i in data:
            p = d_data[i]
            file.write(f"{p[0]} {p[1]} {p[2]}  {i}\n")
