from interface import ArrayInterface

class SimpleArray(ArrayInterface):
    def __init__(self, max_size=5):
        self.elements = []
        self.max_size = max_size
        self.min_value = None
        self.max_value = None

    def find(self, value):
        return value in self.elements  

    def insert(self, value):
        if len(self.elements) < self.max_size:
            low, high = 0, len(self.elements)
            while low < high:
                mid = (low + high) // 2
                if self.elements[mid] < value:
                    low = mid + 1
                else:
                    high = mid
            self.elements.insert(low, value)

            if self.min_value is None and self.max_value is None:
                self.min_value = value
                self.max_value = value
            else:
                if value < self.min_value:
                    self.min_value = value
                if value > self.max_value:
                    self.max_value = value

    def delete(self, value):
        if value in self.elements:
            self.elements.remove(value)
            if not self.elements:
                self.min_value = None
                self.max_value = None
            else:
                if value == self.min_value or value == self.max_value:
                    self.min_value = min(self.elements)
                    self.max_value = max(self.elements)

    def display(self):
        print("Список:", self.elements)

    def get_min(self):
        return self.min_value

    def get_max(self):
        return self.max_value
