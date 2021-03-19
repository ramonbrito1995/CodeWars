print(lista_2)

def filter_list(l):
    lista = l
    lista_1 = list()
    for i in range(len(lista)):
        if type(lista[i]) != type(str(lista[i])):
            lista_1.append(lista[i]) 
    return lista_1
        
print(filter_list([1,2,'a','b']))