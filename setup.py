try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'kif-letter',
    'version': '0.2.0',
    'description': 'Dieses Programm parst Adressatenlisten und formt eine Reso zu einem Serienbrief',
    'author': 'Sebastian Lau',
    'author_email': 'lauseb644@gmail.com',
    'license': 'MIT',
    'url': 'https://github.com/kif-ev/kif-letter/',
    'download_url': 'https://github.com/kif-ev/kif-letter.git',
    'install_requires': ['urllib', 'os', 'sys', 'distutils.core', 'setuptools', 'codecs'],
    'packages': ['kif_letter'],
    'scripts': ['kif_letter.py']
}

setup(**config)
