########################################################
# Matías G. Quevedo - @Gerchu-arqv
# Eimi Saiz - @EimiSaiz
# TP 5|Eje 10. Texto binario
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def DecimalToBinary(Decimal): 
    if(Decimal > 1): 
        DecimalToBinary(Decimal//2) 
    print(Decimal%2, end=' ')

def prueba():
    Decimal = int(input("Ingrese un número en base 10.\n"))
    print("Representación binaria:")
    DecimalToBinary(Decimal)
    pass

if __name__ == "__main__":
    prueba()
    