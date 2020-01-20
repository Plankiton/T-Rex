class Language:
    def __init__(self, _dictionary, _text):
        self.dictionary = _dictionary
        self.text = _text

    # Identing texts
    def ident(self, _rules):
        _text = self.text

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
