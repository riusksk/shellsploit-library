#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


from .payloads import *


def control(**kwargs):
    if kwargs['payload'] in Encoders().py:
        from .pyminifier import hero
        if kwargs['iteration']:
            for x in range(int(kwargs['iteration'])):
                if "bzip2" in kwargs['payload']:
                    hero.main(obfuscate=True, bzip2=True, gzip=False, files=kwargs['files'])
                elif "gzip" in kwargs['payload']: 
                    hero.main(obfuscate=True, bzip2=False, gzip=True, files=kwargs['files'])	
        else:
            if "bzip2" in kwargs['payload']:
                hero.main(obfuscate=True, bzip2=True, gzip=False, files=kwargs['files'])
            elif "gzip" in kwargs['payload']: 
                hero.main(obfuscate=True, bzip2=False, gzip=True, files=kwargs['files'])				
