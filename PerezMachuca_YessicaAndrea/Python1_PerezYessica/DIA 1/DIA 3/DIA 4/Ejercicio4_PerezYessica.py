#ejercicio4
print("Bienvenidos a nuestro programa")
print("")

plata = int(input("por favor puede ingresar la cantidad de dinero que tienes"))
Lista = [1, 5, 10]
for i in Lista:

  if plata <= i:
    queda = plata // i
    print("tenemos " + str(queda) + (' billetes' if plata <= 1 else ' moneda') + " de " + str(i) + " euros ")
    plata = plata % i
 
  
  
 
 
 


