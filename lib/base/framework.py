#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


from lib.core.base import Base 
from lib.payloads.shellcode import Shellcode


class ShellsploitFramework(Base, Shellcode):

    def __init__(self):
        super(Base, self).__init__()
        super(Shellcode, self).__init__()
