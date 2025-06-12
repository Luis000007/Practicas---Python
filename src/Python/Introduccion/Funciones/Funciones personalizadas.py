#definición de la función
def greet():
    print("Hello from a function")
    print("Have a great day")

#llamada a la función
greet()

print()
print()

"""
Una función puede requerir argumentos para completar sus tareas. Los argumentos se colocan dentro de los paréntesis () después del nombre de la función.
"""

#definición de la función
def personal_greet(name):
    print("Hello", name)
    print("Have a great day")


#llamadas a la función
personal_greet("Sarah")
personal_greet("Henry")


print()
print()

"""
El resultado de una función puede ser enviado de vuelta con la declaración return. 
Esto es particularmente útil cuando necesitas seguir usando el valor del resultado en tu programa.
"""

#Definir función
def bmi(weight, height):
    index = weight / (height * height)
    return index  #sends the return value back

#Llamando a una función y usando el valor de retorno
patient_5 = bmi(61, 1.83) #stores return value
print("underweight:", patient_5 < 18.5)

#Otra llamada
patient_7 = bmi(75, 1.74)
print("underweight:", patient_7 < 18.5)


print()
print()

"""
Ejemplo de return
"""

def area_cuadro(lado):
    return lado * lado

mi_area = area_cuadro(5)
print(mi_area)  # imprime 25