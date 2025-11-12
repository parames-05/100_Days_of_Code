def create_alphabet():
    alpha = [chr(i) for i in range(97, 123)]
    return alpha + alpha

abc = create_alphabet()

def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char in abc:
            index = abc.index(char)
            encrypted += abc[index + shift]
        else:
            encrypted += char
    return encrypted

def decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char in abc:
            index = abc.index(char)
            decrypted += abc[index - shift]
        else:
            decrypted += char
    return decrypted

def user_inputs():
    text = input("Enter the text: \n").lower()
    while True:
        try:
            shift = int(input("Enter the shift digit: \n"))
            break
        except ValueError:
            print("Please enter a valid number.")
    return text, shift

def main():
    print("Welcome to the Caesar Cipher!")
    while True:
        choice = input("\nChoose a mode: encrypt / decrypt / off\n").lower()

        if choice == "off":
            print("Switching off... Sayonara!")
            break

        elif choice in ["encrypt", "decrypt"]:
            text, shift = user_inputs()
            if choice == "encrypt":
                result = encrypt(text, shift)
                print(f"\nEncrypted text: {result}")
            else:
                result = decrypt(text, shift)
                print(f"\nDecrypted text: {result}")
        else:
            print("Invalid choice! Please type 'encrypt', 'decrypt', or 'off'.")

if __name__ == "__main__":
    main()

