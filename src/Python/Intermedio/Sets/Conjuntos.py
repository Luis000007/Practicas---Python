print("Los setes se crean con llaves, los sets son desordenados y no soportan indexación o segmentación, peropuedes agregar o eliminar elementos add(), remove()")
print("Los setes no tienen duplicados, cada valor es unico y si llegara a estar prensente un duplicado se ignora y soportan distintos tipos de datos")
print()

print("Set original")
guests = {"Mery", "Anna","Anna", "Jonathan", 48, 20.50}
print(guests)
print()
# print(guests[0]) #error

print("add(), remove(), clear()")
guests.add("Carlos") # Añadir
guests.remove(48) # Eliminar
# guests.clear() # Eliminar todos los elementos

print(guests)
print()


# La función union() se llama en un set y acepta otro set como argumento.
print("union()")
set1 = {"Mickey", "Donald", "Goofy"}
set2 = {"Mine", "Dasy", "Clarabella"}

parejas_disney = set1.union(set2) # union() para unir dos sets
print(parejas_disney)
print()

# La función difference() devuelve un conjunto que contiene elementos que solo están en el primer conjunto y no en el segundo.
print("difference()")
set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}
unique = set1.difference(set2)
print(unique)