from .utils import remove_from_list, merge_lists
from .loader import *


def debug ( *unargs,**args ):
    print()
    for arg in args:
        if arg != 'pause':
            print('\t', arg,': ', args[arg], sep= '')
    for arg in unargs:
        print('\t', arg, sep= '')
    if 'pause' in args:
        input()


class Dictionary:
    config = None
    var_template = REGEX.compile(r'(\\{,}<)(\w{,}):{,1}(.{,}?)>')
    novar_template = REGEX.compile(r'<\w{,}:{,1}.{,}?>|(\\<\w{,}:{,1}.{,}?\\>)')
    def __init__ (self, _conf:dict = None):

        if _conf:
            self.load(_conf)

    def load(self, _conf):
        if type(_conf) == str:
            self.config

    def get_vars (self, _patt, _text ):
        i = 0
        var_templates = self.var_template.findall(_patt)
        context_list = list(remove_from_list(self.novar_template.split(_patt), ''))

        text_template = list(merge_lists(context_list, var_templates))

        variables = {}
        for r in range(len(text_template)):
            regex = ''
            if type(text_template[r]) == tuple:
                if text_template[r][0] != r'\<':
                    regex = text_template[r][2] if text_template[r][2] != '' \
                        else '\w{,}'
                else:
                    regex = ''.join(text_template[r])+'>'
            else:
                regex = text_template[r]
            regex = REGEX.compile(regex)

            res = regex.search(_text[i:])
            if res:
                res = res.group()
                name = text_template[r][1] if type(text_template[r]) == tuple else None

                if name:
                    variables[f'<{name}>'] = res
                i += len(res)
            else:
                return None
        return variables if variables != {} else None

    def replace(self, _patt, _rep, _text):

        if self.var_template.search(_patt):
            variables = self.get_vars(_patt, _text)
            for var in variables:
                _rep = variables[var].join(_rep.split(var))
            return _rep

        pattern = REGEX.compile(_patt)

        all_match = pattern.findall(_text)
        text_splited = pattern.split(_text)
        return ''.join(_rep.join(text_splited))

    # Identing texts
    def ident(self, _text, _rules):

        lines = _text.split('\n')

        level = 0
        lines_to_ident = [0 for i in range ( len(lines))]
        for ln in range( 1, len( lines )-1 ):

            if REGEX.search( _rules[True], lines[ ln-1 ].strip() ):
                level += 1
            if REGEX.search( _rules[False], lines[ ln ].strip() ):
                level -= 1

            lines_to_ident [ ln ] = level

        text = ''
        for ln in range( len( lines ) ):
            line = '   '*lines_to_ident [ ln ]+lines[ln]+'\n'

            if line.strip() == '':
                line = '\n'

            text += line

        return text.strip()+'\n'
