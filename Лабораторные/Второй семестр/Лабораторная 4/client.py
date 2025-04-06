import random
from UnorderedArray import UnorderedArray

def main():
    size = int(input("Введите начальный размер хеш-таблицы: "))
    if size <= 0:
        print("Размер должен быть положительным числом, попробуйте снова")
        return
    count = int(input("Сколько чисел добавить?: "))
    if count < 0:
        print("Количество не может быть отрицательным, попробуйте снова")
        return

    table = UnorderedArray(size)

    for _ in range(count):
        table.insert(random.randint(1, 100))

    print("\nХеш-таблица:")
    table.display()

if __name__ == "__main__":
    main()