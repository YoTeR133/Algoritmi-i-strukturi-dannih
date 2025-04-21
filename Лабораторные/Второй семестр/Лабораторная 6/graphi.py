class Graf:
    def __init__(self):
        self.smezhnost = {}

    def dobavit_vershinu(self, vershina):
        if vershina not in self.smezhnost:
            self.smezhnost[vershina] = []

    def dobavit_rebro(self, otkuda, kuda):
        self.dobavit_vershinu(otkuda)
        self.dobavit_vershinu(kuda)
        if kuda not in self.smezhnost[otkuda]:
            self.smezhnost[otkuda].append(kuda)

    def pokazat_graf(self):
        for vershina in self.smezhnost:
            sosedi = ", ".join(self.smezhnost[vershina])
            print(f"{vershina} → {sosedi}")
