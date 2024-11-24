import random
from unordered_array import UnorderedArray
from ordered_array import OrderedArray

def main():
    max_size = int(input("Введите максимальный размер массива: "))

    print("Работа с неупорядоченным массивом:")
    unordered_array = UnorderedArray(max_size)
    for i in range(max_size):
        random_value = random.randint(1, 100)
        unordered_array.insert(random_value)

    print("Неупорядоченный массив:", unordered_array.get_elements())
    print("Минимальное значение:", unordered_array.get_min())
    print("Максимальное значение:", unordered_array.get_max())

    search_value = random.randint(1, 100)
    print(f"Поиск {search_value}:", "найдено" if unordered_array.find(search_value) else "не найдено")
    unordered_array.delete(search_value)
    print("После удаления:", unordered_array.get_elements())

    print("\nРабота с упорядоченным массивом:")
    ordered_array = OrderedArray(max_size)
    for i in range(max_size):
        random_value = random.randint(1, 100)
        ordered_array.insert(random_value)

    print("Упорядоченный массив:", ordered_array.get_elements())
    print("Минимальное значение:", ordered_array.get_min())
    print("Максимальное значение:", ordered_array.get_max())

    print(f"Поиск {search_value}:", "найдено" if ordered_array.find(search_value) else "не найдено")
    ordered_array.delete(search_value)
    print("После удаления:", ordered_array.get_elements())

if __name__ == "__main__":
    main()
