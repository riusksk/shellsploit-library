#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


from capstoneheader import *


def disas(shellcode, bits=32):
    if bits == 32:
        md = Cs(CS_ARCH_X86, CS_MODE_32)
    elif bits == 64:
        md = Cs(CS_ARCH_X86, CS_MODE_64)

    for i in md.disasm(shellcode, 0x00000):
        if len(hexlify(i.bytes)) > 6:
            db = "\t0x%x:\t%s\t%s %s" % (i.address, hexlify(i.bytes), i.mnemonic, i.op_str)
        else:
            db = "\t0x%x:\t%s\t\t%s %s" % (i.address, hexlify(i.bytes), i.mnemonic, i.op_str)
        test.append(db)
    return "\n" + "\n".join(test) + "\n"
