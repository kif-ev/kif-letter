try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'kif-letter',
    'version': '0.1.1',
    'description': 'Dieses Script parst alle Abgeordneten des Bundestages, erstellt den Rahmen für einen Serienbrief und fügt als Text eine Resolution und eventuelle weitere Texte aus TeX-Dateien ein.',
    'author': 'Sebastian Lau',
    'author_email': 'lauseb644@gmail.com',
    'url': '',
    'download_url': '',
    'install_requires': [''],
    'packages': ['kif-letter'],
    'scripts': []
}

setup(**config)
