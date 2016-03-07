

from genderize.genderize import Genderize
from unidecode import unidecode

import config
from genderdetect import genderDetector


class Name:
    def __init__(self, vorname, nachname, partei):
        self.vorname = vorname
        self.nachname = nachname
        self.partei = partei

        if config.genderdetector == 'GenderizeIO':
            gender = Genderize().get(vorname)
            if gender[0]['gender'] == 'male':
                self.gender = 'm'
            elif gender[0]['gender'] == 'female':
                self.gender = 'f'
            else:
                self.gender = ''
        else:
            gender = genderDetector.guess(self.vorname)
            if gender == 'male':
                self.gender = 'm'
            elif gender == 'female':
                self.gender = 'f'
            else:
                self.gender = ''

    def printout(self):
        name_str = self.nachname + ', ' + self.vorname + ' (' + self.gender + ', ' + self.partei + ')'
        return name_str

