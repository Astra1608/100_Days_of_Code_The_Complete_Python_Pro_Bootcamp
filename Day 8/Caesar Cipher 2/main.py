alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = " "
    for letter in original_text:
        index_no_for_encryption = (alphabet.index(letter) + shift_amount) % len(alphabet)#13
        encrypted_text +=alphabet[index_no_for_encryption]
    print(f"Here's the encoded result: {encrypted_text} ")

def decrypt(original_text, shift_amount):
    decrypted_text = " "
    for letter in original_text:
        index_no_for_encryption = (alphabet.index(letter) - shift_amount) % len(alphabet)  # 13
        decrypted_text += alphabet[index_no_for_encryption]
    print(f"Here's the decoded result: {decrypted_text} ")

#combined encryption and decryption
def caesar(user_direction,user_text,user_shift):
    output_text = " "
    for letter in user_text:
        if user_direction=="decode":
            user_shift *= -1

        index_no_for_encryption = (alphabet.index(letter) + user_shift) % len(alphabet)  # 13
        output_text += alphabet[index_no_for_encryption]
    print(f"Here's the {user_direction}d result: {output_text} ")


caesar(direction,text,shift)












