#This is receivers side
# he must have the private key with himself
# and shoud have recieved encry_aes_key and encry_data
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

#read encry key
with open("aes_encry.pem", "rb") as f:
    encry_aes_key = f.read()

#read public key
with open("private.pem", "rb") as f:
    private_key = f.read()

#create RSAobject and make cipher
private_key_obj = RSA.import_key(private_key)
cipher_rsa = PKCS1_OAEP.new(private_key_obj)

#decry the key using private key
decry_aes_key = cipher_rsa.decrypt(encry_aes_key)
print(decry_aes_key)
