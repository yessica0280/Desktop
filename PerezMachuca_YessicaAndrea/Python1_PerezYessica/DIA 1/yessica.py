#-----------------------------------------------
#-----------DIA CHEAT SHEET PYTHON--------------
#-----------------------------------------------

#Imprimir hola mundo
print("hola mundo.")

#datos primitivos

#numero
numerito = 1 #nombrevariable = valor
print(numerito)#imprimir(variable)
print(type(numerito))#imprimir(tipo(variable))

#Decimal
numeritoDecimal=1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
mibooleanito = True
print(mibooleanito)
print(type(mibooleanito))

#Cadena de texto
texto = "mi tibu"
print(texto)
print(type(texto))

#Ejercicio 1:ingresar la informacion por teclado(input)
print("hola como veras es mi primer python")
print("por favor puede ingresar su nombre")
nombre = input()
print("bienvenido al nuestro sistema"), nombre,". gracias por usar nuestro programa."

#Ejercicio 2:conversion de tipos de variables
Dato =int(input("ingresar edad:"))
print(Dato)
print(type(Dato))
resultado = Dato + 1
print(resultado)

#Ejercicio 3: bucles for y while
dollar = 200
while dollar<= 2010:
    print(dollar)
    dollar +=1

    print("--------------------------")

    for i in range(4):
        print(i)
    print("--------------------")
    miLista = ["huevos", "galletas", "cafe", "azucar"]
    for nombre in miLista:
        print(nombre)

#Ejercicio 4: funciones
#funcion 1 suma de dos nuemeros 
        def suma(n1, n2):
          #aqui sumamos los dos numeros y se devolvera el resultado.     
            return n1 + n2
        resultadoSuma = suma(7, 9)
        print("la suma sera de:",resultadoSuma)
#funcion 2 restar dos numeros
def res(n1, n2):
    #aqui se resta el numero 2 del primero y nos arroja el resultado
    return n1 - n2
resultadoResta = res(7, 9)
print("la resta sera:", resultadoResta)
#funcion 3 multiplicar dos numeros
def multiplicar(n1, n2):
    #aqui multiplica los dos numeros y nos dara el resultado
    return n1 * n2
resultadoMultiplicar = multiplicar(7, 9)
print("la multiplicacion nos daria:", resultadoMultiplicar)
#funcion 4 dividir dos numeros
def divi(n1, n2):
    #aqui divide el numero 1 con el numero 2 y nos da el resultado
    if n2 == 0:
        return "error: no es posible dividir por cero"
    else:
        return n1 / n2
resultadoDivision = divi(6, 3)
print("la dividion nos daria", resultadoDivision)


#Desarrollado por Yessica Andrea Perez Machuca C.C: 1005044824