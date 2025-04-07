from interface import ArrayInterface

class UnorderedArray(ArrayInterface):
    DELETED = object()  

    def __init__(self, size):
        self.size = 0
        self.capacity = size
        self.table = [None] * self.capacity
        self.load_factor = 0.50

    def _hash(self, value):
        return value % self.capacity

    def insert(self, value):
        if self.size >= self.capacity * self.load_factor:
            self._resize()

        index = self._hash(value)
        while self.table[index] not in (None, self.DELETED):
            if self.table[index] == value:
                return  
            index = (index + 1) % self.capacity

        self.table[index] = value
        self.size += 1

    def find(self, value):
        index = self._hash(value)
        start = index
        while self.table[index] is not None:
            if self.table[index] == value:
                return True
            index = (index + 1) % self.capacity
            if index == start:
                break
        return False

    def delete(self, value):
        index = self._hash(value)
        start = index
        while self.table[index] is not None:
            if self.table[index] == value:
                self.table[index] = self.DELETED
                self.size -= 1
                return True
            index = (index + 1) % self.capacity
            if index == start:
                break
        return False

    def _resize(self):
        print(f"\n*** 50% заполнено, расширение таблицы: {self.capacity} → {self.capacity * 2} ***\n")
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        for item in old_table:
            if item not in (None, self.DELETED):
                self.insert(item)

    def display(self):
        for i, val in enumerate(self.table):
            if val is self.DELETED:
                print(f"[{i}]: <Удалён>")
            elif val is None:
                print(f"[{i}]: Пустой")
            else:
                print(f"[{i}]: {val}")