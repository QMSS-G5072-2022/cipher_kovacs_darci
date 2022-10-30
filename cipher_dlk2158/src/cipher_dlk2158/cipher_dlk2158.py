
# The Caesar cipher function can encrypt and decrypt strings of text. Each letter is replaced by a letter some fixed number of positions down the alphabet.

# The input of the function has three text parameters:
# "text" is the string to be encrypted or decrypted
# "shift" is the fixed number of positions down the alphabet to use for encryption
# "encrypt" is binary and tells the function to encrypt or decrypt the string
def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

# the output of the function is the encrypted or decrypted text

# For example: cipher("Hello!",-1)
# returns 'Gdkkn!'

# cipher("Gdkkn!",-1, encrypt=False)
# returns 'Hello!'

