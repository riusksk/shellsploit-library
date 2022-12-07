#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


from .payloads import *


def control(**kwargs):
    if kwargs['payload'] not in Encoders().py:
        return
    from .pyminifier import hero
    if kwargs['iteration']:
        for _ in range(int(kwargs['iteration'])):
            if "bzip2" in kwargs['payload']:
                hero.main(obfuscate=True, bzip2=True, gzip=False, files=kwargs['files'])
            elif "gzip" in kwargs['payload']: 
                hero.main(obfuscate=True, bzip2=False, gzip=True, files=kwargs['files'])
    elif "bzip2" in kwargs['payload']:
        hero.main(obfuscate=True, bzip2=True, gzip=False, files=kwargs['files'])
    elif "gzip" in kwargs['payload']: 
        hero.main(obfuscate=True, bzip2=False, gzip=True, files=kwargs['files'])				
