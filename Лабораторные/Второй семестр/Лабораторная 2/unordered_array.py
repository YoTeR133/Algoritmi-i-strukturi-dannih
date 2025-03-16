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

    def get_min(self):
        if not self.elements:
            return None
        min_value = self.elements[0]
        for value in self.elements[1:]:
            if value < min_value:
                min_value = value
        return min_value

    def get_max(self):
        if not self.elements:
            return None
        max_value = self.elements[0]
        for value in self.elements[1:]:
            if value > max_value:
                max_value = value
        return max_value

    def quick_sort(self):
        if len(self.elements) <= 1:
            return
        self._quick_sort(0, len(self.elements) - 1)

    def _quick_sort(self, left, right):
        stack = deque([(left, right)])
        
        while stack:
            left, right = stack.pop()
            size = right - left + 1
            
            if size <= 133: 
                self._insertion_sort(left, right)
            elif left < right:
                pivot = self._median_of_three(left, right)
                partition_idx = self._partition(left, right, pivot)
                if partition_idx - left < right - partition_idx:
                    stack.append((partition_idx + 1, right))
                    stack.append((left, partition_idx - 1))
                else:
                    stack.append((left, partition_idx - 1))
                    stack.append((partition_idx + 1, right))

    def _insertion_sort(self, left, right):
        for i in range(left + 1, right + 1):
            temp = self.elements[i]
            j = i - 1
            while j >= left and self.elements[j] > temp:
                self.elements[j + 1] = self.elements[j]
                j -= 1
            self.elements[j + 1] = temp

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
            while left_ptr <= right and self.elements[left_ptr] < pivot:
                left_ptr += 1
            while right_ptr >= left and self.elements[right_ptr] > pivot:
                right_ptr -= 1
            if left_ptr >= right_ptr:
                break
            self.elements[left_ptr], self.elements[right_ptr] = self.elements[right_ptr], self.elements[left_ptr]
        self.elements[left_ptr], self.elements[right - 1] = self.elements[right - 1], self.elements[left_ptr]
        return left_ptr