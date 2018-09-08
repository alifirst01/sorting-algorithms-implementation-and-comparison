import random as rd
import time

def Merge(list1, list2):
    res = []
    j, k = 0, 0
    size = len(list1) + len(list2)
    for i in range(size):
        if k >= len(list2):
            res.append(list1[j])
            j += 1
        elif j >= len(list1):
            res.append(list2[k])
            k += 1
        elif list1[j] > list2[k]:
            res.append(list2[k])
            k += 1
        else:
            res.append(list1[j])
            j += 1
    return res


def MergeRecursive(data):
    if len(data) <= 1:
        return data
    else:
        mid = int(len(data) / 2)
        list1 = MergeRecursive(data[:mid])
        list2 = MergeRecursive(data[mid:])
        return Merge(list1, list2)


def partition(data, start, e):
    pivot = data[e]
    i = start - 1
    j = start
    while j < e:
        if data[j] < pivot:
            i += 1
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
        j += 1
    temp = data[i + 1]
    data[i + 1] = data[e]
    data[e] = temp
    return i + 1


def QuickDet(data, start, e):
    if(start < e):
        q = partition(data, start, e)
        QuickDet(data, start, q - 1)
        QuickDet(data, q + 1, e)
    return data


def QuickRandom(data, start, e):
    if (start < e):
        i = rd.randint(start, e)
        temp = data[i]
        data[i] = data[e]
        data[e] = temp
        q = partition(data, start, e)
        QuickRandom(data, start, q - 1)
        QuickRandom(data, q + 1, e)
    return data
	
def Insertion(data):
    count = 0
    for i in range(1, len(data)):
        idx = i
        while idx > 0 and data[idx - 1] > data[idx]:
            temp = data[idx]
            data[idx] = data[idx - 1]
            data[idx - 1] = temp
            idx = idx - 1
    return data


def MaxHeapify(data, size, i):
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if left <= size and data[left] > data[largest]:
        largest = left
    if right <= size and data[right] > data[largest]:
        largest = right
    if i != largest:
        temp = data[largest]
        data[largest] = data[i]
        data[i] = temp
        MaxHeapify(data, size, largest)


def BuildHeap(data, size):
    i = int(size / 2)
    while i > 0:
        MaxHeapify(data, size, i)
        i -= 1


def Heap(data):
    data[0] = None
    heap_size = len(data) - 1
    BuildHeap(data, heap_size)
    while heap_size > 0:
        temp = data[1]
        data[1] = data[heap_size]
        data[heap_size] = temp
        heap_size -= 1
        MaxHeapify(data, heap_size, 1)
    return data[1:]

#----------------------------------- Main ------------------------------
start = 1
end = (2 ** 32) - 1
nums = 4

data_nums = []
data_nums.append(rd.sample(range(start, end), 10))
data_nums.append(rd.sample(range(start, end), 100))
data_nums.append(rd.sample(range(start, end), 1000))
data_nums.append(rd.sample(range(start, end), 10000))
data_nums.append(rd.sample(range(start, end), 100000))
#data_nums.append(rd.sample(range(start, end), 1000000))

time_taken = []
for data in data_nums:
    data_time = []
    data_size = len(data) - 1
    for i in range(1, 6):
        start = time.time()
        if i == 1:
            #Insertion(data[:])
            print()
        elif i == 2:
            MergeRecursive(data[:])
        elif i == 3:
            QuickDet(data[:], 0, data_size)
        elif i == 4:
            QuickRandom(data[:], 0, data_size)
        elif i == 5:
            Heap(data[:] + [data[0]])
        end = time.time()
        data_time.append(end - start)
    time_taken.append(data_time)

print(time_taken)


