
import urllib

from name import Name


class NameParser:
    def __init__(self, address, url):
        self.address = address
        self.url = url
        if url != '':
            response = urllib.urlopen(self.url).read()
            self.pageContent = response
        else:
            self.pageContent = ''
        self.namelist = []
        self.unknown_gender = []

    @classmethod
    def create_nonfunctional(self):
        return NameParser('', '')

    def get_address(self):
        return self.address

    def get_names(self):
        return self.namelist

    def add_name(self, name):
        self.namelist.append(name)

    def _make_name(self, vorname, nachname, partei):
        name = Name(vorname, nachname, partei)
        self.namelist.append(name)
        print('Added %s' % name.printout())
        if name.gender == '':
            self.unknown_gender.append(name.vorname_raw)


class ParserException(Exception):
    def __init__(self, parsertype, msg):
        self.val = msg
        self.parsertype = parsertype

    def __str__(self):
        return "ParserException[" + parsertype + "]: " + self.val

