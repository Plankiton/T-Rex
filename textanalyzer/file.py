class File:
    from os import sep as barra
    def __init__ (self, _file = None):
        self.dir = '.'
        self.text = ''
        self.filename = _file
        self.object = None

        if _file:

            try:
                self.text = open ( _file, 'r' ).read()
            except:
                self.object = open( _file, 'w' )

            if barra in _file:
                self.dir = _file[: _file.rindex(barra)]
                self.filename = _file[ _file.rindex(barra)+1:]

    def write (self, text):
        self.object = open( '{}/{}'.format( self.dir, self.filename ) , 'w' )
        self.object.write( text )
