############################################################
# Matias G. Quevedo - @Gerchu-arq
# Eimi Saiz - @EimiSaiz
# Ingreso de números enteros, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################


# Reemplazar por las funciones del ejercicio
# No esta empezado, aun....
def ingreso_numero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except Exception as ex:
# Ha habido una excepción <class 'TypeError'>
        print("Ha habido una excepción", type(ex))
    else:  #Entra en else, no ha ocurrido ninguna excepción
        print("No ha ocurrido ninguna excepción")
        return entero
'''
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero
'''
def prueba():
    print(f'numero entero:{ingreso_numero("Ingresar un numero entero:")}')
     
     
 ############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
   prueba()
