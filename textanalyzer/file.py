from os import sep as ossepbar
class File:
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

            if ossepbar in _file:
                self.dir = _file[: _file.rindex(ossepbar)]
                self.filename = _file[ _file.rindex(ossepbar)+1:]

    def write (self, text):
        self.object = open(f'{self.dir}/{self.filename}', 'w' )
        self.object.write( text )

    def close (self):
        self.object.close()
