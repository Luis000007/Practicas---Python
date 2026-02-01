""""
Los diccionarios son tipos de colección utilizados para almacenar datos en pares de clave:valor, que se consideran como elementos.
Son ideales para organizar datos en pares, donde cada pieza de datos (valor) tiene su identificador único (clave).
"""
# Los valores con claves duplicadas sobrescribirán los valores existentes.

product = {
    "name": "pen",
    "color": "red",
    "price": 79,
    "price": 50,
    "Marca": ["Blancanieves", "Girasol"]
}

print(product)
print()

# Para acceder a los valores en diccionarios, necesitas usar las keys.

print(product["name"])
print(product["color"])
print(product["price"])
print(product["Marca"])
print()

# Otra forma de Otra forma de acceder a los valores en un diccionario es a través de la función get().

tienda = product.get("name")
print(tienda)
print()

# Puedes obtener todos los valores y claves de un diccionario usando las funciones keys() y values(), respectivamente.

info_keys = product.keys()
info_values = product.values()

print(info_keys)
print(info_values)
print()

# La función items() devuelve todos los pares key:value en un diccionario.

info = product.items()
print(info)
print()

# Puedes usar las claves no solo para acceder a los valores en un diccionario, sino también para cambiarlos y agregar unos nuevos.
# Recomendable solo para agregar o modificar un dato / user["Age"] = 30

user = {
    "Name": "Albert",
    "Age": 29
}
user["Age"] = 30
user["Mail"] = "perenganito@jotomail.com"

print(user["Age"])
print(user.items())

# Y si quieres agregar o modificar mas de un dato lo ideal sera / user.update({"Clave" : "Llave"})

user.update({
    "Direccion" : "Calle de mis huevos morenos",
    "Sexo" : "Claro que si negroooo",
    "Tarjeta" : 23242344325425
})
print(user.items())

# La función pop() elimina el elemento con el nombre de clave especificado. Acepta la clave del elemento que quieres eliminar como argumento.

user.pop("Tarjeta")
print(user)

# Puedes usar el operador in para verificar si una clave o un valor ocurre en un diccionario.

print("Sexo" in user)
print("Tarjeta" in user.values())