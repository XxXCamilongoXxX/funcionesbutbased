#funciones ses
def nombre_mas_largo(p_n):
    for x in range(3):
        if x==0:
            nombre_largo = p_n[0]
    else:
        if len(p_n[x]) > len(nombre_largo):
            nombre_largo = p_n[x]
    print("El nombre más largo es:",nombre_largo)
