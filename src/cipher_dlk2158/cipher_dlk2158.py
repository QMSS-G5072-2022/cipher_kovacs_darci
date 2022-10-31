
def cipher(text, shift, encrypt=True):
    """
       The Caesar cipher function can encrypt and decrypt strings of text. Each letter is replaced by a letter some fixed number of positions down the alphabet.


       Parameters
       ----------
       text : string: the string to be encrypted or decrypted
       shift : integer: the fixed number of positions down the alphabet to use for encryption
       encrypt : binary: tells the function to encrypt or decrypt the string

       Returns
       -------
       The output of the function is the encrypted or decrypted text.

       Examples
       --------
       from cipher_dlk2158 import cipher_dlk2158
       cipher_dlk2158.cipher("Hello!",-1)
       "Gdkkn!"
       cipher_dlk2158.cipher("Gdkkn!",-1, encrypt=False)
       "Hello!"
       """
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




