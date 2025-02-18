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
