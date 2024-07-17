#Solicita una contraseña cuyo valor inicial sea un número, se establece una contraseña predeterminada.


Pass = "43BN"
cont = 1
nombre = input ("Ingresa tu contraseña: ")
while cont <=3: 
    
    if nombre == Pass:
        print ("Bienvenido, Contraseña correcta. ")
        break
    else:
        nombre = input ("contraseña incorrecta,intenta nuevamente: ")
    cont = cont + 1
exit







    

   

 
