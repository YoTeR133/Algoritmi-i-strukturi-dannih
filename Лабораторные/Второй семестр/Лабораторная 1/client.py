import random
import time
from unordered_array import UnorderedArray
from ordered_array import OrderedArray

def test_shell_sort(array_class, max_size, sequence_type, iterations=1000):
    total_time = 0
    for _ in range(iterations):
        arr = array_class(max_size)
        for _ in range(max_size):
            arr.insert(random.randint(1, 100))

        start_time = time.perf_counter()
        arr.shell_sort(sequence_type)
        end_time = time.perf_counter()
        
        total_time += (end_time - start_time)
    
    return (total_time / iterations) * 1000

def main():
    max_size = int(input("Введите максимальный размер массива: "))
    sequences = ["Knuth", "Shell", "ImprovedShell"]

    print("\nТестирование сортировки Шелла для UnorderedArray:")
    for seq in sequences:
        time_taken = test_shell_sort(UnorderedArray, max_size, seq)
        print(f"Последовательность {seq}: {time_taken:.3f} мс")

    print("\nТестирование сортировки Шелла для OrderedArray:")
    for seq in sequences:
        time_taken = test_shell_sort(OrderedArray, max_size, seq)
        print(f"Последовательность {seq}: {time_taken:.3f} мс")

if __name__ == "__main__":
    main()