import random
import time

class HighInterfaceArray:
    def __init__(self, size):
        self.array = [0] * size
        self.n_elems = 0

    def insert(self, value):
        if self.n_elems < len(self.array):
            self.array[self.n_elems] = value
            self.n_elems += 1

    def bubble_sort(self):
        start_time = time.time()
        for out in range(self.n_elems - 1, 0, -1):
            for _in in range(out):
                if self.array[_in] > self.array[_in + 1]:
                    self.swap(_in, _in + 1)
        end_time = time.time()
        print(f"Пузырьковая сортировка: {end_time - start_time:.2f} секунд")

    def insertion_sort(self):
        start_time = time.time()
        for out in range(1, self.n_elems):
            temp = self.array[out]
            in_idx = out
            while in_idx > 0 and self.array[in_idx - 1] >= temp:
                self.array[in_idx] = self.array[in_idx - 1]
                in_idx -= 1
            self.array[in_idx] = temp
        end_time = time.time()
        print(f"Сортировка вставками: {end_time - start_time:.2f} секунд")

    def selection_sort(self):
        start_time = time.time()
        for out in range(self.n_elems - 1):
            min_idx = out
            for in_idx in range(out + 1, self.n_elems):
                if self.array[in_idx] < self.array[min_idx]:
                    min_idx = in_idx
            self.swap(out, min_idx)
        end_time = time.time()
        print(f"Сортировка выбором: {end_time - start_time:.2f} секунд")

    def swap(self, idx1, idx2):
        self.array[idx1], self.array[idx2] = self.array[idx2], self.array[idx1]

size = 100_000
data = [random.randint(0, 100000) for _ in range(size)]

array1 = HighInterfaceArray(size)
for value in data:
    array1.insert(value)
print("Начинаем пузырьковую сортировку...")
array1.bubble_sort()

array2 = HighInterfaceArray(size)
for value in data:
    array2.insert(value)
print("Начинаем сортировку вставками...")
array2.insertion_sort()

array3 = HighInterfaceArray(size)
for value in data:
    array3.insert(value)
print("Начинаем сортировку выбором...")
array3.selection_sort()
