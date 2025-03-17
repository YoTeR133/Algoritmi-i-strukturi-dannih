from interface import ArrayInterface
from collections import deque

class UnorderedArray(ArrayInterface):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

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
        if self.elements[left] > self.elements[center]:
            self.elements[left], self.elements[center] = self.elements[center], self.elements[left]
        if self.elements[left] > self.elements[right]:
            self.elements[left], self.elements[right] = self.elements[right], self.elements[left]
        if self.elements[center] > self.elements[right]:
            self.elements[center], self.elements[right] = self.elements[right], self.elements[center]
        self.elements[center], self.elements[right - 1] = self.elements[right - 1], self.elements[center]
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
                left_ptr += 1
            while right_ptr >= left_ptr and self.elements[right_ptr] > pivot:
                right_ptr -= 1

            if left_ptr >= right_ptr:
                break

            self.elements[left_ptr], self.elements[right_ptr] = self.elements[right_ptr], self.elements[left_ptr]
            left_ptr += 1
            right_ptr -= 1
        self.elements[left_ptr], self.elements[right - 1] = self.elements[right - 1], self.elements[left_ptr]
        return left_ptr
