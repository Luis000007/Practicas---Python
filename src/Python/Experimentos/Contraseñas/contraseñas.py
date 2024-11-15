import itertools
from timeit import repeat
import zipfile

name = 'IFE.zip'
char = '0123456789'

print("Programa que extrae los archivos de un zip protegido")
input("Presione enter para comenzar.........")

for guess in itertools.product(char, repeat=5):
    guess = ''.join(guess)
    print("Probando contraseña:", guess)
    try:
        with zipfile.ZipFile(name, 'r') as zip_ref:
            zip_ref.extractall(pwd=bytes(guess, 'utf-8'))
            print("¡Contraseña encontrada!: ", guess)
            break
    except Exception as e:
        pass

input("Presione enter para finalizar el programa.")
