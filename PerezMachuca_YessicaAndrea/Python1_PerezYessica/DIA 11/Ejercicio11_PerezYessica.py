#Dada una matriz ordenada de numeros enteros distintos y un valor objetivo, devuelve el indice si se encuentra el objetivo. De lo contrario, devuelve el indice donde esraía si se insertara en orden.
#Debe escribir un algoritmocon 0(log n) complejidad de tiempo de ejecucion.
print("Bienvenidos")
print("")
lis = []
lis = input()
element = []
element = input()
for i in range(len(lis)):
    if lis[i] ==element:
        print(i)