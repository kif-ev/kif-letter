import config

class TeXWriter:
    def __init__(self, out, address, namelist):
        self.outdir = out
        self.address = address
        self.namelist = namelist

        text = r"""{0}

{1}
{2}
{3}
{4}
{5}""".format(self._preamble(), self._TeXconfig(), self._TeXstart(), self._TeXbody(), self._TeXend(), self._TeXdoc())

        tex_file = open(out, encoding='utf-8', mode='w')
        tex_file.write(text)
        tex_file.close()

    def _preamble(self):
        return r"""\documentclass[a4paper,12pt]{scrlttr2}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[ngerman]{babel}
\usepackage{graphicx}
\usepackage{url}"""

    def _TeXconfig(self):
        return r"""\setkomavar{{fromname}}{{{0}}}
\setkomavar{{fromaddress}}{{{1}}}
\setkomavar{{backaddress}}{{{2}}}
\setkomavar{{date}}{{{3}}}
\setkomavar{{place}}{{{4}}}
\setkomavar{{signature}}{{{5}}}
\setkomavar{{location}}{{\hspace{{-1cm}}\includegraphics[scale=0.42]{{{6}}}}}

\urldef{{\resourl}}\url{{{7}}}""".format(config.conference_name, config.fromaddress, config.backaddress, config.date, config.place, config.signature, config.logoname)

    def _TeXstart(self):
        return r"""\newcommand{{\letterfor}}[4]{{\begin{{letter}}{{{{\ifx#4mHerrn\else Frau\fi}}\relax\\#1#2 #3\\{0}}}

\opening{{Sehr geehrte{{\ifx#4mr Herr\else\ Frau\fi}}\ #1#3,}}

die {1}{2}""".format(self.parser.get_address(), config.conference_name, config.conference_info)

    def _TeXbody(self):
        return r"""\include{reso}"""

    def _TeXend(self):
        return r"""\closing{{{0},}}

\newpage
\thispagestyle{{empty}}
\hspace{{1cm}}

\end{{letter}}}}""".format(config.closing)

    def _TeXdoc(self):

        docpart = r"""\begin{{document}}

"""
        for name in self.namelist:
            nameTeX = r"""\letterfor{{}}{{{0}}}{{{1}}}{{{2}}}
""".format(name.vorname, name.nachname, name.gender)
            docpart += nameTeX

        return docpart