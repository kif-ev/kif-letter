
from gender_detector import gender_detector  # https://pypi.python.org/pypi/gender-detector/0.0.4
#from gendercomputer import genderComputer  # https://github.com/tue-mdse/genderComputer


class Name:
    def __init__(self, vorname, nachname, partei):
        self.vorname = vorname
        self.nachname = nachname
        self.partei = partei
        gd = gender_detector ('uk')
        gender = gd.guess(vorname)
        if gender == 'male':
            self.gender = 'm'
        elif gender == 'female':
            self.gender = 'f'
        else:
            self.gender = ''

    def printout(self):
        print('{0}, {1} ({2}, {3})'.format(self.nachname, self.vorname, self.gender, self.partei))
