#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#



from re import findall
import codecs


def plaintext( string):
    string = codecs.encode(str.encode(string), 'hex')
    string = string.decode('utf-8')
    db = findall("..?", string)
    return "\\x"+"\\x".join(db)


def plaintextreverse( string):
    string = codecs.encode(str.encode(string), 'hex')
    string = string.decode('utf-8')
    db = findall("..?", string)
    return "\\x"+"\\x".join(db[::-1])


def PORT( port):
    db = []
    fixmesempai = findall('..?', hex(int(port))[2:])
    for x in fixmesempai:
        if len(x) == 1:
            x = f"0{x}"
        db.append(x)
    return "\\x"+"\\x".join(db)


def IP( ip):
    #0x101017f : 127.1.1.1
    ip = str(ip).split(".")
    db2 = []
    db = [hex( int(x))[2:] for x in ip]
    for x in db: 
        if len(x) == 1:
            x = f"0{x}"
        db2.append(x)
    return "\\x"+"\\x".join(db2)


def rawSTR( string):
    db = []
    for x in string:
        first = codecs.encode(str.encode(x), 'hex')
        x = first.decode('utf-8')
        db.append("\\x"+x)
    return "".join(db)


def ARM( string):
    if "/" not in string:
        return
    if len(string) % 4 == 0:
        string = string
    elif  len(string) % 4 == 1:
        string = filler( string, 4)
    elif len(string)	% 4 == 2:
        string = filler( string, 3)
    elif len(string) % 4 == 3:
        string = filler( string, 2)
    db = [ARMsplitter(string[x:x+4]) for x in range(0,len(string),4)]
    return "".join(db)


def ARMsplitter( hexdump, pushdword="None"):
    if pushdword == "None":
        fixmesempai = findall('....?', hexdump)
        db = []
        for x in fixmesempai[::-1]:
            first = codecs.encode(str.encode(x[::-1]), 'hex')
            first = first.decode('utf-8')
            second = findall("..?", first)[::-1]
            db.append("\\x"+"\\x".join(second))
        return "".join(db)			


def stackconvertSTR( string, win=False):
    db = []
    if len(string) == 1:
        string = codecs.encode(str.encode(string), 'hex')
        string = string.decode('utf-8')
        return r"\x6a"+r"\x"+string

    if "/" in string:
        if len(string) % 4 == 0:
            string = string
        elif  len(string) % 4 == 1:
            string = filler( string, 4)
        elif len(string)	% 4 == 2:
            string = filler( string, 3)
        elif len(string) % 4 == 3:
            string = filler( string, 2)
        db.extend(splitter(string[x:x+4]) for x in range(0,len(string),4))
        return "".join(db[::-1])
            #return "".join(db)

    #Linux_x86
    #68 PUSH DWORD
    #6668 PUSH WORD
    #6A PUSH BYTE
    if len(string) == 4:
        first = codecs.encode(str.encode(string[::-1]), 'hex')
        stack = first.decode('utf-8')
        data = findall("..?", stack)
        return "\\x68\\x"+"\\x".join(data)


    elif len(string) % 4 == 0:
        db.extend(splitter(string[x:x+4]) for x in range(0,len(string),4))
        return "".join(db[::-1]) if win == True else "".join(db)
    elif 2 < len(string) < 4:
        first = codecs.encode(str.encode(hexdump[::-1]), 'hex')
        first = first.decode('utf-8')
        second = findall("..?", first)[::-1]
        db.extend("\\x"+x for x in second)
        return "\\x66\\x68"+"".join(db)


    else:
        db = []
        for x in range(0,len(string),4):
            if len(string[x:x+4]) == 4:
                db.append(splitter(string[x:x+4]))
            else:
                db.append(splitter(string[x:x+4], "WordTime"))
        return "".join(db[::-1]) if win == True else "".join(db)


def filler( string, number):
    string = list(string)
    for x in range(len(string)):
        if string[x] == "/":
            string[x] = "/"*number
            break
    return "".join(string) 


def splitter( hexdump, pushdword="None"):
    db = []
    if pushdword == "None":
        fixmesempai = findall('....?', hexdump)
        for x in fixmesempai[::-1]:
            first = codecs.encode(str.encode(x[::-1]), 'hex')
            first = first.decode('utf-8')
            second = findall("..?", first)[::-1]
            db.append("\\x"+"\\x".join(second))
        return "\\x68"+"".join(db)	

    else:		
        #Byte ..
        if len(hexdump) == 1:
            string = codecs.encode(str.encode(hexdump), 'hex')
            string = string.decode('utf-8')
            return r"\x6a"+r"\x"+string
        else:
            first = codecs.encode(str.encode(hexdump[::-1]), 'hex')
            first = first.decode('utf-8')
            second = findall("..?", first)[::-1]
            db.extend("\\x"+x for x in second)
            return "\\x66\\x68"+"".join(db)


