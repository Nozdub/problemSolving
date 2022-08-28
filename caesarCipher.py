import string

# First try of caesarCipher, attempted implementing input into the function, which I couldn't get to work. Commented out
"""
def caesarCipher(text, shift):
    text = input("Write the text you wish to encrypt here: ")
    shift = int(input("How many letters would you like to shift with: "))
    letters = string.ascii_lowercase
    mask = letters[shift] + letters[:shift]
    encyption = str.maketrans(letters, mask)
    return text.translate(encyption)

myMessage = caesarCipher()
"""


# Second try of caesar cipher:
def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)


message = input("Type your text: ")
encryptedMessage = caesar(message)

print(message)
print(encryptedMessage)