#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs


conference_name = '44,0. Konferenz der Informatik-Fachschaften'
conference_info = r"""\footnote{Wikipedia: Konferenz der Informatikfachschaften (\url{https://de.wikipedia.org/wiki/Konferenz_der_Informatikfachschaften}) und Was ist die KIF? (\url{https://kif.fsinf.de/wiki/Was_ist_die_KIF}). Diesen Brief finden Sie auch unter \resourl.}"""
fromaddress = r"""c/o Technische Universität Darmstadt\\Fachschaft Informatik\\Hochschulstr.\\64289 Darmstadt"""
backaddress = r"""{0}, {1}""".format(conference_name, fromaddress)
toaddress = r""""""
date = "08. Mai 2016"
place = "Darmstadt"
signature = "die Teilnehmer und Teilnehmerinnen der {0}".format(conference_name)
logoname = "Kif_logo_440.png"
scalefactor = 0.05
resourl = """https://kif.fsinf.de/wiki/KIF435:Resolutionen/Wissenschaftszeitvertragsgesetz"""
closing = "Hochachtungsvoll"

