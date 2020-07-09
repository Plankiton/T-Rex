from textanalyzer.utils import parse_args

argparser = [
    dict(
        name = 'text',
        help = 'Text inputed',
        opt = ['-t', '--text'],
        get_value = True,
        optional = True
    ),
    dict(
        name = 'pattern',
        help = 'Pattern searched',
        opt = None,
        get_value = True,
        optional = False
    ),
    dict(
        name = 'template',
        help = 'Output template',
        opt = ['-o', '--out'],
        get_value = True,
        optional = True
    ),
    dict(
        name = 'config',
        help = 'A yaml file as substitute to "--template"',
        opt = ['-c', '--config'],
        get_value = True,
        optional = True
    ),
    dict(
        name = 'sep',
        help = 'Output separate char',
        opt = ['-s', '--sep'],
        get_value = False,
        optional = True
    ),
    dict(
        name = 'breaker',
        help = 'The break char for text inputed',
        opt = ['-b', '--breaker'],
        get_value = False,
        optional = True
    )
]

if __name__ == "__main__":
    print(list(parse_args(argparser)))


