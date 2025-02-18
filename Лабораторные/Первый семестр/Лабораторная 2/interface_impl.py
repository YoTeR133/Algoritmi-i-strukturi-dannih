from interface import ArrayInterface

class SimpleArray(ArrayInterface):
    def __init__(self, max_size=5):
        self.elements = []      
        self.max_size = max_size  

    def find(self, value):
        return value in self.elements
    
    def insert(self, value):
        self.elements.append(value)

    def delete(self, value):
        self.elements.remove(value)
        
    def display(self):
        print("Список:", self.elements)

    def get_min(self):
        return min(self.elements)

    def get_max(self):
        return max(self.elements)

