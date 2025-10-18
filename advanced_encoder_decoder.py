import base64

# Caesar Cipher
def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

# Vigenère Cipher
def vigenere_encrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) - shift + 26) % 26 + ord(base))
            key_index += 1
        else:
            result += char
    return result

# Multi-layer encode
def multi_layer_encode(message, vigenere_key):
    step1 = caesar_encrypt(message)
    step2 = vigenere_encrypt(step1, vigenere_key)
    step3 = base64.b64encode(step2.encode()).decode()
    return step3

# Multi-layer decode
def multi_layer_decode(encoded_text, vigenere_key):
    try:
        step1 = base64.b64decode(encoded_text.encode()).decode()
        step2 = vigenere_decrypt(step1, vigenere_key)
        step3 = caesar_decrypt(step2)
        return step3
    except Exception as e:
        return f"[ERROR] Failed to decode: {e}"

# CLI
def main():
    print(" Advanced Multi-Layer Text Encoder/Decoder ")
    while True:
        print("\n1. Encode Message")
        print("2. Decode Message")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            text = input("Enter the message to encode: ")
            key = input("Enter Vigenère cipher key: ")
            encoded = multi_layer_encode(text, key)
            print(f"\nEncoded Output:\n{encoded}")

        elif choice == "2":
            encoded = input("Enter encoded message: ")
            key = input("Enter Vigenère cipher key: ")
            decoded = multi_layer_decode(encoded, key)
            print(f"\nDecoded Output:\n{decoded}")

        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
