from Crypto.Cipher import AES


key = input("Enter a 16 char long password ")

if len(key) != 16:
    print("Password not 16 long, " + len(key))
    key = input("Enter a 16 char long password ")

#ECB MODE
cipher_ecb = AES.new(key.encode("utf8"), AES.MODE_ECB)

#read input image(grayscale)
with open("ba.png", "rb") as f:
    clear = f.read()

#making it a multiple of 16 
clearmod16 = len(clear)%16
print(clearmod16)
cleartrimmed = clear[64:-clearmod16]

#encrypting with ECB
ciphertext_ecb = cipher_ecb.encrypt(cleartrimmed)
ciphertext_ecb = clear[0:64] + ciphertext_ecb + clear[-clearmod16:]

with open("ba_ecb.png", "wb") as f:
    f.write(ciphertext_ecb)

print("Encrypted AES_ECB image saved as ba_ecb.bmp")


















































