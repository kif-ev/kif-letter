
from genderize.genderize import Genderize

import config


class Name:
    def __init__(self, vorname, nachname, partei):
        self.vorname = vorname
        self.nachname = nachname
        self.partei = partei

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

