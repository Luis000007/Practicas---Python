"""
Puedes crear listas de manera mas rapida y eficiente en lugar de crearlas tu mismo, con bucles
"""

num = [] # Necesitas crear una lista vacía y luego agregar cada elemento recorriendo un rango.

for i in range(1, 51):
    num.append(i)

print(num)

# List comprehensions son atajos útiles para tales operaciones.

numss = [x/2 for x in range(1,51)] # Se puede multiplicar(*), restar(-), sumar(+), dividir(/) cada valor en range y almacena los resultadso en la lista
                                   # Se haran las operaciones uno a uno por cada valor de la lists
print(numss)

letrado = [c*2 for c in "Dificuldad"] # Tambien funciona con cadenas

print(letrado)

"""
Sintaxis genérica y estructura de una comprensión de lista (Ejemplo basado en la comprensiones de lista de arriba):

<variable>: letrado
la variable que almacenará la nueva lista creada

<expression>: c*2
una expresión realizada en cada elemento. Si no se necesita ninguna acción específica, se utiliza el elemento en sí

<item>: c
el elemento actual que se está procesando

<iterable>: "Dificuldad"
cualquier objeto iterable, como rangos, listas, cadenas, tuplas y conjuntos
"""

# Puedes usar una lista como iterable en una comprensión de lista. Por ejemplo:

tags = ["travel", "vacation", "journey"]

hashtags = ["#" + x.capitalize() for x in tags] # Se le pueden agregar muchas cosas a la expresion
print(hashtags)

# Puedes incorporar una condición en una comprensión de listas, colocada después del iterable.

users = ["Brandon", "Emma", "Brian",
         "Sophia", "Bella", "Ethan",
         "Ava", "Benjamin", "Mia", "Chloe"]

names_B = [x for x in users if x[0] == "B"] # Tambien puede ser usado != para seleccionaar los nombres que no empiezen con b por ejemplo
                                            # Puedes utilizar cualquier operador que se use con condicioens
print(names_B)