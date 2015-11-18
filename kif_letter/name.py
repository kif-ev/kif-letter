
from genderize.genderize import Genderize
from unidecode import unidecode

import config


class Name:
    def __init__(self, vorname, nachname, partei):
        self.vorname = unidecode(vorname)
        self.nachname = unidecode(nachname)
        self.partei = unidecode(partei)

        if config.genderize_io:
            gender = Genderize().get(vorname)
            if gender[0]['gender'] == 'male':
                self.gender = 'm'
            elif gender[0]['gender'] == 'female':
                self.gender = 'f'
            else:
                self.gender = ''
        else:
            self.gender = ''

    def printout(self):
        name_str = self.nachname + ', ' + self.vorname + ' (' + self.gender + ', ' + self.partei + ')'
        return name_str

