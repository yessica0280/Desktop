Algoritmo calcular_lista_de_notas
	Definir num, cantidad Como Entero
	Definir suma Como Real
	num <- 0
	cantidad <- 0
	suma <- 0
	Escribir 'cuantos n�meros vas a ingresar en total? '
	Leer cantidad
	Para i<-1 Hasta cantidad Con Paso 1 Hacer
		Escribir 'numero', i
		Leer num
		suma <- suma+num
	FinPara
	suma <- suma/cantidad
	Escribir 'el promedio de los n�meros ingresados es: ', suma
FinAlgoritmo
