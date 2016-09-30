#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


from disassembly import Disassembly


class Shellcode(Disassembly):
    info = {
        "author": "",
        "credits": "",
        "name": "",
        "references": "",
        "platform": "",
        "disclosureDate": "",
        "reliability": "",
        "rawassembly": "",
        "size": "",
        "payload": "",
    }

    def __init__(self):
        Disassembly.__init__(self)   

    def getpayload(self):
        return Shellcode.info["payload"][0]

    def getsize(self, x):
        return len(x.split("\\x"))

    @staticmethod
    def prettyout(shellcode):
        from re import findall
        data = shellcode.replace("\\x", "")
        db = []
        print("\n")
        for x in [data[x:x + 40] for x in range(0, len(data), 40)]:
            db = findall("..?", x)
            if data.endswith(x):
                print('\t"\\x' + "\\x".join(db) + '"')
            else:
                print('\t"\\x' + "\\x".join(db) + '"' + ' +')
        print("\n")
