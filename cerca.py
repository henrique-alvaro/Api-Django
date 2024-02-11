def ordem(lista):
    index_marina = lista.index('marina')
    index_paula = lista.index('paula')
    index_renata = lista.index('renata')
    index_sara = lista.index('sara')
    index_vitoria = lista.index('vitoria')
    lista_penalt = []
    
    for nome in lista:
        if nome == 'paula':
            lista_penalt.append(lista[index_paula])
        elif nome == 'vitoria':
            lista_penalt.append(lista[index_vitoria])
        elif nome == 'marina':
            lista_penalt.insert(index_vitoria, lista[index_marina])

    return lista_penalt
     
    
lista = ['marina', 'paula', 'renata', 'sara', 'vitoria']
print(ordem(lista))

