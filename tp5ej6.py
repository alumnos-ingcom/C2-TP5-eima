############################################################
# Matias G. Quevedo - @Gerchu-arq
# 6. Parentesis balanceados, TP5, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################



def parentesis_balanceados(cadena):
    
    mir_dict = {'[':']', '{':'}', '(':')'}
    invertido = []
    aux = 0

    for c in cadena:
        if c == '['or c =='{'or c =='(':   
            invertido.append(mir_dict[c])
            aux = aux + 1
        elif len(invertido) == 0:  # hay mas parentesis abiertos que cerrados
            aux = 1
            break
        elif c == invertido[-1]: # comparo si el parentesis cerrado es el inverso
                                 # del ultimo parentesis abierto 
                aux = aux - 1
                invertido.remove(c)
                
       # si unos parentesis consecutivos (abierto y cerrado)
       # no coinciden, o si se ingresa otro caracter no valido,  entonces salir 
        else:        
            aux = 1
            break
        
    if aux == 0: return True
    else: return False

def prueba():
    cadena = input("Ingresar cadena de parentesis a validar: ")
    print(parentesis_balanceados(cadena))
    
############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()
    

