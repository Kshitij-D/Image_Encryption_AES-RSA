from Crypto.Cipher import AES

#INPUT PASSWORD AND IV
key = input("ENTER THE PASSWORD : ")
iv = input("ENTER THE IV : ")

cipher_d = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))

#reading the encry image
with open("tux_cbc.bmp", "rb") as f:
    clear2 = f.read()

#making it a multiple of 16 
clear2mod16 = len(clear2)%16
clear2trimmed = clear2[64:-2]

#decrypting the image and saving it
decrytext = cipher_d.decrypt(clear2trimmed)
decrytext = clear2[0:64] + decrytext + clear2[-2:]
with open("tux_cbc_decry.bmp", "wb") as f:
    f.write(decrytext)

print("Decrpt Image saved as tux_cbc_decry.bmp")