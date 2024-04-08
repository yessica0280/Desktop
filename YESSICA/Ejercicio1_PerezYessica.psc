Algoritmo Marca_Celulares
	Definir opc Como entero
	bc = Verdadero
	Mientras bc = Verdadero Hacer
	
		Dimension pf1[50], pf2[50], pf3[50], pf4[50], pf5[50]
		pf1[i] = [20]
		pf2[i] = [15]
		pf3[i] = [20]
		pf4[i] = [15]
		pf5[i] = [20]
		Dimension abc1[50], abc2[50], abc3[50], abc4[50], abc5[50]
		abc1[i] = "Moto g24"
		abc2[i] = "samsung a32"
		abc3[i] = "Oppo a58"
		abc4[i] = "Xiaomi Redmi 13c"
		abc5[i] = "Huawei niva 12i"
		Dimension yes1[50], yes2[50], yes3[50], yes4[50], yes5[50]
		yes1[i] = "Motorola"
		yes2[i] = "Samsung"
		yes3[i] = "Oppo"
		yes4[i] = "Xiaomi"
		yes5[i] = "Huawei"
		
		
		Escribir"    BIENVENIDOS A NUESTRO MENU DE VENTAS     "
		Escribir "11) Mostrar modelos disponibles"
		Escribir "12) Agregar un nuevo modelo"
		Escribir "13) Actualizar cantidad de un modelo"
		Escribir "14) Realizar una venta"
		Escribir "15) Mostrar ventas realizadas"
		Escribir "16) Salir"
		Leer opc
		
		
			
				si opc = 11
					Escribir "Opcion 1"
					Escribir "Marca: ", yes1[i] 
					Escribir "Modelo: ", abc1[i]
					Escribir "precio producto: 599.900" 
					Escribir "cantidad disponibles: 20"
					Escribir " ID Unico: 1 "
					
					Escribir "Opcion 2"
					Escribir "Marca: ", yes2[i]
					Escribir "Modelo: ",abc2[i]
					Escribir "Precio producto: 649.900"
					Escribir "cantidad disponibles: 15"
					Escribir "ID Unico: 2 "
					
					Escribir "Opcion 3"
					Escribir "Marca: ", yes3[i]
					Escribir "Modelo: ",abc3[i]
					Escribir "Precio producto:849.900"
					Escribir "Cantidad disponible: 20"
					Escribir "ID Unico 3 "
					
					Escribir "Opcion 4"
					Escribir "Marca: ", yes4[i]
					Escribir "Modelo:",abc4[i]
					Escribir "precio producto:514.900"
					Escribir "Cantidad disponible: 15"
					Escribir "ID Unico: 4 "
					
					Escribir "Opcion 5"
					Escribir "Marca: ", yes5[i]
					Escribir "Modelo:",abc5[i]
					Escribir "Precio producto:899.900"
					Escribir "Cantidad disponible: 20"
					Escribir "ID Unico: 5"
					
					Escribir " por favor para volver al menu principal precione (1)"
					Escribir " por favor para finalilzar el programa presione (6)"
					Leer opc
					Limpiar Pantalla
		        FinSi
				Si opc = 12 Entonces
					Escribir "por favor puede llenar las siguientes preguntas"
					
					Escribir "De que marca es el celular que quieres agregar a la lista"
					Leer MARCA
					Escribir "Cual es el modelo que quieres agregar a la lista"
					Leer MODELO
					Escribir "cual es el precio del producto que quieres agregar a la lista"
					Leer PRECIO
					Escribir "cual es el ID Unico del producto que quieres agregar ala lista"
					Leer unico
				FinSi
				
					Si opc = 6 Entonces
						bc = Falso
					FinSi
		
	FinMientras
	
FinAlgoritmo
