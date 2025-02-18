import random
from interface_impl import SimpleArray

def main():
    max_size = int(input("Введите максимальный размер массива: "))  
    my_array = SimpleArray(max_size)  

    for i in range(max_size):  
        random_value = random.randint(1, 100)
        my_array.insert(random_value)

    my_array.display()

    search_value = random.randint(1, 100)

    if my_array.find(search_value):
        print(f"Значение {search_value} найдено в массиве")
    else:
        print(f"Значение {search_value} не найдено в массиве")

    my_array.delete(random_value)
    my_array.display()

    print("Минимальное значение:", my_array.get_min())
    print("Максимальное значение:", my_array.get_max())

main()
