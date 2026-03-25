from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

# mensaje a cifrar
data = b"Secreto secreto secreto"

# generar clave AES de 256 bits
aes_key = get_random_bytes(32)

# cifrar con AES-GCM
cipher_aes = AES.new(aes_key, AES.MODE_GCM)

ciphertext, tag = cipher_aes.encrypt_and_digest(data)

nonce = cipher_aes.nonce

# cifrar clave AES con RSA
with open("public_key.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

cipher_rsa = PKCS1_OAEP.new(public_key)

encrypted_key = cipher_rsa.encrypt(aes_key)

print("clave AES cifrada:", encrypted_key)
print("nonce:", nonce)
print("tag:", tag)
print("ciphertext:", ciphertext)