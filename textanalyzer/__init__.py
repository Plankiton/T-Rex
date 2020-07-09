from .dictionary import *

__dictionary__ = Dictionary()
def get_vars(pattern, text):
    return __dictionary__.get_vars(pattern, text)

def replace(pattern, substitute, text):
    return __dictionary__.replace(pattern, substitute, text)
