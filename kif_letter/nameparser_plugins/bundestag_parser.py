
from nameparser import *
from name import Name


class BundestagParser(NameParser):

    def _shorten_page_content(self):
        start = str.find(self.pageContent, '        <ul class="standardLinkliste">')
        end = str.find(self.pageContent, "<p>* ausgeschieden")
        if start == -1 or end == -1:
            raise ParserException("Bundestag", "Delimiters not found")
        else:
            self.pageContent = self.pageContent[start:end]

    def __init__(self):
        NameParser.__init__(self, "Platz der Republik 1\n11011 Berlin", """https://www.bundestag.de/bundestag/abgeordnete18/alphabet""")
        self._shorten_page_content()
        self._make_name_list()

    def _make_name_list(self):
        lines = self.pageContent.split('\n', self.pageContent.count('\n'))

        for line_index, l in enumerate(lines):
            if l == '                        <div class="linkIntern">':
                nametokens = lines[line_index+2].split(',')
                if len(nametokens) != 3:
                    raise ParserException("Bundestag", "'%s' is not a name token" % lines[line_index+2])
                if str.find(nametokens[2], '*') != -1:  # SKIP ausgeschiedene Abgeordnete
                    continue
                tag_end = str.find(nametokens[2], '<')
                nametokens[2] = nametokens[2][:tag_end]
                for index, token in enumerate(nametokens):
                    token = token.lstrip()
                    token = token.encode().decode()
                    if index == 0:
                        nachname = token
                    elif index == 1:
                        vorname = token
                    elif index == 2:
                        partei = token
                name = Name(vorname, nachname, partei)
                self.namelist.append(name)
                print('Added %s' % name.printout())

