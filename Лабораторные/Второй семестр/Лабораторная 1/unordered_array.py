from interface import ArrayInterface

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

    def get_elements(self):
        return self.elements

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