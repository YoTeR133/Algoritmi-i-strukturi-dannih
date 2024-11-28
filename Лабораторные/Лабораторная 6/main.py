from stack import Stack
from queue_impl import Queue  
from priority_queue import PriorityQueue
from palindrome_checker import is_palindrome

def stack_example():
    print("\nПример использования стека:")
    stack = Stack(5)
    stack.push('А')
    stack.push('Б')
    stack.push('В')
    while not stack.is_empty():
        print(stack.pop(), end=" ")
    print()

def queue_example():
    print("Пример использования очереди:")
    queue = Queue(5)
    queue.insert(10)
    queue.insert(20)
    queue.insert(30)
    print(queue.remove())  
    print(queue.remove())  
    print(f"Первый элемент в очереди: {queue.peek()}")

def priority_queue_example():
    print("Пример использования приоритетной очереди:")
    pq = PriorityQueue(5)
    pq.insert(30)
    pq.insert(10)
    pq.insert(20)
    while not pq.is_empty():
        print(pq.remove(), end=" ")
    print()

if __name__ == "__main__":
    stack_example()
    queue_example()
    priority_queue_example()

    print("\nПример проверки палиндрома:")
    test_string = "12321"
    print(f"Является ли '{test_string}' палиндромом? {is_palindrome(test_string)}")
    test_string = "яблоко"
    print(f"Является ли '{test_string}' палиндромом? {is_palindrome(test_string)}\n")
