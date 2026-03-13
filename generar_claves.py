from Crypto.PublicKey import RSA

PASSPHRASE = "lab04uvg"

def generar_par_claves(bits: int = 3072):

    key = RSA.generate(bits)

    private_key = key.export_key(
        passphrase=PASSPHRASE,
        pkcs=8,
        protection="scryptAndAES128-CBC"
    )

    public_key = key.publickey().export_key()

    with open("private_key.pem", "wb") as f:
        f.write(private_key)

    with open("public_key.pem", "wb") as f:
        f.write(public_key)

    print("Claves generadas")

if __name__ == "__main__":
    generar_par_claves()