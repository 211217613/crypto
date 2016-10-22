import binascii
import base64

BASE_STRING = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
TARGET = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
def convert():
    if len(BASE_STRING) % 2 != 0:
        # TODO: raise error
        print("string has to be a value even")
        raise ValueError
    temp = binascii.unhexlify(BASE_STRING)
    print(temp)
    temp1 = base64.b64encode(temp).decode('ascii')
    print(temp1)
    if temp1 == TARGET:
        return True
    else:
        return False

if __name__ == '__main__':
    if convert():
        print('YAAAAAY')