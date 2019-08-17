from .dictionary import *

def translate(_str, _file):
    return Dictionary(_file).translate(_str)

def open(_file):
    return File(_file)
