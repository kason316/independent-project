def vigenere_encrypt_function(plaintext, key):
    result = ""
    key_index = 0
    for c in plaintext:
        if c.isupper():
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - 65
            new_char = chr((ord(c) + shift - 65) % 26 + 65)
            result += new_char
            key_index += 1
        elif c.islower():
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - 97
            new_char = chr((ord(c) - 97 + shift) % 26 + 97)
            result += new_char
            key_index += 1
        else:
            result += c
    return result

def vigenere_decrypt_function(ciphertext, key):
    result = ""
    key_index = 0
    for c in ciphertext:
        if c.isupper():
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - 65
            new_char = chr((ord(c) - shift - 65) % 26 + 65)
            result += new_char
            key_index += 1
        elif c.islower():
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - 97
            new_char = chr((ord(c) - 97 - shift) % 26 + 97)
            result += new_char
            key_index += 1
        else:
            result += c
    return result

# 🚫 没有交互界面！完全干净！