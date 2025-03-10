from interface import ArrayInterface

class OrderedArray(ArrayInterface):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def find(self, value):
        low, high = 0, len(self.elements) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.elements[mid] == value:
                return True
            elif self.elements[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def insert(self, value):
        if len(self.elements) >= self.max_size:
            return
        low, high = 0, len(self.elements)
        while low < high:
            mid = (low + high) // 2
            if self.elements[mid] < value:
                low = mid + 1
            else:
                high = mid
        self.elements.insert(low, value)

    def delete(self, value):
        low, high = 0, len(self.elements) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.elements[mid] == value:
                del self.elements[mid]
                return
            elif self.elements[mid] < value:
                low = mid + 1
            else:
                high = mid - 1

    def get_elements(self):
        return self.elements

    def get_min(self):
        if not self.elements:
            return None
        return self.elements[0]

    def get_max(self):
        if not self.elements:
            return None
        return self.elements[-1]

    def shell_sort(self, sequence_type):
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
                    self.elements[inner] = self.elements[inner - h]
                    inner -= h
                self.elements[inner] = temp
            if sequence_type == "Knuth":
                h = (h - 1) // 3
            elif sequence_type == "Shell":
                h = h // 2
            elif sequence_type == "ImprovedShell":
                h = int(h / 2.2)