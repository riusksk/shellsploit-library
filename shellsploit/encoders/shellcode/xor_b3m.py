#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


from random import randint
from itertools import product
from sys import setrecursionlimit
from re import findall
from sys import exit
from sys import version_info
from binascii import hexlify


setrecursionlimit(9999)


def xorme(shellcode):
    cache = shellcode
    mylist = ["".join(x) for x in list(product("ABCDEF", repeat=2))]
    insert = mylist[randint(0, len(mylist) - 1)]
    xorfirst = [
        r"\x40",  # inc eax
        r"\x43",  # inc ebx
        r"\x42",  # inc edx
        r"\x47",  # inc edi
    ]
    header = xorfirst[randint(0, len(xorfirst) - 1)]
    header += r"\xEB\x0D"
    header += xorfirst[randint(0, len(xorfirst) - 1)]
    header += r"\x5E"
    header += xorfirst[randint(0, len(xorfirst) - 1)]
    header += r"\x80\x36"
    header += r"\x" + insert
    header += r"\x74\x0A\x46"
    header += xorfirst[randint(0, len(xorfirst) - 1)]
    header += r"\xEB\xF7"
    header += xorfirst[randint(0, len(xorfirst) - 1)]
    header += r"\xE8\xEF\xFF\xFF\xFF"

    encode = ""
    if version_info.major >= 3:
        for x in hexlify(cache.encode('utf8')):	
            y = x ^ int(f"0x{insert}", 16)
            test = r'\x%02x' % y
            encode += test
    else:
        for x in bytearray(cache.decode("hex")):
            y = x ^ int(f"0x{insert}", 16)
            test = r'\x%02x' % y
            encode += test

    header += encode.upper()
    header += r"\x" + insert

    if r"\x00" in header.lower():
        xorme(shellcode)
    return header.lower().replace("\\x", "")


def start(shellcode):
    try:
        control = True
        while control:
            qe = findall("..?", xorme(shellcode))
            if "00" in qe:
                qe = findall("..?", xorme(shellcode))
                control = True
            else:
                control = False
        return "".join(qe)
    except:
        return "After roll 9999 times,payload generate failed."


def prestart(data, roll=None):
    cache = True
    if roll is None or roll == 1:
        data = start(data) 
        cache = False
    elif roll > 25:
        return "This script is still BETA.Please do not use iteration more than 25 times."
    else:
        cache = False
        for _ in range(int(roll)):
            if data == "After roll 9999 times,payload generate failed.":
                cache = True
                break
            data = start(data)

    if cache != False:
        return "After roll 9999 times,payload generate failed."
    qe = findall("..?", data)
    return "\\x" + "\\x".join(qe).lower()
