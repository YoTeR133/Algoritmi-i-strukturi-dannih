def sozdat_graf():
    return {}

def dobavit_vershina(graf, vershina):
    if vershina not in graf:
        graf[vershina] = []

def dobavit_rebro(graf, otkuda, kuda):
    if otkuda not in graf:
        dobavit_vershina(graf, otkuda)
    if kuda not in graf:
        dobavit_vershina(graf, kuda)
    if kuda not in graf[otkuda]:  
        graf[otkuda].append(kuda)

def pokazat_graf(graf):
    for vershina in graf:
        sosedi = ", ".join(graf[vershina])
        print(f"{vershina} → {sosedi}")
