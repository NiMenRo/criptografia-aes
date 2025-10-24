"""
Autores:    Nicolas Mauricio Rojas - 202259460
            Esteban Alexander Revelo - 2067507
"""
from Crypto.Cipher import AES
from Crypto.Util import Counter

clave = b'A\x83\xbeU\xd7\xa9b\x18\x85AN0\xbft\xc3\xab'


texto_cifrado_ecb = b'\xd5\x8b\xc2\xd0F\xc0w\xfe\xc1\x12\xaaX\x8f}{)i[\xf1\xc7\x9d\x1d\x08\xcd\xc2\xd8>;\r\xef\xce\xec\x89\xbd\xeb{\xe6mY\xcev\xb9\xdb\x06\x17\xd9\xd6cG6\xb4\xcfN\xf9\x15.\xbe\xed\xe7\xee#\xd0\xd9\x03\xb9l\xbap\x0c\x9c\xbe\xc3\xe1\xae\x86~pk\\\x0f' 
texto_cifrado_ctr = b'{\x9a`\x04\x80\xc5\x026D\x1f\xaf\x9c&\xd1\x83\x0c\xf2wL\xd6F}\xd35B.\xb4\xe5\xb1^\x05 P\xc8\xe8\x89\xe1\xf7;G\x13\xf0\xccbs\xe8\x121\x8b4\xbf\xda\x93v\xcb\xe4\xf8g\xe72\xc5~\x97\x01TR\x9d\x0b'

# ---------- DESCIFRADO MODO ECB ----------#
cipher_ecb = AES.new(clave, AES.MODE_ECB)

texto_descifrado_ecb = cipher_ecb.decrypt(texto_cifrado_ecb)
print("\n--- DESCIFRADO ECB ---")
print("Texto descifrado (bruto):", texto_descifrado_ecb)
print("Texto descifrado (utf-8):", texto_descifrado_ecb.decode('utf-8', errors='replace'))


# ---------- DESCIFRADO MODO CTR ----------#
ctr = Counter.new(128)
cipher_ctr = AES.new(clave, AES.MODE_CTR, counter=ctr)
texto_descifrado_ctr = cipher_ctr.decrypt(texto_cifrado_ctr)

print("\n--- DESCIFRADO CTR (con contador 128) ---")
print("Texto descifrado (bruto):", texto_descifrado_ctr)
print("Texto descifrado (utf-8):", texto_descifrado_ctr.decode('utf-8', errors='replace'))