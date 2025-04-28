class Graf:
    def __init__(self):
        self.smezhnost = {}

    def dobavit_vershinu(self, vershina):
        if vershina not in self.smezhnost:
            self.smezhnost[vershina] = []

    def dobavit_rebro(self, otkuda, kuda):
        if otkuda not in self.smezhnost:
            print(f"\nОшибка: вершина '{otkuda}' не существует.")
            return
        if kuda not in self.smezhnost:
            print(f"\nОшибка: вершина '{kuda}' не существует.")
            return
        if kuda not in self.smezhnost[otkuda]:
            self.smezhnost[otkuda].append(kuda)
        else:
            print(f"\nРебро из '{otkuda}' в '{kuda}' уже существует.")

    def pokazat_graf(self):
        for vershina, sosedi in self.smezhnost.items():
            print(f"{vershina} → {', '.join(sosedi) if sosedi else 'нет рёбер'}")

    def topologicheskaya_sortirovka(self):
        visited = set()
        stack = []
        temp_mark = set()

        def visit(node):
            if node in temp_mark:
                raise Exception(f"Обнаружен цикл в графе через вершину '{node}'.")
            if node not in visited:
                temp_mark.add(node)
                for neighbor in self.smezhnost.get(node, []):
                    visit(neighbor)
                temp_mark.remove(node)
                visited.add(node)
                stack.append(node)

        try:
            for v in self.smezhnost:
                if v not in visited:
                    visit(v)
            stack.reverse()
            return stack
        except Exception as e:
            print(str(e))
            return None
