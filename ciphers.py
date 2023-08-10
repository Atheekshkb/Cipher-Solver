# function to read a file
def readfile(filename):
    try:
        page = open(filename, 'rt')
        message = page.read()
    except IOError:
        print("The selected file cannot be open for reading!")
    except FileNotFoundError:
        print("The selected file does not exist!")
    page.close()
    return message


def writefile(filename, message):
    f = open(filename, "w")
    f.write(message)
    f.close()


def make_alphabet():
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(26):
        char = i + 65
        alphabet += (chr(char),)
    return alphabet


def encode(plaintext):
    shift = 3
    ciphertext = []
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    length = len(alphabet)
    for char in plaintext:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
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
                k = i + shift
                if k < 0:
                    k = 26 + k
                    letter = alphabet[(k) % length]
                    plaintext.append(letter)
                    found = True
                    break
            if not found:
                plaintext.append(char)
                return plaintext


def to_string(text):
    s = ""
    for val in text:
        s += val
        return s


def main():
    print("Would you like to encode or decode the message?")
    char = input("Type E to encode, D to decode, or Q to quit: ")
    while True:
        if char == 'E':
            filename = input("Please enter a file for reading: ")
            text = readfile(filename)
            filename = input("Please enter a file for writing: ")
            print("plaintext:")
            print(text)
            val = encode(text)
            strtext = to_string(val)
            print("ciphertext: ")
            print(strtext)
            writefile(filename, strtext)
        elif (char == 'D'):
            filename = input("Please enter a file for reading: ")
            text = readfile(filename)
            filename = input("Please enter a file for writing: ")
            print("ciphertext: " + text)
            val = decode(text)
            strtext = to_string(val)
            print("plaintext: " + strtext)
            writefile(filename, strtext)
        elif (char == 'Q'):
            print("Goodbye!")
            break
        else:
            print("Wrong Input!")
            print("Would you like to encode or decode the message")
            char = input("Type E to encode D to decode Q to quit: ")
            # call main()
            main()