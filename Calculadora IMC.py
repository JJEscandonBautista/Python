# Este programa calcula el Indice de Masa corporal el cual se calcula con la fómula Peso / estatura2   -> Peso sobre estatura al cuadrado. 
# El programa solicita nombre, edad, pesos y estatura de la persona y genera el cálculo.

Nombre = input ("Ingresa tu nombre: ")
Edad = int (input ("Ingresa tu edad: "))
Peso = float (input("Ingresa tu peso: "))
Estatura = float(input("Ingresa tu estatatura: "))

IMC = Peso / (Estatura**2)


#Esta sección genera la impresión del nombre y la leyenda "Tu índice de masa corporal es: y el resultado de la operación"
print ("Nombre: " + Nombre)
print ("Edad: " +  (str(Edad) + " años "))
print ( "Peso: " + (str(Peso) + (" kg. ")))
print ( "Estatura: " + (str(Estatura) + (" mts. ")))
print (str (Nombre + " tu IMC es de: " + str(IMC))) 






