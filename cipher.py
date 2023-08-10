# assignment: programming assignment 4
# author: Atheeksh Bhagavath
# date: November 16, 2022
# file: cipher.py is a program that (put the description of the program)
# input: should take in files to use for output
# output: encoded or decoded input files

def readfile(filename):
    text = ""
    try:
        page = open(filename, 'rt')
        text = page.read()
        page.close()
    except IOError:
        print("\nThe selected file cannot be open for reading!")
    except FileNotFoundError:
        print("\nThe selected file does not exist!")
    return text

def writefile(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()

def make_alphabet():
    alphabet = []
    for i in range(26):
        char = i + 65
        alphabet += (chr(char),)
    return alphabet

def encode(plaintext):
    shift = 3
    ciphertext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in plaintext:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                k = i + shift
                if k > 26:
                    k = k-26
                    letter = alphabet[(k) % length]
                    ciphertext.append(letter)
                    found = True
                    break
                else:
                    letter = alphabet[(i+shift) % length]
                    ciphertext.append(letter)
                    found = True
                    break
        if not found:
            ciphertext.append(char)
    return ciphertext

def decode(text):
    shift = -3
    plaintext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in text:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                found = True
                k = i + shift
                if k < 0:
                    k = 26 + k
                    letter = alphabet[(k) % length]
                else:
                    letter = alphabet[(i+shift) % length]
                plaintext.append(letter)
                break       
        if not found:
            plaintext.append(char)
    return plaintext

def to_string(text):
    Str = ""
    for val in text:
        Str += val
    return Str

def main():
    while True:
        print("Would you like to encode or decode the message?")
        char = input("Type E to encode, D to decode, or Q to quit: ")
        if char.upper() == 'E':
            text = ''
            while text == '':
                filename = input("Please enter a file for reading: ")
                text = readfile(filename)
            filename = input("Please enter a file for writing: ")
            print("Plaintext: ")
            print(text)
            value = encode(text)
            text = to_string(value)
            print("Ciphertext: ")
            print(text)
            writefile(filename, text)
        elif (char.upper() == 'D'):
            text = ''
            while text == '':
                filename = input("Please enter a file for reading: ")
                text = readfile(filename)            
            filename = input("Please enter a file for writing:")
            print("\nCiphertext: \n" + text)
            val = decode(text)
            strtext = to_string(val)
            print("\nPlaintext: \n" + strtext)
            writefile(filename, strtext)
        elif (char.upper() == 'Q'):
            print("Goodbye!")
            break
        else:
            print("No choice selected. Please try again.")
            main()
main()