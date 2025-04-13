from interface import ArrayInterface

class QuadraticFunc(ArrayInterface):
    DELETED = object()

    def __init__(self, size):
        self.size = 0
        self.capacity = size
        self.table = [None] * self.capacity
        self.load_factor = 0.5

    def _hash(self, value):
        return value % self.capacity

    def insert(self, value):
        if self.size >= self.capacity * self.load_factor:
            self._resize()

        index = self._hash(value)
        i = 0

        while True:
            probe_index = (index + i ** 2) % self.capacity
            if self.table[probe_index] in (None, self.DELETED):
                self.table[probe_index] = value
                self.size += 1
                return
            elif self.table[probe_index] == value:
                return
            i += 1
            if i == self.capacity:
                return 

    def find(self, value):
        index = self._hash(value)
        i = 0

        while True:
            probe_index = (index + i ** 2) % self.capacity
            current = self.table[probe_index]
            if current is None:
                return False
            elif current == value:
                return True
            i += 1
            if i == self.capacity:
                return False

    def delete(self, value):
        index = self._hash(value)
        i = 0

        while True:
            probe_index = (index + i ** 2) % self.capacity
            current = self.table[probe_index]
            if current is None:
                return False
            elif current == value:
                self.table[probe_index] = self.DELETED
                self.size -= 1
                return True
            i += 1
            if i == self.capacity:
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
