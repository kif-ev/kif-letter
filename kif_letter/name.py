

from .genderdetect import genderDetector


class Name:
    def __init__(self, vorname, nachname, partei):
        self.vorname = vorname
        self.vorname_raw = vorname
        self.nachname = nachname
        self.partei = partei

        # Vornamen auf elementaren Teil reduzieren
        dotted_prefix_end = self.vorname_raw.rfind('. ')
        if dotted_prefix_end > -1:
            self.vorname_raw = self.vorname_raw[dotted_prefix_end+2:]
        double_name_splitter = self.vorname_raw.rfind('-')
        if double_name_splitter > -1:
            self.vorname_raw = self.vorname_raw.partition('-')[0]
        # Strip other suffixes
        van_sufix = self.vorname_raw.rfind(' van')
        if van_sufix > -1:
            self.vorname_raw = self.vorname_raw[:van_sufix]

        print("Guessing gender of %s" % self.vorname_raw)
        gender = genderDetector.guess(self.vorname_raw)
        if gender == 'male':
            self.gender = 'm'
        elif gender == 'female':
            self.gender = 'f'
        else:
            self.gender = ''
        print("Gender detected: '%s'" % gender)

    def printout(self):
        name_str = self.nachname + ', ' + self.vorname + ' (' + self.gender + ', ' + self.partei + ')'
        return name_str

