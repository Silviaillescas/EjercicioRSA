# Laboratorio RSA – Cifrado de Información
---

## Descripción del laboratorio

Este laboratorio implementa un sistema de cifrado basado en RSA y cifrado híbrido RSA-OAEP + AES-256-GCM para proteger documentos confidenciales.

El objetivo principal es comprender cómo funciona RSA tanto desde su fundamento teórico como desde su aplicación práctica, y analizar por qué en los sistemas reales no se utiliza RSA para cifrar directamente documentos completos, sino para proteger claves simétricas que luego se usan para cifrar la información.

En este proyecto se desarrollan las siguientes partes:

- Generación de claves RSA seguras
- Exportación de claves en formato PEM
- Cifrado y descifrado de mensajes con RSA-OAEP
- Implementación de cifrado híbrido RSA-OAEP + AES-256-GCM
- Análisis del uso de PEM y del comportamiento probabilístico de OAEP

---

## Escenario

Una firma de abogados necesita transferir documentos legales confidenciales entre sus oficinas de Guatemala City, Miami y Madrid.

Los documentos incluyen:

- contratos  
- acuerdos de confidencialidad  
- datos personales  

El sistema debe garantizar que:

- solo el destinatario pueda leer el documento  
- la información no pueda ser modificada sin detección  
- el proceso sea eficiente incluso para archivos grandes  

Por esta razón se implementa un esquema de cifrado híbrido, en donde RSA protege la clave AES y AES protege el documento real.

---

## Objetivos de aprendizaje

Al completar este laboratorio se espera:

- Explicar la fundamentación matemática de RSA  
- Generar pares de claves RSA de longitud adecuada  
- Implementar cifrado híbrido RSA-OAEP + AES-256-GCM  
- Comprender por qué OAEP es más seguro que esquemas antiguos de padding  
- Analizar la presencia de RSA en protocolos y tecnologías reales  

---

## Estructura del proyecto

EjercicioRSA/

- generar_claves.py  
- rsa_encrypt.py  
- rsa_decrypt.py  
- hybrid_encrypt.py  
- hybrid_decrypt.py  
- private_key.pem  
- public_key.pem  
- README.md  

---

## Requisitos

- Python 3.x  
- PyCryptodome  

---

## Instalación

Instalar la librería necesaria con:

pip install pycryptodome

Si existe conflicto entre pip y python:

python -m pip install pycryptodome

---

## Archivos del proyecto

**generar_claves.py**  
Genera un par de claves RSA de 3072 bits y exporta las claves en formato PEM.

**rsa_encrypt.py**  
Cifra un mensaje usando la clave pública RSA y OAEP.

**rsa_decrypt.py**  
Descifra el mensaje utilizando la clave privada.

**hybrid_encrypt.py**  
Cifra un documento usando AES-GCM y cifra la clave AES con RSA.

**hybrid_decrypt.py**  
Recupera la clave AES con RSA y descifra el documento.

---

## Uso

### 1. Generar claves RSA

python generar_claves.py

Se generan:

- private_key.pem  
- public_key.pem  

Passphrase:

lab04uvg

---

### 2. Cifrado con RSA-OAEP

python rsa_encrypt.py

Salida esperada:

Ciphertext: b'...'

---

### 3. Descifrado con RSA-OAEP

python rsa_decrypt.py

Salida esperada:

Mensaje: b'Secreto'

---

### 4. Cifrado híbrido

python hybrid_encrypt.py

Salida esperada:

clave AES cifrada: b'...'  
nonce: b'...'  
tag: b'...'  
ciphertext: b'...'  

---

### 5. Descifrado híbrido

python hybrid_decrypt.py

Salida esperada:

Documento: b'Documento legal confidencial'

---

## Respuestas de análisis

### ¿Por qué no cifrar el documento directamente con RSA?

RSA no es adecuado para cifrar grandes volúmenes de información porque:

- solo puede cifrar bloques pequeños  
- es computacionalmente más lento  
- no es eficiente para archivos grandes  

Por ello se utiliza cifrado híbrido:

- AES cifra el documento  
- RSA cifra la clave AES  

---

### ¿Qué contiene un archivo .pem?

Un archivo PEM contiene datos criptográficos codificados en Base64.

Estructura:

-----BEGIN PUBLIC KEY-----  
(datos en Base64)  
-----END PUBLIC KEY-----  

Contiene:

- módulo (n)  
- exponente (e)  

---

### ¿Por qué el mismo mensaje cifrado da resultados distintos?

RSA-OAEP introduce aleatoriedad mediante una semilla aleatoria.

Esto provoca que el ciphertext sea diferente cada vez, incluso con el mismo mensaje.

Esto proporciona seguridad semántica y evita ataques por patrones.

---

### ¿Ventaja de AES-GCM?

AES-GCM proporciona:

- confidencialidad  
- integridad  
- autenticación  

Gracias al uso del tag de verificación.

---

### ¿Por qué usar cifrado híbrido?

Porque:

- RSA permite intercambio seguro de claves  
- AES permite cifrado eficiente de datos grandes  
- GCM asegura integridad  

Es el enfoque usado en sistemas reales.

---

## Tecnologías utilizadas

- Python  
- PyCryptodome  
- RSA 3072 bits  
- AES-256-GCM  
- OAEP  
- Formato PEM  

---

## Conclusiones

RSA no debe utilizarse para cifrar directamente archivos grandes.

El cifrado híbrido permite combinar:

- seguridad (RSA)  
- eficiencia (AES)  

OAEP mejora la seguridad al introducir aleatoriedad.

AES-GCM permite garantizar confidencialidad e integridad.

Este enfoque refleja el funcionamiento de sistemas criptográficos modernos.

---
