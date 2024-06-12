import matplotlib.pyplot as plt
import numpy as np
import random
import time

def bubble_sort(data, draw_data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_data(data, ['green' if x == j or x == j+1 else 'blue' for x in range(len(data))])
                time.sleep(0.2)
    draw_data(data, ['green' for _ in range(len(data))])

def selection_sort(data, draw_data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, ['green' if x == i or x == min_idx else 'blue' for x in range(len(data))])
        time.sleep(0.2)
    draw_data(data, ['green' for _ in range(len(data))])

def insertion_sort(data, draw_data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        draw_data(data, ['green' if x == i or x == j+1 else 'blue' for x in range(len(data))])
        time.sleep(0.2)
    draw_data(data, ['green' for _ in range(len(data))])

def merge_sort(data, draw_data):
    merge_sort_alg(data, 0, len(data)-1, draw_data)

def merge_sort_alg(data, left, right, draw_data):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, draw_data)
        merge_sort_alg(data, middle + 1, right, draw_data)
        merge(data, left, middle, right, draw_data)

def merge(data, left, middle, right, draw_data):
    n1 = middle - left + 1
    n2 = right - middle

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = data[left + i]

    for j in range(n2):
        R[j] = data[middle + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        data[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        data[k] = R[j]
        j += 1
        k += 1

    draw_data(data, ['green' if x >= left and x <= right else 'blue' for x in range(len(data))])
    time.sleep(0.2)

def quick_sort(data, draw_data):
    quick_sort_alg(data, 0, len(data)-1, draw_data)

def quick_sort_alg(data, low, high, draw_data):
    if low < high:
        pi = partition(data, low, high, draw_data)
        quick_sort_alg(data, low, pi-1, draw_data)
        quick_sort_alg(data, pi+1, high, draw_data)

def partition(data, low, high, draw_data):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            draw_data(data, ['green' if x == i or x == j else 'blue' for x in range(len(data))])
            time.sleep(0.2)
    data[i+1], data[high] = data[high], data[i+1]
    return i+1

def draw_data(data, color_array):
    plt.clf()
    plt.bar(range(len(data)), data, color=color_array)
    plt.title("Sorting Algorithm Visualization")
    plt.pause(0.05)
    plt.draw()

def main():
    algorithms = {
        '1': ('Bubble Sort', bubble_sort),
        '2': ('Selection Sort', selection_sort),
        '3': ('Insertion Sort', insertion_sort),
        '4': ('Merge Sort', merge_sort),
        '5': ('Quick Sort', quick_sort)
    }

    print("Choose a sorting algorithm:")
    for key, value in algorithms.items():
        print(f"{key}. {value[0]}")

    choice = input("Enter the number of the sorting algorithm: ")

    if choice not in algorithms:
        print("Invalid choice. Exiting.")
        return

    print("Generating data to be sorted...")
    data = [random.randint(1, 100) for _ in range(50)]

    plt.figure(figsize=(10, 6))
    plt.ion()

    algorithm_name, algorithm_function = algorithms[choice]
    print(f"Running {algorithm_name}...")
    algorithm_function(data, draw_data)

    plt.ioff()
    plt.show()

if __name__ == '__main__':
    main()
