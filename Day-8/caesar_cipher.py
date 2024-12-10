#Task: Get user input and how much they want to shift each character by in the 
# alphabet, and whether they want to encode or decode the text
# Creating a caesar cipher.

#List containing the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']

#get user inputs for direction, text and shift amount
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#caesar function
def ceasar(direction, orginal_text, shift_amount):
    cipher = ""

    #make sure user input the correct direction
    if direction == "encode" or direction == "decode":

        #if decode then we want to go in the negative direction (left of the list)
        if direction == "decode":
            shift_amount = shift_amount * -1

        #shift text
        for ch in orginal_text:
            new_pos = alphabet.index(ch) + shift_amount
            new_pos = new_pos % len(alphabet) #using remainer so we dont get IndexOutOfBoundsError
            cipher += alphabet[new_pos]

        #print ciphered word
        print(f"Your text has been {direction}d to: {cipher}")
    
    else:
        print(f"ERROR: Direction {direction} does not exist!\nPlease choose to 'encode' or 'decode' your text.")

#call caesar fucntion
ceasar(direction=direction, orginal_text=text, shift_amount=shift)
