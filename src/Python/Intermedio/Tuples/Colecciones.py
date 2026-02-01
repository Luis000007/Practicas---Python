

print("Un Tuple es una coleccion que contiene varios valores, solo que son inmutables a diferencia de las listas: ")
tuples = (23.2323, 32, "Sueño")
print(tuples)
print()

# Los tuples no son mutables

# tuples[0] = 56.7581 #error
# tuples.append("ere") #error

print(tuples[0])
print(tuples[1])
print(tuples[2])

print()
print()
"""
Las tuplas, como las listas, pueden contener elementos duplicados.
Puedes usar la función count() para calcular el número de ocurrencias de un elemento en una tupla.
"""

scores = (7, 7, 9, 9, 8, 9)
print("# of 7:",scores.count(7))
print("# of 9:",scores.count(9))
print("# of 2:",scores.count(2))



print()
print()
"""
Puedes usar muchas funciones de las listas siempre y cuando no las modifiques 
"""

print("Ejemplos")
Tienda = ("Max Steel", "Auto", "Patin", 121, 34, 2323.50)

Numeros = (2323, 23232, 56756, 656, 78)

# Contar el numero de elementos en la tuple / len()
count = print("En la tuple tienda hay: ", len(Tienda)," articulos")

# Para identificar el valor maximo / max()
# Para identificar el valor minimo / min()
mayor = print("Valor maximo:", max(Numeros))
minimo = print("Valor maximo:", min(Numeros))
print()
print()

print("Ejemplos practicos")

points = (12, 14, 9, 10, 9)
for point in points:
    if point > 10:
        print(point, ": passed")


print()
print()

"""
La desempaquetación de tuplas permite asignar elementos de tuplas a variables. Los valores se asignarán en el orden en que aparecen en la tupla.
"""

birthday_date = (12, "August", 1993)
day, month, year = birthday_date

print(day)
print(month)
print(year)


print()
print()
"""
El operador * en el desempaquetado de tuplas se utiliza para reunir varios elementos de la tupla en una lista. 
Esto es útil cuando se trata de tuplas de longitud desconocida.
"""

scores = (98, 96, 91, 88, 64)
winner, *rest = scores
print(winner)
print(rest)

