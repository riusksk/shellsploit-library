#------------------Bombermans Team---------------------------------#
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/Shellsploit
# LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from .color import *


# That encoders can be use on "injectors" ..
def encoderlist(require=False):
    if require != False:
        data = [
            "encoders/py/bzip2",
            "encoders/py/gzip",
            "encoders/shellcode/intel/x86/xor86.py",
            "encoders/shellcode/intel/x86/xor_b3m.py",
            "encoders/shellcode/intel/x86/xor64.py",
        ]
        return data
    else:
        print (bcolors.GREEN + """

Python
========

	encoders/py/bzip2
	encoders/py/gzip			


Shellcode
==========

	encoders/shellcode/intel/x86/xor86.py
	encoders/shellcode/intel/x86/xor_b3m.py
	

	""" + bcolors.ENDC)

# encoders/shellcode/intel/x86/xor64.py


def backdoorlist(require=False):
    if require != False:
        data = [
            "backdoors/linux86/reverse_tcp",
            "backdoors/linux64/reverse_tcp",
            "backdoors/osx86/reverse_tcp",
            "backdoors/osx64/reverse_tcp",
            "backdoors/windows/x86/reverse_tcp",

            #		"backdoors/php/reverse_tcp",
            #		"backdoors/asp/reverse_tcp",
            #		"backdoors/jsp/reverse_tcp",
            #		"backdoors/war/reverse_tcp",

            "backdoors/unix/python/reverse_tcp",
            "backdoors/unix/perl/reverse_tcp",
            "backdoors/unix/bash/reverse_tcp",
            "backdoors/unix/ruby/reverse_tcp",
            "backdoors/windows/asm/reverse_tcp",
            "backdoors/windows/ps/reverse_tcp",


        ]
        return data
    else:
        print (bcolors.GREEN + """

Binaries
==========

  backdoors/linux86/reverse_tcp
  backdoors/linux64/reverse_tcp
  backdoors/osx86/reverse_tcp
  backdoors/windowsx86/reverse_tcp - [Passive]
  backdoors/windowsx64/reverse_tcp - [Passive]


Scripting Payloads
===================

  backdoors/unix/python/reverse_tcp
  backdoors/unix/perl/reverse_tcp
  backdoors/unix/bash/reverse_tcp
  backdoors/unix/ruby/reverse_tcp
  backdoors/windows/asm/reverse_tcp
  backdoors/windows/ps/reverse_tcp

	""" + bcolors.ENDC)


# Web Payloads 
#=============

#  backdoors/php/reverse_tcp - [Passive]
#  backdoors/asp/reverse_tcp - [Passive]
#  backdoors/jsp/reverse_tcp - [Passive]
#  backdoors/war/reverse_tcp - [Passive]
