from os import sep as barra

class File:
    def __init__ (self, _file = None):
        self.dir = ''
        self.text = ''
        self.filename = _file

        if _file:
            self.text = open ( _file, 'r' ).read()

            if barra in _file:
                self.dir = _file[: _file.rindex(barra)]
                self.filename = _file[ _file.rindex(barra)+1:]

