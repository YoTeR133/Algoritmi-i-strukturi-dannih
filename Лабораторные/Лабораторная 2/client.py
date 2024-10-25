import random
from interface_impl import SimpleArray

def main():
    my_array = SimpleArray()  

    for i in range(5):  
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
