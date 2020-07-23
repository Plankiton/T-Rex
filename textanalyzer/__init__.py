from .dictionary import *

__dictionary__ = Dictionary()
def get_vars(pattern, text):
    return __dictionary__.get_vars(pattern, text)

def replace(pattern, substitute, text):
    return __dictionary__.replace(pattern, substitute, text)

def has_var(pattern):
    var_templates = __dictionary__.var_template.findall(pattern)
    return len(var_templates)

search = REGEX.search
