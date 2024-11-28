class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
    
    def push(self, item):
        if self.is_full():
            raise OverflowError("Невозможно добавить элемент: стек заполнен.")
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Невозможно извлечь элемент: стек пуст.")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Невозможно посмотреть верхний элемент: стек пуст.")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.size
