"""
Una función puede devolver múltiples valores.
"""

def rect(length, width):
    area = length * width
    perimeter = 2 * length + 2 * width
    return area, perimeter #2 valores

area_x, perimeter_y = rect(50, 100) #2 variables
print("El area es: ", area_x)
print("El perimeter es: ", perimeter_y)


print()
print()

"""
Otro bello ejemplo
"""

def profitable(d1, d2):
    area = d1 * d2
    invest = area > 700
    return invest

buy = profitable(90, 120)
print(buy)


print()
print()

"""
La ejecución del código dentro de una función termina cuando se devuelve un valor. 
Cualquier línea adicional de código después de la línea de retorno se ignorará.
"""
def rect(d1, d2):
    area = 0
    return area
    #Fin de la ejecución de la función
    area = d1 * d2 #No se ejecuta

x = rect(50, 50)
print(x)


print()
print()

"""
Python permite que los argumentos de función tengan valores predeterminados. 
Si se llama a la función sin el argumento, el argumento obtiene su valor predeterminado.

El valor predeterminado se utiliza solo si no se ha pasado otro valor como argumento cuando se llama a la función.
"""

def greet(name="Guest"):
    print("Welcome", name)

greet() # Bienvenido Invitado
greet("John") # Bienvenido John

print()

def greet(name="Guest"):
    print("Welcome", name)
greet("Anna")