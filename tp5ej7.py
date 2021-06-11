 ############################################################
# Matias G. Quevedo - @Gerchu-arq
# Eimi Saiz - @EimiSaiz
# 7. Distancias, TP5, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

'''
Escriba una funcion que determine la distancia entre dos números.
Implementar este ejercicio sin utilizar la función valor absoluto abs().

Ejemplo La distancia entre -6.5 y 6.0 es 12.5'''

def ingreso_num(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número.
    """
    num_decimal = input(mensaje + " #")
    try:
        num_decimal_2cifras = float("{0:.2f}".format(num_decimal))    # si es un numero con cifras decimales, lo acorta a dos cifras
    except Exception as ex:
# Ha habido una excepción <class 'TypeError'>
        print("Ha habido una excepción", type(ex))
    else:  #Entra en else, no ha ocurrido ninguna excepción
        print("No ha ocurrido ninguna excepción")
        return num_decimal_2cifras
    
def Distancia(nro_1, nro_2):
  distancia = ((nro_1 - nro_2)**2)(1/2)
  return distancia
  
def prueba():
  n1 = ingreso_num("Ingrese primer numero:")
  n2 = ingreso_num("Ingrese segundo numero:")
  print(f'La distancia entre {n1} y {n2} es: {Distancia(n1, n2):.2f}')
  
if __name__ == "__main__":
    prueba()
      
