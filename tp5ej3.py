############################################################
# Matias G. Quevedo - @Gerchu-arq

# 3. Tribonacci! , TP5, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################


# La secuencia...

from tp4ej1 import ingreso_numero  # uso la funcion ingreso_numero(mensaje) del ej. 1


def Tribonacci(salida, _n):
    if _n > 3:
        for i in range(_n-3):
            num = sum(salida[-3:])
            salida.append(num)
        return salida
    else:
        return salida[:_n]

def prueba():
    n = ingreso_numero("Ingresar valor de n:")
    while n < 0:
            print('El valor ingresado debe ser positivo \n')
            n = ingreso_numero("Ingresar valor de n:")

    print(f'\n{n}-esima Sucecion Tribonacci:{Tribonacci([1,1,1],n)}')    
    print(f'Numero {n}-esimo de la sucecion Tribonacci:{Tribonacci([1,1,1],n)[-1]}')
    

 ############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()         

