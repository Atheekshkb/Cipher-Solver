from ciphers import *

if __name__ == '__main__':

    # check the function encode()
    print('Testing encoding ...\n')
    standard = ['KHOOR!', 'KRZ DUH BRX?'] # list of text lines
    plaintext = encode(['HELLO!', 'HOW ARE YOU?'])# list of text lines
    i = 0
    for line in plaintext:
        assert line == standard[i]
        print(line)
        print(standard[i], '\n')
        i += 1

    # check the function decode()
    print('Testing decoding ... \n')
    standard = ['HELLO!', 'HOW ARE YOU?'] # list of text lines
    ciphertext = decode(['KHOOR!', 'KRZ DUH BRX?']) # list of text lines
    i = 0
    for line in ciphertext:
        assert line == standard[i]
        print(line)
        print(standard[i], '\n')
        i += 1
                        
    
