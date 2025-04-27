import random
from graphi import Graf

def main():
    graf = Graf()

    while True:
        print("\n1 — Добавить вершину")
        print("2 — Добавить ребро")
        print("3 — Показать граф")
        print("4 — Топологическая сортировка")
        print("5 — Пример заполнения и сортировки")
        print("6 — Выход\n")

        vibor = input("Ваш выбор: ").strip()

        if vibor == "1":
            v = input("Введите метку вершины: ").strip()
            graf.dobavit_vershinu(v)

        elif vibor == "2":
            otkuda = input("Из вершины: ").strip()
            kuda = input("В вершину: ").strip()
            graf.dobavit_rebro(otkuda, kuda)

        elif vibor == "3":
            print("\nТекущий граф:")
            graf.pokazat_graf()

        elif vibor == "4":
            print("\nРезультат топологической сортировки:")
            result = graf.topologicheskaya_sortirovka()
            if result:
                print(" → ".join(result))

        elif vibor == "5":
            print("\nАвтоматическое заполнение графа")
            auto_fill_graph(graf)
            print("\nТекущий граф после автоматического заполнения:")
            graf.pokazat_graf()
            print("\nРезультат топологической сортировки:")
            result = graf.topologicheskaya_sortirovka()
            if result:
                print(" → ".join(result))

        elif vibor == "6":
            print("")
            break

        else:
            print("\nОшибка: некорректный ввод. Попробуйте снова.")

def auto_fill_graph(graf):
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    for v in vertices:
        graf.dobavit_vershinu(v)

    edges = [('A', 'D'), ('B', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')]
    for otkuda, kuda in edges:
        graf.dobavit_rebro(otkuda, kuda)

if __name__ == "__main__":
    main()
