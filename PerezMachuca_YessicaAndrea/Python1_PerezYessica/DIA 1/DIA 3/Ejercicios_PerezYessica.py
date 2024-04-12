#Imprimir bienvenidos
def funcion1():
    print("funcion 1 de los dos ejercicios")
def esprimo(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def menu():
    print("\nbienvenidos a nuestro programa donde vamos a verificar numeros primos")
    print("por favor puede seleccionar una opcion")
    print("1: Verificar si el numero es primo")
    print("2: Detener el programa")
    print("3: Aqui veras informacion adicional")
    print("")
def infoAdicinal():
    print("\nlos numeros primos son aquellos que se puedeen dividir por 1 o por si mismos")
    print("")
def main():
    while True:
        menu()
        opc = input("por favor puede ingresar el numero de la posicion deseada")
        print("")
        if opc == '1':
            num =int(input("por favor puedes ingresar el numero que deseas verificar"))
            if esprimo(num):
                print(f"{num} como ves el numero si es primo")
            else:
               print(f"{num} como ves el numero no es primo")
        elif opc == '2':
            print("Gracias por haber usado nuestro programa para verificar si un numero es primo o no")
            break
        elif opc == '3':
            infoAdicinal()
        else:
            print("la opcion que has elejido no es correcta por favor puedes ingresar una quer si sea corrdcta")
if __name__ == "__main__":
    main()


#ejercicio 2
#imprimir bienvenido
def funcion2():
    print("funcion 2 de los ejercicios")

import random
import string
    
def generarcontraseña(longitud, mayusculas, minusculas,numeros, simbolos):
    caracteres = ""
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    contraseña="".join(random.choice(caracteres)for _ in range(longitud))
    range(longitud)
    return contraseña
def main():
    print("bienvenidos a nuestro programa para generar contraseñas")
    print("en este programa vamos a generar contraseñas segun tus preferencias")
    while True:
        try:
            longitud=int(input("ingrese por favor la longitud que deseas para la contraseña"))
            break
        except ValueError:
            print("por favor puede ingresar un numero que sea entero")
    mayusculas=input("deseas incluir mayusculas en tu contraseña? (s/n)").lower()=='s'
    minusculas=input("deseas incluir minusculas en tu contraseña? (s/n)").lower()=='s'
    numeros=input("deseas incluir numeros en tu contraseña? (s/n)").lower()=='s'
    simbolos=input("desea incluir simbolos en tu contraseña? (s/n)").lower()=='s'
    contraseñanueva=generarcontraseña(longitud, mayusculas, minusculas, numeros, simbolos)
    print("contraseña nueva",contraseñanueva)
    while True:
        generarotra=input("desea crear otra contraseña? (s/n)").lower()
        if generarotra=='s':
            main()
        elif generarotra=='n':
            print("Gracias por haber usado nuestro programa para generar contraseñas")
            break
        else:
            print("si quiere generar otra contraseña ingrese 's' o 'n' para salir")
if __name__ == "__main__":
    main()





   




    
