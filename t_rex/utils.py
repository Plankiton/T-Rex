from sys import stderr as e, exit

def die(*msg, **fmsg):
    print('\033[1;31m[!]\033[00m', *msg, **fmsg, file=e)
    exit(1)

def remove_from_list(items: list, item):
    for i in items:
        if i != item:
            yield i

def merge_lists(l1: list, l2:list):
    c = 0
    for i in l1:
        if i:
            yield i
        else:
            yield l2[c]
            c += 1

def parse_args(config: dict):
    from sys import argv
    args = argv[1:]

    if '-h' in args:
        print(f'get [OPTIONS] pattern\n------\n\nOptions:\n------\n\n -h, --help       Show this message.')
        for arg in config:
            print(f' {", ".join(arg["opt"]) if arg["opt"] else arg["name"]}       {arg["help"]}.')
        exit(0)

    limit = 0
    for arg in config:
        default = None
        if 'default' in arg:
            default = arg['default']

        value = default
        if arg['opt']:
            for opt in arg['opt']:
                if opt in args:
                    pos = args.index(opt)+1
                    value = args[pos] if arg['get_value'] else True
                    break
        else:
            for a in range(len(args)):
                if not '-' in args[a] and \
                        (not '-' in args[a-1] or a == 0)\
                        and a >= limit:
                    value = args[a]
                    limit += 1

        if not arg['optional'] and value == None:
            arg_opts = ''
            if arg['opt'] != [] and type(arg['opt']) == list:
                arg_opts = ' ('+'|'.join(arg['opt'])+')'
            die(f"The arg {arg['name']}{arg_opts} required!")

        yield dict(
            arg = arg['name'],
            value = value
        )

def read_stdin():
    from sys import stdin
    return stdin.read()
