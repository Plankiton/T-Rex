class File:
    r'''
    A abstraction for manipulation of files
    '''

    def __init__(self, dir:str = None, text:str = None):
        self.text = text
        self.dir = dir

        self.open(self.dir)


    def __str__(self) -> str:
        return f'<File: {self.dir}>'


    def __call__(self, dir:str):
        r'''
        recev a <dir> and open the file, if it do not exists, this functio will to create.

        params:
            dir:str -> directory of the file

        example:
            <File>.load('/etc/hosts')
        '''

        self.open(dir)


    def open(self, dir:str):
        r'''
        recev a <dir> and open the file, if it do not exists, this functio will to create.

        params:
            dir:str -> directory of the file

        example:
            <File>.load('/etc/hosts')
        '''

        self.dir = dir.strip()

        try:
            file = open(self.dir)
            self.text = file.read()
            file.close()

        except (FileNotFoundError, IOError):
            file = open(self.dir, 'w')
            self.text = ''
            file.close()


    def get_text(self) -> str:
        r'''
        this function returns the file text

        example:
            <File>.load('/etc/hosts')
            file_text = <File>.get_text()
        '''

        return self.text

    def write(self, text:str, append_mode:bool = False):
        r'''
        write the <text> on file

        params:
            text:str -> the text that you want to put on file
            append_mode:bool -> if it is False, the text from file is replaced by <text>
        '''

        if not append_mode:
            file = open(self.dir, 'w')
            file.write(text)
            file.close()
        else:
            file = open(self.dir, 'w')
            file.write(r'{self.text}{text}')
            file.close()

