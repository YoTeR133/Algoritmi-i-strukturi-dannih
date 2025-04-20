from graphi import sozdat_graf, dobavit_vershina, dobavit_rebro, pokazat_graf

def main():
    graf = sozdat_graf()

    while True:
        print("\nМеню:")
        print("1 — Добавить вершину")
        print("2 — Добавить ребро")
        print("3 — Показать граф")
        print("4 — Выход")

        vibor = input("Ваш выбор: ")

        if vibor == "1":
            v = input("Введите вершину: ")
            dobavit_vershina(graf, v)
        elif vibor == "2":
            otkuda = input("Из вершины: ")
            kuda = input("В вершину: ")
            dobavit_rebro(graf, otkuda, kuda)
        elif vibor == "3":
            pokazat_graf(graf)
        elif vibor == "4":
            break

if __name__ == "__main__":
    main()
