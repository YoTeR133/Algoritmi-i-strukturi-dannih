from interface import ArrayInterface
from collections import deque

class UnorderedArray(ArrayInterface):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size
        self.comparisons = 0 
        self.swaps = 0       

    def find(self, value):
        return value in self.elements

    def insert(self, value):
        if len(self.elements) < self.max_size:
            self.elements.append(value)

    def delete(self, value):
        if value in self.elements:
            self.elements.remove(value)

    def display(self):
        print(" ".join(map(str, self.elements)))

    def quick_sort(self):
        self.comparisons = 0
        self.swaps = 0
        if len(self.elements) <= 1:
            return
        self._quick_sort(0, len(self.elements) - 1)

    def _quick_sort(self, left, right):
        stack = deque([(left, right)])

        while stack:
            left, right = stack.pop()
            
            if left >= right:
                continue

            pivot = self._median_of_three(left, right)
            partition_idx = self._partition(left, right, pivot)

            if partition_idx - left > right - partition_idx:
                stack.append((left, partition_idx - 1))
                stack.append((partition_idx + 1, right))
            else:
                stack.append((partition_idx + 1, right))
                stack.append((left, partition_idx - 1))

    def _median_of_three(self, left, right):
        center = (left + right) // 2
        self.comparisons += 3
        if self.elements[left] > self.elements[center]:
            self.elements[left], self.elements[center] = self.elements[center], self.elements[left]
            self.swaps += 1
        if self.elements[left] > self.elements[right]:
            self.elements[left], self.elements[right] = self.elements[right], self.elements[left]
            self.swaps += 1
        if self.elements[center] > self.elements[right]:
            self.elements[center], self.elements[right] = self.elements[right], self.elements[center]
            self.swaps += 1
        self.elements[center], self.elements[right - 1] = self.elements[right - 1], self.elements[center]
        self.swaps += 1
        return self.elements[right - 1]

    def partition(self, pivot):
        if not self.elements:
            return -1
        return self._partition(0, len(self.elements) - 1, pivot)

    def _partition(self, left, right, pivot):
        left_ptr = left
        right_ptr = right - 1

        while True:
            while left_ptr <= right_ptr and self.elements[left_ptr] < pivot:
                self.comparisons += 1
                left_ptr += 1
            while right_ptr >= left_ptr and self.elements[right_ptr] > pivot:
                self.comparisons += 1
                right_ptr -= 1

            self.comparisons += 1
            if left_ptr >= right_ptr:
                break

            self.elements[left_ptr], self.elements[right_ptr] = self.elements[right_ptr], self.elements[left_ptr]
            self.swaps += 1
            left_ptr += 1
            right_ptr -= 1
        self.elements[left_ptr], self.elements[right - 1] = self.elements[right - 1], self.elements[left_ptr]
        self.swaps += 1
        return left_ptr

    def shell_sort(self, sequence_type):
        self.comparisons = 0
        self.swaps = 0
        n = len(self.elements)
        if n <= 1:
            return

        h = 1
        if sequence_type == "Knuth":
            while h <= n // 3:
                h = h * 3 + 1
        elif sequence_type == "Shell":
            h = n // 2
        elif sequence_type == "ImprovedShell":
            h = int(n / 2.2)
        else:
            raise ValueError("Unknown sequence type")

        while h > 0:
            for outer in range(h, n):
                temp = self.elements[outer]
                inner = outer
                while inner >= h and self.elements[inner - h] > temp:
                    self.comparisons += 1
                    self.elements[inner] = self.elements[inner - h]
                    self.swaps += 1
                    inner -= h
                self.comparisons += 1
                self.elements[inner] = temp
            if sequence_type == "Knuth":
                h = (h - 1) // 3
            elif sequence_type == "Shell":
                h = h // 2
            elif sequence_type == "ImprovedShell":
                h = int(h / 2.2)

    def merge_sort(self):
        self.comparisons = 0
        self.swaps = 0
        if len(self.elements) <= 1:
            return
        temp_array = [0] * len(self.elements)
        self._merge_sort(temp_array, 0, len(self.elements) - 1)

    def _merge_sort(self, temp_array, lower_bound, upper_bound):
        if lower_bound < upper_bound:
            middle = (lower_bound + upper_bound) // 2
            self._merge_sort(temp_array, lower_bound, middle)
            self._merge_sort(temp_array, middle + 1, upper_bound)
            self._merge(temp_array, lower_bound, middle, upper_bound)

    def _merge(self, temp_array, lower_bound, middle, upper_bound):
        i = lower_bound
        j = middle + 1
        k = 0

        while i <= middle and j <= upper_bound:
            self.comparisons += 1
            if self.elements[i] <= self.elements[j]:
                temp_array[k] = self.elements[i]
                i += 1
            else:
                temp_array[k] = self.elements[j]
                j += 1
            k += 1

        while i <= middle:
            temp_array[k] = self.elements[i]
            i += 1
            k += 1

        while j <= upper_bound:
            temp_array[k] = self.elements[j]
            j += 1
            k += 1

        for m in range(k):
            self.elements[lower_bound + m] = temp_array[m]
            self.swaps += 1