'''
Get Tool
'''

from textanalyzer.utils import parse_args, read_stdin
from textanalyzer import REGEX as r, get_vars, replace, search

argparser = [
    dict(
        name='text',
        help='Text inputed',
        opt=['-t', '--text'],
        get_value=True,
        optional=True
    ),
    dict(
        name='pattern',
        help='Pattern searched',
        opt=None,
        get_value=True,
        optional=False
    ),
    dict(
        name='template',
        help='Output template',
        opt=['-o', '--out'],
        get_value=True,
        optional=True
    ),
    dict(
        name='config',
        help='A yaml file as substitute to "--out"',
        opt=['-c', '--config'],
        get_value=True,
        optional=True
    ),
    dict(
        name='sep',
        help='Output separate char',
        opt=['-s', '--sep'],
        get_value=True,
        optional=True
    ),
    dict(
        name='breaker',
        help='The break char for text inputed',
        opt=['-b', '--breaker'],
        get_value=True,
        optional=True,
        default='\n'
    ),
    dict(
        name='match',
        help='The matched text.',
        opt=['-m', '--match'],
        get_value=False,
        optional=True,
        default=False
    )
]

def do_replace(*_a):
    return replace(_a[0], _a[1], _a[2])

def do_search(*_a):
    r = search(_a[0], _a[-1])

    if r:
        if _a[-2] and len(_a)>2:
            return r.group()

        match = r.string[r.start():r.end()]
        begin = r.string[:r.start()]
        end = r.string[r.end():]

        return f'{begin}\033[1;31m{match}\033[00m{end}'
    return r

if __name__ == "__main__":
    args = {}
    for arg in parse_args(argparser):
        args[arg['arg']] = arg['value']

    input_text = None
    if args['text']:
        input_text = args['text']
    else:
        input_text = read_stdin()

    operation = do_search
    _args = [args['pattern'], args['match']]

    if args['template']:
        operation = do_replace
        _args = [args['pattern'], args['template']]

    response = None
    for line in input_text.split(args['breaker']):
        args = [a for a in _args]+[line]
        response = operation(*args)
        if response:
            print(response)

