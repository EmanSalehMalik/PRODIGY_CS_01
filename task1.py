def caesar_cipher(text, shift, mode):
    result = ""

    # Adjust shift for decryption
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Non-alphabet characters are unchanged

    return result

def main():
    while True:
        choice = input("Do you want to (E)ncrypt, (D)ecrypt, or (Q)uit? ").lower()

        if choice == 'q':
            print("Goodbye!")
            break
        elif choice in ['e', 'd']:
            text = input("Enter the text: ")
            shift = int(input("Enter the number of shifts: "))
            mode = "encrypt" if choice == 'e' else "decrypt"

            result = caesar_cipher(text, shift, mode)
            print(f"Result: {result}\n")
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
