try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'kif-letter',
    'version': '0.1.1',
    'description': 'Dieses Programm parst Adressatenlisten und formt eine Reso zu einem Serienbrief',
    'author': 'Sebastian Lau',
    'author_email': 'lauseb644@gmail.com',
    'license': 'MIT',
    'url': '',
    'download_url': '',
    #'install_requires': ['urllib'],
    'packages': ['kif-letter', 'kif-letter-nameparser-plugins', 'distutils', 'urllib'],
    'scripts': []
}

setup(**config)
