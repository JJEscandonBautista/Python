#Programa que mide la longitud de una palabra.
#La palabra debe ser entre 4 y 8 letras de largo.
#Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, se debe imprimir un mensaje que indique que la palabra es correcta.
#Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: “Hacen falta letras. Solo tiene N letras” (siendo N el número de letras de la palabra).
#Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: “Sobran letras. Tiene N letras” (siendo N el número de letras de la palabra).

palabra = input  ("Ingresa una palabra: ") 

len(palabra)

if len (palabra) == 8:
    print ("La palabra es correcta")

elif len (palabra) <=7:
    print (f"Hacen falta letras. Solo tiene {len(palabra)} letras")

elif len (palabra) >=8:
    print (f"Sobran letras. Esta palabra {len(palabra)} letras")

exit
    