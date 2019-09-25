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
    def __init__ (self, _conf = None):
        if _conf:
            if '@c' in _conf [ :2 ]:
                self.config = Config( _text = _conf [2: ])
            else:
                self.config = Config(_conf)

    def get_var_templates (self, _text ):
        i = 0
        f = 0
        list_var = []
        while f <= len( _text ) and i < len( _text ):
            if _text[i] == '%' and _text[i-1] != '\\':
                text_end = _text[i:]
                if '&' in text_end:
                    if '\\&' in text_end:
                        if text_end.index('&') == text_end.index('\\&')+1:
                            continue
                    f = text_end.index('&')+ i + 1
                else:
                    continue
                list_var.append(_text[i:f])

            i += 1

        lvars = {}
        elvars = {}
        plvars = {}

        # Geting list of variables
        for var in list_var:
            var_patt = r'''p\w{1,}'''
            var_name = var.strip()

            if not '?' in var:
                lvars [ "{}".format(var_name) ] = var_patt

            else:
                # Geting list of variables with pattern on key of Config
                var_name = var [ 1 : var.index('?') ].strip()
                var_patt = var [ var.index('?')+1 : var.rindex('&') ].strip()

                if '!' in var_patt :
                    elvars [ "%{}&".format(var_name) ] = ' '+var_patt[ :var_patt.rindex('!') ]
                    var_patt = var_patt[ var_patt.rindex('!'): ].strip()

                var_name = "%{}&".format(var_name)
                lvars [ var_name ] = ' '+var_patt

            plvars[var] = lvars[var_name][1:]

        return { 'templates': lvars, 'else_templates': elvars, 'pure_templates': plvars}

    def regex(self, _patt):
        regex = _patt
        plvars = self.get_var_templates(_patt)['pure_templates']
        for pure_var in plvars:
            regex =  plvars [ pure_var ].join( regex.split(pure_var) )
        return regex

    def get_vars (self, _key, _text ):
        def add_variable ( _variable, _name, _len_compl, _pos ):

            _variable [ _name ] = _variable [ _name ].group()
            _variable [ _name ] = _variable[ _name ][:len(_variable [ _name ])-_len_compl]
            _pos += len( _variable [ _name ] )+1

            return _variable, _name, _len_compl, _pos


        lvars = self.get_var_templates(_key)['templates']
        elvars = self.get_var_templates(_key)['else_templates']
        plvars = self.get_var_templates(_key)['pure_templates']

        variable = {}

        i = 0
        f = 0
        pos = 0

        # Confirming text pattern

        while f < len(_key):

            if _key[f] == '%':

                k = _key [f:]
                lenght = len ( k [ : k.index('&')+1 ].strip() )

                # Geting variables name
                name = k [: k.index('&')+1].strip()

                # Adapting regex
                compl = ''
                len_compl = 0
                if '?' in name:
                    if k.index('&')+1 < len(k):
                        compl = k[ k.index('&')+1 ]
                        if compl == '\\':
                            compl += k[ k.index('&')+2 ]
                        len_compl = 1

                regex = _key[:f].lstrip()
                for pure_var in plvars:
                    regex =  plvars [ pure_var ].join( regex.split(pure_var) )

                # confirming variable position
                result = REGEX.match( regex, _text.strip() )

                # Adapting text
                if '?' in name:
                    name = REGEX.search(r'%\w{1,}\?', name).group()
                    name = name[:len(name)-1]+'&'

                # Positioning

                # Geting variables values

                if result:
                    pos = len( result.group() )
                else:
                    f += 1
                    continue

                # Case pattern in end and value of pattern is the default
                if lvars [ name ][0] == 'p':
                    lvars [ name ] = r'\w{1,}'

                # Case pattern in end
                elif name in elvars:
                    lvars [ name ] = elvars [ name ]

                lvars [ name ] = lvars [ name ].strip()

                # Getting variable...
                variable [ name ] = REGEX.match( lvars [ name ]+compl, _text[pos:].strip() )

                if variable [ name ]:
                    variable, name, len_compl, pos = add_variable(variable, name, len_compl, pos)
                else:
                    variable.pop(name)

            f += 1

        return variable if variable != {} else None

    def replace (self, _key = None, _rep = None, _text = None, _vars = None, _type = 'function', _abs = False ):

        replaced = _text
        atual_type = _type

        if _abs:
            replaced = _rep
            variables = self.get_vars ( _key, replaced )
            if _vars and variables:
                for key in _vars:
                    variables[key] = _vars[key]
            elif _vars:
                variables = _vars


            if variables != None:
                for var in variables:
                    replaced = variables[var].join( replaced.split(var) )
            return replaced

        # Processing replaces
        if _key and _rep and _text:

            if ( REGEX.search(r'\%\w{1,}\&', _key) is None ):
                regex = REGEX.compile(_key)
                i = 0
                while i < ( len( replaced ) ):
                    res = regex.match(replaced[i:])
                    if res:
                        replaced = replaced[:i] + _rep + replaced[i+len(res.group()):]
                        i += len(res.group())
                    i += 1

        # Processing functions
        if _key and _rep and _text and atual_type == 'function':

            variables = self.get_vars ( _key, replaced )
            if _vars and variables:
                for key in _vars:
                    variables[key] = _vars[key]
            elif _vars:
                variables = _vars


            if variables != None:
                replaced = _rep
                for var in variables:
                    replaced = variables[var].join( replaced.split(var) )

        return replaced

    # Add list of variables to a list of variables
    def add_vars ( self, _dic_ini = {}, _dic_end = {} ):
        if _dic_end:
            for key in _dic_end:
                _dic_ini[key] = _dic_end[key]
        return _dic_ini

    # Check if the key is in text
    def check ( self, _key = None, _text = None ):
        if _key and _text:

            variables = self.get_var_templates( _key )['pure_templates']
            for var in variables:
                _key = variables[var].join( _key.split(var) )

            if REGEX.search ( _key, _text.strip() ):
                return True
            else:
                return False
        else:
            return None

    def get_local_functions_variables(self, _lines):

        Keys = self.config.elements
        local_variables = {}

        # Registring the keys with local functions
        for key in Keys:
            atual_key = Keys[key]

            if atual_key.locals or atual_key.childs or atual_key.end:
                local_variables [ atual_key.name ] = []

        # Registring lines in the keys
        for key in local_variables:
            atual_key = Keys[key]
            for ln in range( len( _lines ) ):
                line = _lines [ ln ]

                if self.check ( atual_key.pattern, line ) and atual_key.end:

                    variables = self.get_vars( atual_key.pattern, line )
                    if variables == None:
                        variables = {}


                    end_aux = atual_key.end
                    if type( atual_key.end ) == dict:
                        atual_key.end = atual_key.end['name']

                    if atual_key.name == atual_key.end:
                        lln = ln + 1
                        while lln < len( _lines ):

                            if self.check ( Keys [ atual_key.end ].pattern, _lines[lln] ):
                                local_variables [ atual_key.name ].append( { 'variables': variables, 'begin': ln, 'end': lln } )
                                break
                            lln += 1

                    else:
                        lln = len( _lines ) - 1
                        while lln > ln:

                            if self.check ( Keys [ atual_key.end ].pattern, _lines[lln] ):
                                local_variables [ atual_key.name ].append( { 'variables': variables, 'begin': ln, 'end': lln } )
                                break
                            lln -= 1
                    atual_key.end = end_aux
        return local_variables


    def get_childs ( self, _key, _local_variables ):

        Keys = self.config.elements
        exceptions = []
        if _key.childs:
            _key.locals.names = {}
            for i in range(len(_key.childs())):
                child = _key.childs()[i]

                if type ( child ) == str :
                    _key.locals.functions[ Keys[child].pattern] = Keys[child].replace

                else:
                    child = _key.childs()[i]['name']

                    _key.locals.functions[ Keys[child].pattern] = _key.childs()[i]['replace']
                _key.locals.names [ Keys[child].name ] = Keys[child].pattern

                if Keys[child].end:

                    if type(Keys[child].end) == dict:
                        end_child = Keys[child].end['name']
                    else:
                        end_child = Keys[child].end

                    for i in range( len( _local_variables [ child ] ) ):

                        exceptions.append({
                            'line': _local_variables [ child ][i]['end'],
                            'pattern': Keys[ end_child ].pattern,
                            'replace': Keys[ end_child ].replace if type(Keys[child].end) != dict else Keys[child].end['replace'],
                        })
        return _key, exceptions


    def do_local_functions( self, _key , _local, _lines, _local_variables = {} ):

        Keys = self.config.elements

        if type(_key.end) == dict:
            end_key = _key.end['name']
        else:
            end_key = _key.end

        if _local['begin'] == _local['end']:
            return _lines

        if not _key.locals:
            _key.locals = Config.Element.Local({})

        _key, exceptions = self.get_childs( _key, _local_variables )

        # Doing the exceptions
        for exc in exceptions:
            _lines [ exc [ 'line' ] ] = self.replace (
                _key = exc [ 'pattern' ],
                _rep = exc [ 'replace' ],
                _text = _lines[ exc [ 'line' ] ],
                _vars = _local['variables'],
            )

        for line in range( _local['begin'], _local['end'] ):

            # Local replaces
            for word in _key.locals.keywords:

                repl = _key.locals.keywords[ word ]

                # Replacing keys with variables
                _lines[line] = self.replace (
                    _key = word,
                    _rep = repl,
                    _text = _lines[line],
                    _vars = _local['variables'],
                )

            # Local functions
            for key in _key.locals():

                repl = _key.locals()[ key ]

                # Replacing keys with variables
                if self.check ( key, _lines[ line ] ):
                    _lines[line] = self.replace (
                        _key = key,
                        _rep = repl,
                        _text = _lines[line],
                        _vars = _local['variables']
                    )

        return _lines


    def do_functions(self, _key, _lines):

        # Replacing keys without variables
        for ln in range(len(_lines)):
            line = _lines [ ln ]

            _lines[ln] = self.replace (

                _key = _key.pattern,
                _rep = _key.replace,
                _text = line,

            )

            # Case key is a function
            for key in _key.functions:

                repl = _key.functions[key]

                # Replacing keys with variables
                repl = self.replace (
                    _key = key,
                    _rep = repl,
                    _text = line
                )
                if repl.strip() != _lines[ln].strip():
                    _lines[ln] = repl
                    break

        return _lines

    def get_eval_templates (self, _text ):

        i = 0
        f = 0
        list_eval = []
        while f <= len( _text ) and i < len( _text ):
            if _text[i: i+2] == '!{':
                text_end = _text[i+1:]
                if '}' in text_end:
                    f = text_end.rindex('}') + i + 1
                    while REGEX.search(r'\!\{', text_end):
                        f = text_end.rindex('}')
                        text_end = text_end[: f]
                        f +=  i + 1
                else:
                    continue
                list_eval.append(_text[i:f]+'}')
            i += 1
        return list_eval

    # Executing python commands in texts
    def do_evals (self, _text):
        evals = self.get_eval_templates( _text)

        for cmd in evals:
            _text = str(eval(cmd[2:len(cmd)-1])).join( _text.split(cmd) )

        return _text

    # Translating a text
    def translate (self, _text):

        Keys = self.config.elements
        lines = _text.split('\n')

        local_variables = self.get_local_functions_variables( lines )

        for key in Keys:

            atual_key = Keys[key]

            # Doing local functions
            if atual_key.name in local_variables:
                for local in local_variables [ atual_key.name ]:
                    lines = self.do_local_functions(atual_key, local, lines, local_variables)
            else:
                # Doing global functions
                lines = self.do_functions( atual_key, lines)

        # Doing evals in replaces
        for ln in range( len( lines ) ):
            lines[ln] = self.do_evals( lines[ln] )

        return '\n'.join(lines)

    # Identing texts
    def ident (self, _text, _rules):

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
