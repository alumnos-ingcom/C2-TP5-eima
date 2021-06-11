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

from tp4ej1 import ingreso_numero  # uso la funcion ingreso_numero(mensaje) del ej. 1, tp4

def Distancia(nro_1, nro_2):
  distancia = ((nro_1 - nro_2)**2)**(1/2)
  return distancia
  
def prueba():
  n1 = ingreso_numero("Ingrese primer numero:")
  n2 = ingreso_numero("Ingrese segundo numero:")
  print(f'La distancia entre {n1} y {n2} es: {Distancia(n1, n2):.2f}')
  
if __name__ == "__main__":
    prueba()
      
