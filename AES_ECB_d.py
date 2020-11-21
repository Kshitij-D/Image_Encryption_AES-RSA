from Crypto.Cipher import AES

#get the password and create cipher
key = input("Enter the password password ")
cipher_ecb_d = AES.new(key.encode("utf8"), AES.MODE_ECB)

#read input image(grayscale)
with open("babo_ecb.bmp", "rb") as f:
    clear = f.read()

#making it a multiple of 16 
clearmod16 = len(clear)%16
cleartrimmed = clear[64:-clearmod16]

#decrypting with ECB
ciphertext_ecb = cipher_ecb_d.decrypt(cleartrimmed)
ciphertext_ecb = clear[0:64] + ciphertext_ecb + clear[-clearmod16:]

with open("tux_ecb_decry.bmp", "wb") as f:
    f.write(ciphertext_ecb)

print("Decrypted AES_ECB image saved as tux_ecb_decry.bmp")
