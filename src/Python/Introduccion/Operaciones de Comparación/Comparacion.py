print(30<25)
print(5 < 9)
print(50 > 100)
print()
print()
print(type(5 < 9))
print(type(50 > 100))
print(type(True))
print(type(False))
print(type("Holis"))
print(type(34))
print()
print()

## Si son diferentes siempre dara False, tambien con doble False
print(True and False)
print(False and True)
print(True and True)

print()

## Siempre y cuando haya un True, dara True
print(True or False)
print(False or True)

print()
print()

## Puedes almacenar operaciones de comparacion en variables
heart_rate = 165
peak_rate = heart_rate > 160
print(peak_rate)

print()

light_on = True
door_locked = False
print(light_on or door_locked)
print(light_on and door_locked)