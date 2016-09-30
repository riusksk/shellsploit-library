from optparse import OptionParser
import sys
from .opt import *

from . import pyminify
from . import __version__

"""
-Lzma disable for a while.Coz pyminifer will be improve while merge to shellsploit.-

py3 = False
lzma = False
if not isinstance(sys.version_info, tuple):
    if sys.version_info.major == 3:
        py3 = True
        try:
            import lzma
        except ImportError:
            pass
    else:
        import pylzma as lzma
"""



def main(**kwargs):
    options = Namespace(obf_functions=False, obf_import_methods=False, pyz=None, nominify=False, obf_classes=False, tabs=False, replacement_length= 1, bzip2=kwargs['bzip2'], destdir='./minified', prepend=None, obf_variables=False, outfile=None, obf_builtins=False, obfuscate=kwargs['obfuscate'], gzip=kwargs['gzip'], use_nonlatin=False)
    pyminify(options, kwargs['files'])


