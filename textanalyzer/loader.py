from yaml import safe_load as yaml
import re as REGEX
from .file import *
import re

_ptn_var = re.compile(r'\\{0}<\w{,}(:{1}.{,}){,1}\\{0}>')
class _type_replace:
    def __init__(self, pattern:str, template:str):
        self.pattern = re.compile(pattern)
        self.template = template

    def search(self, text:str) -> re.Match:
        r'''
        Search the pattern of object on a <text>, and returns None if not to found

        params:
            text:str -> text where are the pattern
        '''

        res = self.pattern.search(text)
        if res: return {'pos': res.pos,
                        'res': res.group()}
        else: return res

    def findall(self, text:str) -> list:
        r'''
        Search the pattern of object on a <text>, and returns None if not to found

        params:
            text:str -> text where are the pattern
        '''

        matched = []
        for i in range(len(text)):
            res = self.search(text[i:])
            if res:
                matched.append(res)
        return matched


class _type_var:
    def __init__(self, name:str, pattern:str = None, value:str = None):
        self.name = name
        self.value = value
        self.pattern = r'\w{,}'

        if pattern:
            self.pattern = pattern


class _type_replace_var(_type_replace):
    del findall
    def __init__(self, pattern:str, template:str):
        super().__init__(pattern, templates)
        self.templates = []

    def toregex(self, pattern:str) -> str:
        variables = self.findall(pattern)
        pattern = _ptn_var.split(pattern)

        full_pattern = []
        print(variables)

    def search(self, text):
        variables = []

class Config:
    def __init__(self, file:File = None, body:dict = None):

        self.body = []
        # self.load(body)
        # if file:
        #    self.load(yaml(file.text))


    '''
    def load(self, body:dict):
        for key in body:
            if type(body[key]) == dict:
                pass
            else:
                if not _ptn_var.search(key):
                    self.body.append(_type_replace(key, body[key]))
                else:
                    self.body.append(_type_replace_var(key, body[key]))
