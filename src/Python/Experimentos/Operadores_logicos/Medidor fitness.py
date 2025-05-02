# Tomar los pasos y los minutos como entradas
steps = int(input())
active_minutes = int(input())

# Almacenar el resultado de las operaciones en la variable
goal_achieved = (steps > 10000) or (active_minutes > 30)

# Mostrar el resultado en la pantalla
print(goal_achieved)