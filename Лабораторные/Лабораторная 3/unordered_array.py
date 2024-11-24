from interface import ArrayInterface

class UnorderedArray(ArrayInterface):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size
        self._min_value = None
        self._max_value = None

    def find(self, value):
        return value in self.elements

    def insert(self, value):
        if len(self.elements) < self.max_size:
            self.elements.append(value)
            self._min_value = None 
            self._max_value = None

    def delete(self, value):
        if value in self.elements:
            self.elements.remove(value)
            self._min_value = None
            self._max_value = None

    def get_elements(self):
        return self.elements

    def get_min(self):
        if self._min_value is None:
            if not self.elements:
                return None
            self._min_value = self.elements[0]
            for value in self.elements[1:]:
                if value < self._min_value:
                    self._min_value = value
        return self._min_value

    def get_max(self):
        if self._max_value is None:
            if not self.elements:
                return None
            self._max_value = self.elements[0]
            for value in self.elements[1:]:
                if value > self._max_value:
                    self._max_value = value
        return self._max_value
