########################################################
# Matías G. Quevedo - @Gerchu-arqv
# Eimi Saiz - @EimiSaiz
# TP 5|Eje 8. El Cifrado del César
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

# Cantidad de posiciones: 3.
    
shift = 3
texto_cifrado = "KHOOR ZRUOG"
texto_corriente = ""
for c in texto_cifrado:
    # Chequear si el caracter es una letra mayuscula.
    if c.isupper():
        # find the position in 0-25
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        # perform the negative shift
        new_index = (c_index - shift) % 26
        # convert to new character
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        # append to plain string
        texto_corriente = texto_corriente + new_character
    else:
        # since character is not uppercase, leave it as it is
        texto_corriente += c
print("Texto cifrado:",texto_cifrado)
print("Texto decifrado:",texto_corriente)