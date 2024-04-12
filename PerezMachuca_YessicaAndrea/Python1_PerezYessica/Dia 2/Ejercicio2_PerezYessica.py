import random

print("bienvenidos al programa donde adivinaras un numero secreto")
print("despues de cada intento te vamos a dar una retroalimentacion")
print("empecemos")
numerosecreto=random.randint(1,100)

intentos = 0
adivinado = False

while not adivinado:
    suposicion=input("por favor ingresa tu suposicion(entre 1 y 100): ")
    
    if not suposicion.isdigit():
      print("por favor puede ingresar un numero que sea valido")
      continue

    suposicion = int(suposicion)

    if suposicion < 1 or suposicion > 100:
      print("el numero se debe encontrar en el rango del 1 a 100")
      continue
    intentos += 1

    if suposicion < numerosecreto:
        print("el numero es demasiado bajo, por favor intentelo de nuevo")
    elif suposicion > numerosecreto:
        print("el numero es muy alto, por favor puede intentarlo otra vez")
    else: 
        print(f"felicitaciones, has adivinado el numero secretoen {intentos} intentos")
        adivinado = True

jugarotravez = input("deseas volver a jugar? (S/N):")

if jugarotravez.lower() == 'si':
    numerosecreto= random.randint(1, 100)
    intentos = 0
    adivinado = False
    print("genial vamos a jugar otra vez")
else:
    print("finalizamos nuestro juego, gracias por jugar")




