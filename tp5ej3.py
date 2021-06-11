############################################################
# Matias G. Quevedo - @Gerchu-arq
# Eimi Saiz - @EimiSaiz
# 3. ¡Tribonacci!, TP5, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

'''La secuencia de Tribonacci es el mismo concepto que la de Fibonacci común, pero acá en lugar de sumar dos terminos;
  se suman de a tres. Tribonacci - OEIS
  Los tres primeros terminos son uno y el termino 4 es la suma de los tres anteriores.

  Implementar una funcion que permita obtener el n-esimo termino de la suceción Tribonacci, 
  siendo este termino un numero entero positivo mayor a 3.'''


from tp4ej1 import ingreso_numero  # uso la funcion ingreso_numero(mensaje) del ej. 1, tp4

def Tribonacci(salida, _n):
  if _n > 3:
    for i in range(_n-3):
      num = sum(salida[-3:])
      salida.append(num)
    return salida
  else:
    return salida[:_n]
  
def prueba():
  n = ingreso_numero("Ingresar valor de n:")
  while n < 0:
    print('El valor ingresado debe ser positivo \n')
    n = ingreso_numero("Ingresar valor de n:")
  print(f'\n{n}-esima Sucesion Tribonacci:{Tribonacci([1,1,1],n)}')
  print(f'Numero{n}-esima de la Sucesion Tribonacci:{Tribonacci([1,1,1],n)[-1]}')

      
if __name__ == "__main__":
    prueba()
