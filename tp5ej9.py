############################################################
# Matias G. Quevedo - @Gerchu-arq

# 9.  Factoriones, TP5, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

from tp4ej1 import ingreso_numero 

def factorion(n) :
    # lista de factoriales, 10! > 1.499.999, entonces uso como maximo 10
    MAX = 10
    fact = [0] * MAX
    fact[0] = 1
    lista_factorion = []
    
    # factoriales para luego comparar
    
    for i in range(1, MAX) :
        fact[i] = i * fact[i - 1]

    copia_numero = n

    # para almacenar los factoriales
    # de los digitos de n
    sum = 0
    while (n > 0) :

        # consigo el ultimo digito
        d = n % 10
        lista_factorion.append(d) # almaceno los posibles factoriones
        sum += fact[d]

        # Remuevo ultimo digito
        n = n // 10
        
    if (sum == copia_numero):
        print(lista_factorion[::-1])
        return True
    
    return False
    

def prueba():
    
    n = 1
    limite = 1499999
    
    while (n < limite):
        if (factorion(n)): print("....................")
        n = n + 1
            
 ############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()  
    

  


