############################################################
# Matias G. Quevedo - @Gerchu-arq
# Ingreso de números enteros, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

# codigo base para usar funcion ingreso_numero()

def ingreso_numero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
        # Ha habido una excepción <class 'TypeError'>
    except:
        entero = 'error'
    if entero == 'error':
        print("error de validacion")
        # sale del programa
        exit()
    else:        
        return entero
    
def prueba():
    ingreso_numero("Ingresar un numero entero:")

if __name__ == "__main__":
    prueba()
    
