#en esta sección del código se solicitan los valores de el año actual y un año cualquiera. 
#Se hace un acvalidación del dato con un condicional, si es un valor numérico continua el programa y si no envía un mensaje de " Dato erróneo".

entrada = input("Intriduce el año actual: ")

if entrada.isnumeric ():
    año1 = int (entrada)
else:
    print ("Dato erróneo")


entrada = input("Intriduce un año cualquiera: ")

if entrada.isnumeric ():
    año2 = int (entrada)
else:
    print ("Dato erróneo")    


#En esta sección se hace un ciclo if, elif y else con un cálculo matemático en donde si el año actual es mayor al año random, será igualal año actual menos el año random.
#si el año actual y el random son el mismo, se imprime son el mismo año.
#De lo contrario el año actual es menor al año random se hará la resta del año random menos el año actual.

if año1 > año2:
    resultado = año1 - año2 
    print (" Han pasado " + (str(resultado) + " años. "))
elif año1 < año2:
    resultado = año2 - año1
    print (" Faltan " + (str(resultado) + " años. ")) 
else:
    año1 == año2
    print ("es el mismo año")

exit ()

    
  
    



