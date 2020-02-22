import sys

plaintext = list(sys.argv[1])
key = str(sys.argv[2])

print("Plaintext: " + "".join(plaintext) )
print("key: " + key)
for i in range(0,len(plaintext)):
    newChar = ord(plaintext[i]) + ord(key[i%len(key)])-96
    if(newChar > 122):
        newChar -= 26
    plaintext[i] = chr(newChar)

print("The ciphertext is:" + "".join(plaintext))