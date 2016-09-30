#-*- coding: utf-8 -*-
#------------------Bombermans Team---------------------------------#
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/Shellsploit
# LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#


"""
Except AES every function is working on 2x and 3x.We'll fix it soon and add couple of things to ..

ıf you cant install that damn thing into windows follow these steps;
Ref : http://stackoverflow.com/a/11405769
1) Install : https://www.microsoft.com/en-us/download/details.aspx?id=44266
2) easy_install http://www.voidspace.org.uk/python/pycrypto-2.6.1/pycrypto-2.6.1.win32-py2.7.exe

"""


def base64(TEXT, choice):
    from base64 import b64encode, b64decode
    return b64encode(TEXT.encode('utf-8')).decode('utf-8') if choice == "encode" else b64decode(TEXT).decode("utf-8")


def base32(TEXT, choice):
    from base64 import b32encode, b32decode
    return b32encode(TEXT.encode('utf-8')).decode('utf-8') if choice == "encode" else b32decode(TEXT).decode("utf-8")


def base16(TEXT, choice):
    from base64 import b16encode, b16decode
    return b16encode(TEXT.encode('utf-8')).decode('utf-8') if choice == "encode" else b16decode(TEXT).decode("utf-8")


def hex_(TEXT, choice):
    from codecs import encode, decode
    return encode(TEXT.encode('utf-8'), "hex").decode('utf-8') if choice == "encode" else decode(TEXT, "").decode("utf-8")


def md5(TEXT):
    from hashlib import md5
    return md5(TEXT.encode("utf-8")).hexdigest()


def sha1(TEXT):
    from hashlib import sha1
    return sha1(TEXT.encode("utf-8")).hexdigest()


def sha224(TEXT):
    from hashlib import sha224
    return sha224(TEXT.encode("utf-8")).hexdigest()


def sha256(TEXT):
    from hashlib import sha256
    return sha256(TEXT.encode("utf-8")).hexdigest()


def sha384(TEXT):
    from hashlib import sha384
    return sha384(TEXT.encode("utf-8")).hexdigest()


def sha512(TEXT):
    from hashlib import sha512
    return sha512(TEXT.encode("utf-8")).hexdigest()


def AES(TEXT, KEY, choice):
    from sys import version_info
    from base64 import b64encode, b64decode

    try:
        from Crypto.Cipher import AES
        from Crypto import Random
    except ImportError:
        print("\npycrypto must be installed.\n")
        return False	

    # AES key must be either 16, 24, or 32 bytes long
    BS = len(KEY) if len(KEY) % 16 == 0 or len(
        KEY) % 24 == 0 or len(KEY) % 32 == 0 else False
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    if choice == "encode":
        raw = pad(TEXT)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(raw)) if version_info[0] == 2 else b64encode(iv + cipher.encrypt(raw), "encode").decode("utf-8")
    else:
        enc = b64decode(TEXT)
        iv = enc[:16]
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:])) if version_info[0] == 2 else unpad(cipher.decrypt(enc[16:])).decode("utf-8")
