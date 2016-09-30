#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


class Encoders(object):
    def __init__(self):
        self.py = [
            'encoders/py/bzip2',
            "encoders/py/gzip",
        ]

    def ret(self):
        return len(self.py)
