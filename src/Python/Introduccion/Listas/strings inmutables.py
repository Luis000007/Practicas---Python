animal = "Dog"
print(animal[0])
print(animal[1])
print(animal[2])

print()
print()

"""Las cadenas de texto son inmutables lo que significa que no puedes cambiar los caracteres de una cadena de texto, de lo contrario dará error """

# Las cadenas de texto son inmutables
word = "car"
word[2] = "t"


# Las listas son mutables
words = ["car", "dog", "bird"]
words[0] = "cat"
print(words)