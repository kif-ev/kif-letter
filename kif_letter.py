#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

from kif_letter.nameparser import NameParser as NP
import kif_letter.nameparser_plugins as NPP
from kif_letter.texwriter import TeXWriter


def main():
    os.environ["PYTHONIOENCODING"] = 'utf-8'
    argc = len(sys.argv)
    out = ''
    parsername = ''
    url = ''
    if argc >= 5:
        for arg_indx, arg in enumerate(sys.argv):
            if arg_indx == 0:  # Skip script name
                continue
            if argc < arg_indx+1:
                print("Cannot parse parameter '%s'" % arg )
                os.abort()

            if arg == '-o' or arg == '--out':
               out = sys.argv[arg_indx+1]
            elif arg == '-p' or arg == '--parser':
                parsername = sys.argv[arg_indx+1]
                if parsername == 'wikitable' and argc < 6:
                    print("You have to provide a url to a table on de.wikipedia.org")
                    exit(1)
            elif arg_indx == 5:
                url = sys.argv[arg_indx]
                if url.find("http") == -1:
                    print "'{}' is no valid url".format(utl)

    else:
        print("Usage: kif_letter.py -o OUTFILE -p PARSERNAME [URL]")
        exit(0)

    if len(out) == 0:
        print("\nCannot write TeX files\n")
        exit(1)

    namelist = []
    address = ''
    if parsername != '':
        parser = NP.create_nonfunctional()
        if parsername == 'bundestag':
            parser = NPP.WikiTableParser("Platz der Republik 1\n11011 Berlin", \
                                         NPP.WikiTableParser.WIKI_PAGE + "Liste_der_Mitglieder_des_Deutschen_Bundestages_(18._Wahlperiode)")
            #parser = NPP.BundestagParser()
        elif parsername == 'wikiparser':
            if len(url) == 0 or url.find("de.wikipedia.org") == -1:
                print "'{}' is no valid wikipedia url...".format(url)
                exit(1)
            parser = NPP.WikiTableParser(config.toadress, url)
        else:
            print("Parser '%s' does not exist.")
            exit(1)

        namelist = parser.get_names()
        address = parser.get_address()
    else:
        print("Don't parsing any names")

    if out != '':
        tex = TeXWriter(out, address, namelist)
        print("\nWrote TeX letter to %s\n" % out)

    if len(parser.unknown_gender ) > 0:
        print("Could not detect a gender for following names:")
        for name in parser.unknown_gender:
            print("%s" % name)
        print("Please train an re-submit the dictionary at 'kif_letter/gender_detector/data/usprocessed.csv'")


if __name__ == "__main__":
    main()
