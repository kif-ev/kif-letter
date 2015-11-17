
import re
import html.parser

from nameparser import *
from name import Name


class BundestagParser(NameParser):

    def _shorten_page_content(self):
        start = str.find(self.pageContent, "Alphabetische Liste aller Mitglieder")
        end = str.find(self.pageContent, "<p>* ausgeschieden")
        if start == -1 or end == -1:
            raise ParserException("Bundestag", "Delimiters not found")
        else:
            self.pageContent = self.pageContent[start:end]

    def __init__(self):
        NameParser.__init__(self, "Platz der Republik 1\n11011 Berlin", "https://www.bundestag.de/bundestag/abgeordnete18/alphabet")
        self._shorten_page_content()
        self._make_name_list()

    def _make_name_list(self):
        lines = re.split('\n', self.pageContent)

        for l in lines:
            if l == '<div class="linkIntern">':
                nametokens = (l+1).split()
                for nameindex, nt in enumerate(nametokens):
                    if nt == '>':
                        nachname = nt[:-2]
                        vorname = nametokens[nameindex+1][:-2]
                        partei = nametokens[nameindex+2][:-5]
                        name = Name(vorname, nachname, partei)
                        self.namelist.append(name)
                        print('Added ')
                        name.printout()
                        break

