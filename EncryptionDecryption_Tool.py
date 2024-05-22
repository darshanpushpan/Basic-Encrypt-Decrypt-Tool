def caesar_cipher(text, shift, direction):
    """
    Encrypts or decrypts the text based on the shift value and direction.
    :param text: str, the input text to be encrypted or decrypted.
    :param shift: int, the number of positions each character in the text should be shifted.
    :param direction: str, 'encrypt' for encryption, 'decrypt' for decryption.
    """
    if direction == 'decrypt':
        shift = -shift  # Invert the shift for decryption

    transformed_text = ""

    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            start = ord('a') if char.islower() else ord('A')
            # Shift the character and ensure it wraps around the alphabet
            transformed_char = chr((ord(char) - start + shift) % 26 + start)
            transformed_text += transformed_char
        else:
            # If the character is not an alphabet, add it unchanged
            transformed_text += char

    return transformed_text

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift key (number of positions to shift): "))
    direction = input("Choose 'encrypt' or 'decrypt': ").strip().lower()

    while direction not in ['encrypt', 'decrypt']:
        print("Invalid direction. Please choose 'encrypt' or 'decrypt'.")
        direction = input("Choose 'encrypt' or 'decrypt': ").strip().lower()

    result = caesar_cipher(text, shift, direction)
    print("Result:", result)

if __name__ == "__main__":
    main()
