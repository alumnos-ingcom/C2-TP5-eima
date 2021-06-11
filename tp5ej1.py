  
############################################################
# Matias G. Quevedo - @Gerchu-arq
# Eimi Saiz - @EimiSaiz
# 1. Pares e impares, TP5, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

# Escribir una función que retorne True cuando un número entero es par y False cuando no lo sea, sin utilizar módulo.(%)

from tp4ej1 import ingreso_numero  # uso la funcion ingreso_numero(mensaje) del ej. 1, tp4

def Par_o_Impar(_numero)
  cociente = int(_numero/2)
  resto = _numero - cociente*2
  if resto == 0 : return True
  else: return False
  
def prueba():
  numero = ingreso_numero("Ingresar numero:")
  if (Par_o_Impar(nnumero)): print(f'{numero} es Par')
  else: print(f'{numero} es Impar')
      
if __name__ == "__main__":
    prueba()
