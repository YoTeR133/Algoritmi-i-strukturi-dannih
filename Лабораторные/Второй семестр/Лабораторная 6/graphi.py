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
            print(f"\n{vershina} → {', '.join(sosedi) if sosedi else 'нет рёбер'}")
