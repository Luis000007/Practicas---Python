from playsound import playsound

class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre

    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Wooof-wooof"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miaaaau"


mascota1 = Perro("Saco de pulgas")
mascota2 = Gato("Tonchi")


print(mascota1.obtener_nombre(), "dice:", mascota1.hacer_sonido())
playsound(r'C:\Users\PC\Downloads\dog_barking-6296.mp3')

print(mascota2.obtener_nombre(), "dice:", mascota2.hacer_sonido())
playsound(r'C:\Users\PC\Downloads\cat-meow-12-fx-306191.mp3')


