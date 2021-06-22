########################################################
# Matías G. Quevedo - @Gerchu-arqv
# Eimi Saiz - @EimiSaiz
# TP 5 - Eje. 10: Texto binario
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def decimal_to_binary(decimal): 
    if(decimal > 1): 
        decimal_to_binary(decimal//2) 
    print(decimal%2, end=' ')

def prueba():
    decimal = int(input("Ingrese un número en base 10.\n"))
    print("Representación binaria:")
    decimal_to_binary(decimal)
    pass

if __name__ == "__main__":
    prueba()
