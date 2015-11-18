
import sys
import os

from kif_letter.nameparser import NameParser as NP
import nameparser_plugins
from kif_letter.texwriter import TeXWriter


def main():
    argc = len(sys.argv)
    out = ''
    parsername = ''
    if argc == 5:
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
    else:
        print("Usage: kif_letter.py -o OUTFILE -p PARSERNAME")
        os.abort()


    namelist = []
    address = ''
    if parsername != '':
        parser = NP.create_nonfunctional()
        if parsername == 'bundestag':
             parser = nameparser_plugins.BundestagParser()
        else:
            print("Parser '%s' does not exist.")
            os.abort()

        namelist = parser.get_names()
        address = parser.get_address()
    else:
        print("Don't parsing any names")

    if out != '':
        tex = TeXWriter(out, address, namelist)
    else:
        print("Cannot write TeX files")
        os.abort()




if __name__ == "__main__":
    main()
