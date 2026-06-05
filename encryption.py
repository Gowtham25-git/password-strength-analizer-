def encrypt(text, key):
    encrypted = ""

    for char in text:
        if char.isalpha():
            shift = key

            if char.isupper():
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            encrypted += char

    return encrypted


def decrypt(text, key):
    decrypted = ""

    for char in text:
        if char.isalpha():
            shift = key

            if char.isupper():
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            decrypted += char

    return decrypted


message = input("Enter Message: ")
key = 3

encrypted_text = encrypt(message, key)
print("Encrypted Message:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted Message:", decrypted_text)
