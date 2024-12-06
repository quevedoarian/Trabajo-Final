#Por terminal: Generador Contraseña
import secrets, string, sys

diccionario = {
  'letras': string.ascii_letters,
  'numeros': string.digits,
  'caracteres': string.punctuation
}

def generador_contraseña():
    
    password = ''   
    i = 0
    
    
    print("\t⫸------------------------⫷\n")
    print("\t Generador de Contraseñas\n") #A mejorar: Mis diseños graficos
    print("\t⫸------------------------⫷\n")

    #Solicitud de contraseña
    solo_letras = print("1. Generar contraseña solo de Letras.")
    solo_numeros = print("2. Generar contraseña solo de Números.")
    letras_numeros = print("3. Generar contraseña con Letras y Números.")
    letras_numeros_caracteres = print("4. Generar contraseña con Letras, Números y Caracteres.")
    salir = print("0. Salir\n")
    opcion = input("➤  Escriba la opcion seleccionada: ")
    
    
    
    #Opciones
    if opcion == "0":
        print("Saliendo del programa...")
        
    elif opcion == "1":
        longitud = int(input("Escriba la longitud de la constraseña: \n"))
        print("Su nueva contraseña es: ")                            #LETRAS
        for i in range(longitud):
            password += secrets.choice(diccionario['letras'])
        print(f"{password}")
        
    elif opcion == "2": 
        longitud = int(input("Escriba la longitud de la constraseña: \n"))
        print("Su nueva contraseña es: ")                            #NUEMROS
        for i in range(longitud):
            password += secrets.choice(diccionario['numeros'])
        print(f"{password}")
        
    elif opcion == "3":
        longitud = int(input("Escriba la longitud de la constraseña: \n"))
        print("Su nueva contraseña es: ")                            #LETRAS Y NUMEROS
        for i in range(longitud):
            password += secrets.choice(diccionario['letras'] + diccionario['numeros'])
        print(f"{password}")
            
        
    elif opcion == "4":
        longitud = int(input("Escriba la longitud de la constraseña: \n"))
        print("Su nueva contraseña es: ")                            #LETRAS, NUMEROS Y CARACTERES
        for i in range(longitud):
            combinacion =diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']
            password += secrets.choice(combinacion)
        print(f"{password}") 
        
    else:
        print("Por favor, seleccione una opcion correcta.")
    

generador_contraseña ()
    
    
 
 
        
        
        
    
    
    
        


