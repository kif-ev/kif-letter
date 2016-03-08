
from urllib import request
import codecs

class NameParser:
    def __init__(self, address, url):
        self.address = address
        self.url = url
        if url != '':
            response = request.urlopen(self.url).read()
            self.pageContent = response.decode()
        else:
            self.pageContent = ''
        self.namelist = []

    @classmethod
    def create_nonfunctional(self):
        return NameParser('', '')

    def get_address(self):
        return self.address

    def get_names(self):
        return self.namelist

    def add_name(self, name):
        self.namelist.append(name)


class ParserException(Exception):
    def __init__(self, parsertype, msg):
        self.val = msg
        self.parsertype = parsertype

    def __str__(self):
        return "ParserException[" + parsertype + "]: " + self.val

