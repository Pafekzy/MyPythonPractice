def caesar_cipher(text, shift, encrypt=True):
    if not encrypt:
        shift = -shift
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char.lower()) - 97 + shift_amount) % 26 + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

text = input("Enter text to encrypt/decrypt: ")
shift = int(input("Enter shift amount: "))
encrypt = input("Encrypt or decrypt (e/d)? ").lower() == 'e'
print("Result:", caesar_cipher(text, shift, encrypt))


# Caesar Cipher for Encryption and Decryption