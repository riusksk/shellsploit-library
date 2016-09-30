#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


class Commands(object):
    def IP(self):
        from urllib2 import urlopen
        from re import findall

        lists = [
            "http://www.get-ip.me/",
            "http://checkip.dyndns.org/",
            "http://whatsmyip.net/",
            "http://mxtoolbox.com/WhatIsMyIP/",
        ]

        for x in lists:
            try:
                data = urlopen(x, timeout=2).read()
                grab = findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', data)
                ip = grab[0]
                break
            except:
                pass

        if len(ip) < 0:
            return "NAT IP Not founded."
        else:
            nat = "IP : %s\t-NAT" %   ip
            self.localIP( nat)


    def localIP(self, natip):
        #http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
        import socket
        print ("\n"+natip)
        try:
            print ("IP : {0}\t-Local".format([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]))
        except:
            print ("Local IP Not founded.")
        print ("")


    @staticmethod
    def clean():
        from os import name,system
        if name == "nt":
            return system('cls')
        else:
            return system('clear')


    @staticmethod
    def pids( check=None, name=None):
        #It currently supports Linux, Windows, OSX, FreeBSD and Sun Solaris,
        #both 32-bit and 64-bit architectures, with Python versions from 2.6 to 3.5
        #(users of Python 2.4 and 2.5 may use 2.1.3 version).
        from psutil import process_iter

        if check == "wholelist":
            print ("")
            for p in process_iter():
                try:
                    print ('\tPID: {0}  \t\t {1}'.format(p.pid,p.name()))
                except:
                    pass
            print ("")

        else:
            cache = None
            print ("")
            for p in process_iter():
                try:
                    if name.lower() in p.name().lower():
                        cache = True
                        print ('\tPID: {0}  \t\t {1}'.format(p.pid,p.name()))
                except:
                    pass
            print ("")
            if cache == None:
                print ("PID not founded for : {0} ".format(name))


    @staticmethod
    def oscommand( command):
        from os import system
        try:
            print ("")
            system( command)
        except Exception as error:
            return "Unexpected error : %s " % error


    @staticmethod		
    def web2ip( target):
        import socket
        try:
            return socket.gethostbyname(target)
        except Exception as error:
            return "Unexpected error : %s " % error


    @staticmethod
    def exit( out=None):
        from sys import exit 
        return exit( out) if out else exit()






