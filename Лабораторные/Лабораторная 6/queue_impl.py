class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []
    
    def insert(self, item):
        if self.is_full():
            raise OverflowError("Невозможно добавить элемент: очередь заполнена.")
        self.queue.append(item)
    
    def remove(self):
        if self.is_empty():
            raise Exception("Ошибка: Очередь пуста, невозможно извлечь элемент.")
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise Exception("Ошибка: Очередь пуста, невозможно посмотреть первый элемент.")
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.size
