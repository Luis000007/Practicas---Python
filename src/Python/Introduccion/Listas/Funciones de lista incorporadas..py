print("len()")
"""
len() es una de las funciones incorporadas más útiles.

len() significa longitud y, cuando se utiliza en listas, devuelve el número de elementos en la lista.
"""

movies = ["Avatar", "Titanic", "Avengers"]
print(len(movies))


# La función len() no solo es para listas. Acepta como argumento cualquier secuencia, incluyendo cadenas de texto.
# Mostrara el numero de caracteres en el string
movie = "Avatar"
print(len(movie))



print()
print()



print("append()")
"""
La función append() agrega un nuevo elemento al final de una lista.

append() se llama utilizando la notación de punto porque es específica de las listas.
"""

# Agregara "Imagine" a la lista original
songs = ["Yesterday", "Hello", "Believer"]
songs.append("Imagine")
print(songs)



print()
print()



print("insert()")
"""
La función insert() te permite agregar un elemento a una lista en una posición específica.
insert() toma 2 argumentos. El primero es el índice (dónde insertar) y el segundo es el elemento (qué insertar).
"""

items = ["book", "pen", "pencil"]
items.insert(2,"marker")
print(items)
print(items[2])



print()
print()



print("pop()")
"""
La función pop() elimina un elemento de una lista. Toma el índice del elemento a eliminar como argumento.
"""

items = ["book", "pen", "pencil"]
items.pop(1)
print(items)
print(items[1])