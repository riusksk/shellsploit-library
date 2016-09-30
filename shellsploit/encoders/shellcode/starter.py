#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


from .payloads import *


def control(**kwargs):
    if kwargs['payload'] in Encoders().shellcode:
        data = open(kwargs['files'][0], "r").read().strip()

        if kwargs['payload'] == "encoders/shellcode/intel/x86/xor86.py":
            from .xor import prestart
        elif kwargs['payload'] == "encoders/shellcode/intel/x86/xor_b3m.py":
            from .xor_b3m import prestart

        with open(kwargs['files'][0], "w") as encoded:
            encoded.write(prestart((data.replace("\\x", "")), kwargs['iteration']))
