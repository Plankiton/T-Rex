#!/usr/bin/python3

import sys
from argparse import ArgumentParser as Parser

from textanalizer import *


def show_documentation():
    print(r'''
    Use the pipe ("|") to send the text to getter.

    example:
        echo "joao, maria, laura marteu" | getter 'laura' -b ','

-b| --break-char
-----------------
    is to split the text in last example the text did split were is ",", by default -b is '\n'(break line)

-s| --separate
---------------
    is to split the text output, by default is '\n'.

    example:
        echo "joao, .maria, .laura marteu" | getter '^\.' -b ',' -s ', '

-t| --template / pattern
-------------------------
    is to change the output, in pattern you will write a regex and this regex will be used on "-t"

    example:
        echo "people tony stark;dog scoobydoo;cat garfild" | getter "people \w{1,}$" -b ';' -t 'people hawk stark'

    and in -t you can use variables, and him need be like this: "%<variable-name>&"
        echo "people tony stark;dog scoobydoo;cat garfild" | getter "people %name&" -b ';' -t '%name&'

    but always that you take a variable the getter use the regex "\w{1,}", if you need other regex is just insert a ? in variable (%<variable-name>?<regex>&)

    example:
        echo "people tony stark;dog scoobydoo;cat garfild" | getter "%type& %name?.{1}&" -b ';' -t '%name& -> %type'

    Other option is execute python comands to change response manually, is just write the commands between '!{' and '}'

    example:
        echo "people tony stark;dog scoobydoo;cat garfild" | getter "%type& %name?.{1}&" -b ';' -t '%name& -> !{ "%type".split() }'

    Too have a especial chars:
        %r: response of the searched pattern
        %i: current item from text splited by -b|--break-char
        %p: indice of the item

    the escape char is "\", so...
        \\%: %
        \\!: !
        \\&: &
    '''.strip())
    return 0
def do_tmpl( _text, _conf, _items, _ind ):
    chars = {
        r'%r': search(_conf, _items[_ind]),
        r'%i': _items[_ind],
        r'%p': _ind,
        r'%a': _items
        }

    for c in chars:
        text = REGEX.split( c, _text )
        char = str( chars[c] )
        _text = char.join(text)
    return _text

def main():
    args = Parser(
            description = "Search engine for terminal.",
            prog = "Getter"
            )

    if ( (not '-c' in sys.argv and not '--config' in sys.argv)
        and (not '-d' in sys.argv and not '--documentation' in sys.argv)):
            args.add_argument(
                    'pattern',
                    help = 'short pattern to search in text.',
                    type = str
                    )
    args.add_argument(
            '-c', '--config',
            help = "Yaml with the dictionary to search in text.",
            type = str
            )
    args.add_argument(
            '-f', '--file',
            help = "file to input the text.",
            type = str
            )
    args.add_argument( '-t', '--template',
            help = "output format",
            type = str
            )
    args.add_argument( '-s', '--separate',
            help = "separate char to output",
            type = str
            )
    args.add_argument( '-b', '--break-char',
            help = "break point char in the text input",
            type = str,
            dest = 'break_char'
            )
    args.add_argument( '-d', '--documentation',
            help = "documentation",
            action = 'store_true',
            default = False,
            )
    args.add_argument( '-v', '--show-variables',
            help = "show a json with the variables",
            action = 'store_true',
            default = False,
            dest = 'variables'
            )
    args = args.parse_args()

    docu = args.documentation
    if docu:
        return show_documentation()

    text = fopen(args.file).text if args.file else sys.stdin.read()
    conf = args.config if args.config else '@c'+args.pattern
    brea = args.break_char if args.break_char else '\n'
    sepr = args.separate if args.separate else '\n'
    tmpl = args.template
    patt = args.pattern
    response = ''

    items = text.strip().split( brea )
    for txt in range( len(items) ):
        items[txt] = items[txt].strip()
        if search( patt, items[txt] ):
            if args.variables:
                print(
                    get_vars( patt, items[txt] )
                )
            elif tmpl:
                response += do_evals(
                        do_tmpl(
                            ''.join(( replace( patt, tmpl, items[txt]), sepr )),
                            patt, items, txt
                            )
                        )
            else:
                response += items[txt]+sepr
    print( response.strip() )
    return 0

if __name__=="__main__":
    main()
