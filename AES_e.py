from Crypto.Cipher import AES
#key and iv for CBC mode
iv = "0000111122223333"
key = input("Enter a 16 char long password : ")

while len(key) != 16:
    print("Password not 16 long, ")
    print(len(key))
    key = input("Enter a 16 char long password ")

print("The IV is ", iv)
#creating cipher for encry and decry
cipher = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))

#read input image(grayscale)
with open("babo.bmp", "rb") as f:
    clear = f.read()

#making it a multiple of 16 
clearmod16 = len(clear)%16
cleartrimmed = clear[64:-clearmod16]
#encypting via CBC
ciphertext = cipher.encrypt(cleartrimmed)
ciphertext = clear[0:64] + ciphertext + clear[-clearmod16:]

#saving the encry image
with open("babo_cbc.bmp", "wb") as f:
    f.write(ciphertext)

print("The AES_EBC encry image is saved as tux_cbc.bmp")
print("DO NOT FORGET TO NOTE DOWN IV AND THE PASSWORD FOR DECRYP")