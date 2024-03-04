import time
import os
#Creamos una funcion para encriptar
def cifrador(texto , clave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.!?#'
    texto_Cifrado = ""
    contador_Clave = 0
    # Iteramos sobre la cadena "texto" 
    for caracter in texto: 
        # Revisamos si el caracter se encuentra en el alfabeto
        if caracter in alfabeto:
            indice_Caracter = alfabeto.find(caracter)
            indice_Clave = alfabeto.find(clave[contador_Clave % len(clave)])
            nuevo_Indice = (indice_Caracter + indice_Clave) % len(alfabeto)
            texto_Cifrado += alfabeto[nuevo_Indice]
            contador_Clave += 1
        # En caso de que el caracter no se encuentre en el alfabeto lo agrega tal cual al texto encriptado
        else:
            texto_Cifrado += caracter
    return texto_Cifrado

def descifrador(texto_Cifrado, clave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.!?#'
    texto_Descifrado = ""
    contador_Clave = 0
    for caracter in texto_Cifrado: 
        if caracter in alfabeto:
            indice_Caracter = alfabeto.find(caracter)
            indice_Clave = alfabeto.find(clave[contador_Clave % len(clave)])
            # Lo que cambia ademas de la variable "texto_Cifrado" por "texto_Descifrado", es la operacion del nuevo indice.
            # En lugar de sumar los indices ahora los restamos
            nuevo_indice = (indice_Caracter - indice_Clave) % len(alfabeto)
            texto_Descifrado += alfabeto[nuevo_indice]
        else:
            texto_Descifrado += caracter
        contador_Clave += 1
    return texto_Descifrado


def main():
    while True:

        print("+--------@SyD-------+")
        print("|                   |")
        print("|   1. Cifrar       |")
        print("|   2. Descifrar    |")
        print("|   3. Salir        |")
        print("|                   |")
        print("+-------------------+")
        opcion = (input("Elige una opción: "))
        if opcion == "1":
            os.system("cls")
            texto = input("Ingrese el texto a cifrar: ")
            clave = input("Ingrese la clave que se usara: ")
            print(f"El texto cifrado es: {cifrador(texto,clave)}")
            break
            
        elif opcion == "2":
            os.system("cls")
            texto_Descifrar = input("Ingresa el texto a descifrar: ")
            clave = input("Ingresa la clave: ")
            print(f"Tu texto plano es: {descifrador(texto_Descifrar,clave)}")
            break
            
        elif opcion == "3":
            print("Saliendo...")
            time.sleep(1)
            break
        
        elif opcion != isinstance(opcion, int):
            print("Opción no valida. Por favor eliga 1, 2 o 3")

print('''
███████╗███╗░░██╗░█████╗░██████╗░██╗██████╗░████████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝████╗░██║██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
█████╗░░██╔██╗██║██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░███████║██║░░██║██║░░██║██████╔╝
██╔══╝░░██║╚████║██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░██╔══██║██║░░██║██║░░██║██╔══██╗
███████╗██║░╚███║╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░██║░░██║██████╔╝╚█████╔╝██║░░██║
╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

██╗░░░██╗██╗░██████╗░███████╗███╗░░██╗███████╗██████╗░███████╗
██║░░░██║██║██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔════╝
╚██╗░██╔╝██║██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝█████╗░░
░╚████╔╝░██║██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══╝░░
░░╚██╔╝░░██║╚██████╔╝███████╗██║░╚███║███████╗██║░░██║███████╗
░░░╚═╝░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚══════╝''')
main()