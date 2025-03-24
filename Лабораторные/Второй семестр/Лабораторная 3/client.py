import random
import time
from unordered_array import UnorderedArray

def main():
    max_size = int(input("\nВведите максимальный размер массива: "))
    arr_quick = UnorderedArray(max_size)
    arr_shell = UnorderedArray(max_size)
    arr_merge = UnorderedArray(max_size)
    
    random_values = [random.randint(1, 100) for _ in range(max_size)]
    
    start_time = time.perf_counter()
    for value in random_values:
        arr_quick.insert(value)
    insert_time_quick = (time.perf_counter() - start_time) * 1000
    
    start_time = time.perf_counter()
    for value in random_values:
        arr_shell.insert(value)
    insert_time_shell = (time.perf_counter() - start_time) * 1000
    
    start_time = time.perf_counter()
    for value in random_values:
        arr_merge.insert(value)
    insert_time_merge = (time.perf_counter() - start_time) * 1000
    
    start_time = time.perf_counter()
    arr_quick.quick_sort()
    sort_time_quick = (time.perf_counter() - start_time) * 1000
    
    start_time = time.perf_counter()
    arr_shell.shell_sort("Knuth")
    sort_time_shell = (time.perf_counter() - start_time) * 1000
    
    start_time = time.perf_counter()
    arr_merge.merge_sort()
    sort_time_merge = (time.perf_counter() - start_time) * 1000
    
    print("\nБыстрая сортировка:")
    print(f"Время сортировки: {sort_time_quick:.3f} мс")
    print(f"Сравнений: {arr_quick.comparisons}, Перестановок: {arr_quick.swaps}")
    
    print("\nСортировка Шелла:")
    print(f"Время сортировки: {sort_time_shell:.3f} мс")
    print(f"Сравнений: {arr_shell.comparisons}, Перестановок: {arr_shell.swaps}")
    
    print("\nСортировка слиянием:")
    print(f"Время сортировки: {sort_time_merge:.3f} мс")
    print(f"Сравнений: {arr_merge.comparisons}, Перестановок: {arr_merge.swaps}\n")

if __name__ == "__main__":
    main()