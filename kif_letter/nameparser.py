
from urllib import request


class NameParser:
    def __init__(self, address, url):
        self.address = address
        self.url = url
        response = request.urlopen(self.url)
        self.pageContent = str(response.read())
        self.namelist = []

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

