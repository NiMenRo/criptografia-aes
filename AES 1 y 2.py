"""
Autores:    Nicolas Mauricio Rojas - 202259460
            Esteban Alexander Revelo - 2067507
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util import Counter

# Parámetros 
texto_plano = "texto secreto"
clave = b'A\x83\xbeU\xd7\xa9b\x18\x85AN0\xbft\xc3\xab'  # clave de 16 bytes (128 bits)
modo = AES.MODE_ECB # Modo de operacion ECB (Electronic Codebook)

# ------------------------ MODO ECB ------------------------

print("\n--- MODO ECB ---\n")

# Crear el cifrador AES
cipher = AES.new(clave, modo)

# Convertimos el texto a bytes
texto_bytes = texto_plano.encode('utf-8')

print("Texto plano original:", texto_plano)
print("Longitud del texto:", len(texto_bytes), "bytes")
print("\nCifrando sin aplicar padding...\n")

# Intentar cifrar sin padding
try:
    texto_cifrado_error = cipher.encrypt(texto_bytes)
    print("Texto cifrado (sin padding):", texto_cifrado_error.hex())
except ValueError as e:
    print("Error al cifrar sin padding:", e)

# Aplicamos padding al texto plane en bytes
texto_padded = pad(texto_bytes, AES.block_size)
print("\nLongitud del texto con padding:", len(texto_padded), "bytes")

texto_cifrado = cipher.encrypt(texto_padded)

print("\nTexto cifrado con padding:", texto_cifrado.hex())
print("Longitud del texto cifrado:", len(texto_cifrado), "bytes")


# ------------------------ FIN MODO ECB ------------------------


# ------------------------ MODO CTR ------------------------

print("\n\n--- MODO CTR ---\n")

# Crear un contador (necesario en CTR)
ctr = Counter.new(128)
cipher = AES.new(clave, AES.MODE_CTR, counter=ctr)

# Cifrar (CTR no requiere padding)
texto_cifrado = cipher.encrypt(texto_plano.encode('utf-8'))

# Mostrar resultados
print("Texto plano:", texto_plano)
print("Texto cifrado en bytes:", texto_cifrado)
print("Texto cifrado:", texto_cifrado.hex())
print("Longitud del texto cifrado:", len(texto_cifrado), "bytes")