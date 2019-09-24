from .dictionary import *

def translate(_str, _conf):
    return Dictionary(_conf).translate(_str)

def fopen(_file):
    return File(_file)

def replace(_patt, _rep, _text):
    return Dictionary().replace( _key=_patt, _rep=_rep, _text=_text)

def search(_patt, _text):
    regex = Dictionary().regex(_patt).strip()
    res = REGEX.search( regex, _text)
    return res.group() if res else None
