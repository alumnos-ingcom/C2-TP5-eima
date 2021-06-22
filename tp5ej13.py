############################################################
# Matias G. Quevedo - @Gerchu-arq
# Eimi Saiz - @EimiSaiz
# 13.  Búsqueda de palabras, TP5, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################


'''
Escribir una función que dado un texto y una palabra, retorne la
ubicación de la palabra en el texto o una excepción si la palabra no forma parte del texto.
Considerar solo la primera vez que aparezca la palabra a buscar.'''


def busqueda_de_palabra(palabra):
    with open("datos.txt") as archivo:
        l_datos = []
        busqueda = []
        cant_lineas = 1
        for lineas in archivo:     
           l_datos = lineas.split()       
           for i in range(len(l_datos)):
               if l_datos[i] == palabra:
                   busqueda.append([True,f'linea:{cant_lineas}'])
           cant_lineas = cant_lineas + 1
    archivo.close()       
    return busqueda  

def prueba():
    palabra = input("ingresar palabra a buscar: ")
    try:
          si_esta, nro_de_linea = busqueda_de_palabra(palabra)[0]
        # Ha habido una excepción <class 'TypeError'>
    except:
        si_esta = False
    if si_esta == False:
        print("Excepcion: Palabra no encontrada")
        # sale del programa
        exit()
    else:
        return busqueda_de_palabra(palabra)

 ############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
   print(prueba())         

