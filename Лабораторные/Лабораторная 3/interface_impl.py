from interface import ArrayInterface

class UnorderedArray(ArrayInterface):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size
        self.min_value = None
        self.max_value = None

    def find(self, value):
        return value in self.elements

    def insert(self, value):
        if len(self.elements) < self.max_size:
            self.elements.append(value)
            if self.min_value is None or value < self.min_value:
                self.min_value = value
            if self.max_value is None or value > self.max_value:
                self.max_value = value

    def delete(self, value):
        if value in self.elements:
            self.elements.remove(value)
            if value == self.min_value or value == self.max_value:
                if self.elements:
                    self.min_value = min(self.elements)
                    self.max_value = max(self.elements)
                else:
                    self.min_value = None
                    self.max_value = None

    def get_elements(self):
        return self.elements

    def get_min(self):
        return self.min_value

    def get_max(self):
        return self.max_value

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
        if self.find(value):
            self.elements.remove(value)

    def get_elements(self):
        return self.elements

    def get_min(self):
        return self.elements[0] if self.elements else None

    def get_max(self):
        return self.elements[-1] if self.elements else None
