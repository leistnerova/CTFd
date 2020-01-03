from passlib.hash import bcrypt_sha256
import os
import string
import struct


def hash_password(plaintext):
    return bcrypt_sha256.encrypt(str(plaintext))


def verify_password(plaintext, ciphertext):
    return bcrypt_sha256.verify(plaintext, ciphertext)


def generate_password():
    # used from https://stackoverflow.com/questions/3854692/generate-password-in-python
    pass_len = 8
    symbols = string.printable.strip()
    return ''.join([symbols[x * len(symbols) / 256] for x in struct.unpack('%dB' % (pass_len,), os.urandom(pass_len))])
