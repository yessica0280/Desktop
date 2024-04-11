#Ejercico 1 serie fibonacci
#imprimir bienvidos
print("bienvenidos")

print("por favor ingresa tu nombre")
nombre=input()

pos=int(input("por favor puede escribir que posicion quiere en la serie fibonacci: "))
ans = input("deseas ver toda la serie? (S/N): ")
ifibo = 0
ffibo = 1
for x in range(0,pos):
    if x == 0:
        ffibo = 0
    elif x == 1:
        ffibo = 1
    if ans =="S" or ans =="s":
        print(f'posicion:{x+1:>4}--valor en la serie fibonacci:{ffibo:>10}')
    sum =ffibo
    ffibo = ffibo + ifibo
    ifibo = ffibo - ifibo
print(f'\nposicion fin:{x+1:>4}--valor en la serie de fibonacci{sum:>10}')
continuar = int(input("deseas seguir en el programa:? <1=si, 0=no>:"))