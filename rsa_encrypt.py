from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

mensaje = b"Hola UVG"

# cargar clave pública
with open("public_key.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

cipher = PKCS1_OAEP.new(public_key)

ciphertext = cipher.encrypt(mensaje)

print("Ciphertext:", ciphertext)