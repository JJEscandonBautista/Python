#Bucle infinito donde se solicita al usuario ingresar una letra.
#Se da la opción cero para cerrar el bucle.
# Se imprime la letra anterior y posterior a la ingresada.

import string


def listaletras():
    return list(string.ascii_lowercase)


print(listaletras())




while (True):
        letra = input ("Ingresa una letra, cero para salir: ")
        print (letra)   
        if letra == "0":
           break

print ("FIN")
    
        
     
   
   
    



      


        
    
    

 



   
    




   
    



