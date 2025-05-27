"""
El rebanado te permite extraer una porción de una lista. Los índices de inicio y fin están separados por dos puntos :
"""
"""
Las comas, son los numeros, empeuza desde 1, y el borde de la izquierza es 0.
"""

animals =["cat", "dog", "bird", "cow"]
print(animals[1:3])

print()
print()

"""
Tambien puede aplicarse a Cadenaz de texto
"""
vehicle = "airplane"
print(vehicle[0:3])

print()
print()

"""
Cuando haces segmentación, puedes omitir el índice de inicio. Esto significa que estarás segmentando desde el primer elemento.
"""
cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[:3])

print()
print()

"""
Cuando haces segmentación, puedes omitir el índice de parada. Esto significa que estarás segmentando hasta el último elemento.
"""

cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[1:])

print()
print()

"""
Python admite "indexación desde el final", llamada indexación negativa. Esto significa que el último valor de una secuencia tiene un índice de -1.
Se cuenta desde las comillas tambien
"""
animals = ["cat", "dog", "bird", "cow"]
print(animals[-1]) # Último elemento
print(animals[-2]) # Penúltimo elemento
print(animals[-3:]) # Últimos 3 elementos
print(animals[-3:-1])


"""
Puedes combinar la indexacion positiva con la negativa
"""
c = ['$', '£', '€', '¥']
print(c[1:-1])