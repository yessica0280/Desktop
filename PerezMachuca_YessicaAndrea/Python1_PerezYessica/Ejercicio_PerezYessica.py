
import json

with open("large-file.json",encoding= "utf-8") as openfile:
    miJSON = json.load(openfile)
    '''
    print(miJSON)
    '''

#print(type(miJSON))


eventocrear=[]
def crear(nuevoid, nuevotype, nuevoactor, nuevorepo):
 eventocrear = {
   
    'id' : nuevoid,
    'type': nuevotype,
    'actor': nuevoactor,
    'repo': nuevorepo
   }
 
eventocrear.append(eventocrear)


'''
for i in range (5):
  print(miJSON[i])
'''


        


'''
crearEventos=[]
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])

#print(crearEventos[5]['actor']['id'])
    
for q in range (5):
    print("#######################")
    print("#### Evento # ",q+1 ,"##")
    print("#######################")
    print("ID: ",crearEventos[q]['id'])
    print("Tipo:",crearEventos[q]['type'])
    print("Actor:")
    print("------- ID:",crearEventos[q]['actor']['id'])

crearEventos[0]['id']=256
with open("eventos.json","w") as outfile:
    json.dump(crearEventos,outfile)
'''    
booleano = True
while booleano == True:
  print("######### MENU ################")
  print("")
  print("1: Deseas crear un evento")
  print("2: Deseas actualizar un evento")
  print("3: Deseas revisar algun evento")
  print("4: Deseas eliminar algun evento")
  print("")
  opc=input("por favor puede ingresar la opcion deseada ")
  if opc=="1":
      nuevoid = input("ingresa el id del nuevo evento")
      nuevotype =input("ingresa el nuevo type del evento")
      nuevoactor= input("ingresa el nuevo actor del evento")
      nuevorepo = input("ingresa el nuevo repo del evento")
  
         
  break

## Desarrollado por Yessica Andrea Perez Machuca C.C 1005044824 Grupo:T2

