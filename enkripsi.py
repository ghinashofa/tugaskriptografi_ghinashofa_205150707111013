def encypt_func(text, key):  
    hasil = ""  
  
    for i in range(len(text)):  
        char = text[i]    
  
        if (char.isupper()):  
            hasil += chr((ord(char) + key - 65) % 26 + 65)   
        else:  
            hasil += chr((ord(char) + key - 97) % 26 + 97)  
    return hasil 

text = input('Input text: ')
key = int(input('Input key: '))

print("Plaintext : " + text)  
print("Urutan Pengulangan : " + str(key))  
print("Hasil (Ciphertext): " + encypt_func(text, key))