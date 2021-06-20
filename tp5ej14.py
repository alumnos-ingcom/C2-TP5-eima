############################################################
# Matias G. Quevedo - @Gerchu-arq
# Eimi Saiz - @EimiSaiz
# 14. Numero Capicua, TP5, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

from tp4ej1 import ingreso_numero  


def invierte_numero(numero):
    numero_invertido = 0
    while numero > 0:
        digito = numero % 10
        numero_invertido *= 10
        numero_invertido += digito
        numero //= 10
    return numero_invertido 

def es_palindromo(numero):
    numero_invertido = invierte_numero(numero)
    return numero == numero_invertido 

    
def prueba():
    numero = ingreso_numero("Ingrese un número: ")
    numero = abs(numero)
    if es_palindromo(numero):
        print("El número es palíndromo")
    else:
        print("El número no es palíndromo")
    

############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()     
    