#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs


conference_name = '43,5. Konferenz der deutschsprachigen Informatik-Fachschaften'
conference_info = r"""\footnote{Wikipedia: Konferenz der Informatikfachschaften (\url{https://de.wikipedia.org/wiki/Konferenz_der_Informatikfachschaften}) und Was ist die KIF? (\url{https://kif.fsinf.de/wiki/Was_ist_die_KIF}). Diesen Brief finden Sie auch unter \resourl.}"""
fromaddress = r"""c/o Fachschaft Informatik am Institut für Informatik der Unversität Bonn\\Römerstraße 164\\53117 Bonn"""
backaddress = r"""{0}, {1}""".format(conference_name, fromaddress)
date = "15. November 2014"
place = "Bonn"
signature = "die Teilnehmer und Teilnehmerinnen der {0}".format(conference_name)
logoname = "465px-Kif_logo_435"
resourl = """https://kif.fsinf.de/wiki/KIF435:Resolutionen/Wissenschaftszeitvertragsgesetz"""
closing = "Hochachtungsvoll"

# Possible values 'Default', 'GenderizeIO'
genderdetector = 'Default'
