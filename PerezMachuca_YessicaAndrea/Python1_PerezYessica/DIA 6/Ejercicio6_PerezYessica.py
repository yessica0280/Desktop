#Ejercicio 6
num = []
dato=int(input("por favor puedes ingresar los numeros"))
for x in range(0, dato):
    ingresado = input("")
    num.append(ingresado)
    num.sort()
print(num)
sinduplicado=sorted(list(set(num)))
print(sinduplicado)
ordenados=sorted(num)
#Desarrollado por Yessica Andrea Perez Machuca C.C 1005044824 Grupo:T2