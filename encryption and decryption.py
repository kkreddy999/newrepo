n = input("Enter the string ")
enc_mess = ''
for i in n:                                     
    if i ==' ':
        enc_mess +=' '
    else:
        enc_mess +=chr(ord(i)+3)
print(f"Enc mess {enc_mess}")
 
dec_mess = ''
for i in enc_mess:
    if i ==' ':
        dec_mess +=' '
    else: 
        dec_mess +=chr(ord(i)-3)
print(f"dec mess {dec_mess}")