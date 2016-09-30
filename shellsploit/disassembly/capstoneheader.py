#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#



from capstone import *
from binascii import hexlify


ARCH = {
    'arm': CS_ARCH_ARM,
    'arm64': CS_ARCH_ARM64,
    'mips': CS_ARCH_MIPS,
    'ppc': CS_ARCH_PPC,
    'x86': CS_ARCH_X86,
    'xcore': CS_ARCH_XCORE
}

MODE = {
    '16': CS_MODE_16,
    '32': CS_MODE_32,
    '64': CS_MODE_64,
    'arm': CS_MODE_ARM,
    'be': CS_MODE_BIG_ENDIAN,
    'le': CS_MODE_LITTLE_ENDIAN,
    'micro': CS_MODE_MICRO,
    'thumb': CS_MODE_THUMB
}

test = []
