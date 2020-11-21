#Lets create a RSA key
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

key = RSA.generate(2048)  
private_key = key.export_key()
public_key = key.publickey().export_key()

#create private and public files
with open("private.pem", "wb") as f:
    f.write(private_key)
with open("public.pem", "wb") as f:
    f.write(public_key)

print("Private and Public keys generated and saved to disk :)")
