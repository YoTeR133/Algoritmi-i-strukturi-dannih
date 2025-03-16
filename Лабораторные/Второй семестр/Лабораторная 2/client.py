import random
import time
from unordered_array import UnorderedArray

def main():
    max_size = int(input("\nВведите максимальный размер массива: "))
    arr = UnorderedArray(max_size)
    
    for _ in range(max_size):
        arr.insert(random.randint(1, 100))
    
    print("\nМассив до сортировки:")
    arr.display()
    
    start_time = time.perf_counter()
    arr.quick_sort()
    end_time = time.perf_counter()
    
    print("\nМассив после сортировки:")
    arr.display()
    print(f"\nВремя выполнения: {(end_time - start_time) * 1000:.3f} мс\n")

if __name__ == "__main__":
    main()