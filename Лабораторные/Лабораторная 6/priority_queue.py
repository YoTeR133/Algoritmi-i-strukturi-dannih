class PriorityQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []
    
    def insert(self, item):
        if self.is_full():
            raise OverflowError("Невозможно добавить элемент: приоритетная очередь заполнена.")
        self.queue.append(item)
        self.queue.sort(reverse=True)  
    
    def remove(self):
        if self.is_empty():
            raise IndexError("Невозможно удалить элемент: приоритетная очередь пуста.")
        return self.queue.pop()
    
    def peek_min(self):
        if self.is_empty():
            raise IndexError("Невозможно посмотреть минимальный элемент: очередь пуста.")
        return self.queue[-1]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.size
