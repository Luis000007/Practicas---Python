"""
Los bucles while repiten el código mientras se cumple una condición.

Por ejemplo, un vendedor de boletos en un teatro venderá boletos repetidamente hasta que todos los asientos estén ocupados.
"""
print("Condicion por cumplir:")
seats= 10 # número inicial de asientos
while seats > 0: # ¿hay asientos disponibles?
    print("Sell ticket") # boleto vendido
    seats = seats - 1 # número de asientos actualizado  / si se comenta esta linea pasa lo de abajo

    """
Con los bucles while, puedes encontrarte con lo que se conoce como un bucle infinito. Esto ocurre cuando la condición es siempre verdadera y el código nunca deja de repetirse.

Los contadores te ayudan a evitar bucles infinitos.
    """

print()
print()
print("Aumento:")

counter = 0
while counter < 4:
    print(counter)
    counter = counter + 1