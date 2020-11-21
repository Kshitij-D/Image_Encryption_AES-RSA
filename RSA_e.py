from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

#to actually encrypt data we encry the data with AES
#and the rsa encrypted aes key is shared

#encrypt the aes key with (reciever's) public rsa key
#in our case reciever and the sender are the same

#lets read the public key first
with open("public.pem", "rb") as f:
    public_key = f.read()

#generate the RSAobject
public_key_obj = RSA.import_key(public_key)

#Generate the cipher
cipher_rsa_e = PKCS1_OAEP.new(public_key_obj)

#input the key to be encrypted
#and encrypt using the cipher
aes_key = input("Enter the aes_key : ")
aes_key = aes_key.encode("utf-8")
aes_key_encry = cipher_rsa_e.encrypt(aes_key)

#save the encrypted aes key
with open("aes_encry.pem", "wb") as f:
    f.write(aes_key_encry)

print("The encrypted key is saved in aes_encry.pem")