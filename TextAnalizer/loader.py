from .file import *
import re as REGEX
from yaml import safe_load as yaml

class Config:

    class Element:
        named_keys = []

        class Local:
            def __init__ ( self, _local ):
                self.keywords = {}
                self.names = None
                if 'keywords' in _local:
                    self.keywords = _local['keywords']
                    _local.pop('keywords')

                self.functions = _local
            def __str__ (self):
                return str(self.functions)
            def __call__ (self):
                return self.functions

        class Child:
            def __init__ ( self, _child ):
                self.items = []
                if type(_child) == str:
                    self.items = [_child]
                elif type(_child) == dict:
                    for key in _child:
                        self.items.append({'name': key, 'replace': _child[key]})
                elif type( _child == list ):
                    self.items = _child
            def __str__ (self):
                return str(self.items)
            def __call__ (self):
                return self.items

        def __init__(self, _keys = {}, _key = None, _rep = None):

            # Properties

            self.functions = {}
            self.locals = None
            self.replace = _rep
            self.pattern = _key
            self.name = _key
            self.childs = None
            self.end = None

            # Additioning data to properties

            if _key and _rep:
                _keys['fnc'] = { _key: _rep }
                _keys['fnc'] = { _key: _rep }

            ptn = None
            if 'p' in _keys:
                ptn = 'p'
            elif 'ptn' in _keys:
                ptn = 'ptn'
            elif 'pattern' in _keys:
                ptn = 'pattern'
            if (ptn == 'p') or (ptn == 'ptn') or (ptn == 'pattern'):
                self.pattern = _keys[ptn]
                self.name = _key

            if _keys:

                for key in _keys:
                    if (key == 'f') or (key == 'fnc') or (key == 'function'):
                        self.functions = _keys[key]

                    if (key == 'l') or (key == 'lcl') or (key == 'local'):
                        self.locals = self.Local( _keys[key] )
                    if (key == 'r') or (key == 'rpl') or (key == 'replace'):
                        self.replace = _keys[key]
                    if (key == 'n') or (key == 'nam') or (key == 'name'):
                        self.name = _keys[key]
                    if (key == 'c') or (key == 'chd') or (key == 'childs'):
                        self.childs = self.Child( _keys[key] )
                    if (key == 'e') or (key == 'end'):
                        self.end = _keys[key]

        def __str__ (self):

            out = {
                'name': self.name,
                'key': self.pattern,
                'end': self.end,
                'functions': self.functions,
                'locals': self.locals() if self.locals else self.locals,
                'replace': self.replace
            }

            return str(out)

        def __call__ (self):

            out = {
                'name': self.name,
                'key': self.pattern,
                'end': self.end,
                'functions': self.functions,
                'locals': self.locals(),
                'replace': self.replace
            }

            return out

    def __init__ (self, _file = None, _text = None ):

        self.text = _text
        if not _text:
            self.file = File(_file)
            self.text = self.file.text

        self.properties = { ':identation': { True: '', False: ''}}
        self.elements = {}

        # Loading data
        dictionary = yaml( self.text )
        self.dict  = dictionary

        # Saving data
        for key in dictionary:

            if ':' is key[0]:
                self.properties[key] = dictionary[key]
            else:
                if type (dictionary[key]) == str:

                    key_tmp = self.Element(_rep = dictionary[key], _key = key)
                    if key_tmp.name:
                        self.elements[key_tmp.name] = key_tmp
                    else:
                        self.elements[key] = key_tmp

                elif type (dictionary[key]) == dict:

                    key_tmp = self.Element(_keys = dictionary[key], _key = key )
                    self.elements[key_tmp.name] = key_tmp

    def __str__ (self):
        return str(self.dict)

