import random

playing = True
while playing:

    print('1. Piedra ✊')
    print('2. Papel ✋')
    print('3. Tijera ✌️')
    print('4. lagarto 🦎')
    print('5. Spock 🖖')
    option = int(input('¿Que quieres jugar? '))

    if option == 1:
        user = '✊'
        print('Piedra ✊')
    elif option == 2:
        user = '✋'
        print('Papel ✋')
    elif option == 3:
        user = '✌️'
        print('Tijera ✌️')
    elif option == 4:
        user = '🦎'
        print('Lagarto 🦎')
    elif option == 5:
        user = '🖖'
        print('Spock 🖖')
    else:
        print('Opccion invalida')


    game = ['✊', '✋', '✌️', '🦎', '🖖']
    cpu = random.choice(game)

    print()
    print(f'{user} VS {cpu}🤖')

    if user == cpu:
        print('Empate 🤝')

    elif user == '✊' and cpu == '✌️':
        print('¡Ganaste! 🎉')
    elif user == '✋' and cpu == '✊':
        print('¡Ganaste! 🎉')
    elif user == '✌️' and cpu == '✋':
        print('¡Ganaste! 🎉')
    elif user == '✊' and cpu == '🦎':
        print('¡Ganaste! 🎉')
    elif user == '🦎' and cpu == '🖖':
        print('¡Ganaste! 🎉')
    elif user == '🖖' and cpu == '✌️':
        print('¡Ganaste! 🎉')
    elif user == '✌️' and cpu == '🦎':
        print('¡Ganaste! 🎉')
    elif user == '🦎' and cpu == '✋':
        print('¡Ganaste! 🎉')
    elif user == '🖖' and cpu == '✊':
        print('¡Ganaste! 🎉')
    elif user == '✋' and cpu == '🖖':
        print('¡Ganaste! 🎉')

    else:
        print('Gana el CPU 🤖')

    again = input('¿Quieres seguir jugando? (y/n): ').lower()
    if again == 'n':
        playing = False

print('El juego a terminado 👋')
print('✊ ✋ ✌️ 🦎 🖖')