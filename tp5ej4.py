############################################################
# Matias G. Quevedo - @Gerchu-arq

# 4. Numeros Perfectos, TP5, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

from tp4ej1 import ingreso_numero

def NumeroPerfecto(num):
    
    suma = 0
    for i in range(1,num):
        if (num % (i) == 0):
            suma += (i)
    if num == suma:
        return True
    else:
        return False

def prueba():
    
    num = ingreso_numero("Ingresar numero:")
    
    try:     
         if(num < 0): aux = True
         else: aux = False
    except:
        aux = True
    if aux == True:
        print("ingresar numero entero positivo")
        # sale del programa
        exit()
        
    elif NumeroPerfecto(num):
        print("%s es un numero perfecto" % num)
    else:
        print("%s NO es un numero perfecto" % num)
        
############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()        