def caesar_cipher_encrypt(text, shift):
    """Encrypt the text using Caesar Cipher with the given shift."""
    encrypted_text = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_cipher_decrypt(text, shift):
    """Decrypt the text using Caesar Cipher with the given shift."""
    return caesar_cipher_encrypt(text, -shift)

def main():
    """Main function to run the Caesar Cipher encryption and decryption."""
    while True:
        print("Caesar Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher_encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")
        elif choice == '2':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher_decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
