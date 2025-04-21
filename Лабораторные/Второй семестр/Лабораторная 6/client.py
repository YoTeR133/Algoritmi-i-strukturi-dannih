from graphi import Graf

def main():
    graf = Graf()

    while True:
        print("\nМеню:")
        print("1 — Добавить вершину")
        print("2 — Добавить ребро")
        print("3 — Показать граф")
        print("4 — Выход")

        vibor = input("Ваш выбор: ")

        if vibor == "1":
            v = input("Введите вершину: ")
            graf.dobavit_vershinu(v)
        elif vibor == "2":
            otkuda = input("Из вершины: ")
            kuda = input("В вершину: ")
            graf.dobavit_rebro(otkuda, kuda)
        elif vibor == "3":
            graf.pokazat_graf()
        elif vibor == "4":
            break

if __name__ == "__main__":
    main()
