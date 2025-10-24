"""
Autores:    Nicolas Mauricio Rojas - 202259460
            Esteban Alexander Revelo - 2067507
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util import Counter

# Texto y clave original de 128 bits
texto_plano = "texto secreto"
clave = b'A\x83\xbeU\xd7\xa9b\x18\x85AN0\xbft\xc3\xab'  # 16 bytes

# Extender la clave a 256 bits (32 bytes)
clave_256 = clave * 2
print("Longitud de la clave:", len(clave_256), "bytes")

# ------------------------ MODO ECB (256 bits) ------------------------
cipher_ecb = AES.new(clave_256, AES.MODE_ECB)
texto_bytes = texto_plano.encode('utf-8')
texto_padded = pad(texto_bytes, AES.block_size)
texto_cifrado_ecb = cipher_ecb.encrypt(texto_padded)

print("\n--- MODO ECB (256 bits) ---")
print("Texto cifrado (hex):", texto_cifrado_ecb.hex())
print("Longitud del texto cifrado:", len(texto_cifrado_ecb), "bytes")

# ------------------------ MODO CTR (256 bits) ------------------------
ctr = Counter.new(128)
cipher_ctr = AES.new(clave_256, AES.MODE_CTR, counter=ctr)
texto_cifrado_ctr = cipher_ctr.encrypt(texto_plano.encode('utf-8'))

print("\n--- MODO CTR (256 bits) ---")
print("Texto cifrado (hex):", texto_cifrado_ctr.hex())
print("Longitud del texto cifrado:", len(texto_cifrado_ctr), "bytes")
