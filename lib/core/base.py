#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


from commands import Commands


class Base(Commands):
    def __init__(self):
        Commands.__init__(self)  

    @staticmethod
    def dynamicimport( script):
        "return a function or class"
        import importlib
        return importlib.import_module( script)


    @staticmethod
    def binary2hex( binary):
        "convert binary to hexdecimal"
        import binascii
        return binascii.hexlify(binary)

