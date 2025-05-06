# tomar la población celular inicial como entrada
cells = int(input())

# tomar el número de días como entrada
days = int(input())

# inicializar el contador de días
counter = 1


# completar el bucle while
while counter <= days:
    cells = cells * 2


    # Mensaje diario
    print("Day " + str(counter) + ": " +str(cells))
    counter = counter + 1