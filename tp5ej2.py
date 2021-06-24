############################################################
# Matias G. Quevedo - @Gerchu-arq

# 2. Fibonacci, TP5, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

from tp4ej1 import ingreso_numero
 
def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
def prueba():
    
    n = ingreso_numero("Ingresar valor de n:")
    try:     
         if(n < 0): aux = True
         else: aux = False
    except:
        aux = True
    if aux == True:
        print("entrada incorrecta")
        # sale del programa
        exit()
    else:
        print(Fibonacci(n))
    
    
############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()