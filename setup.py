try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Alex Goncalves',
    'url': 'None',
    'download_url': 'None',
    'author_email': 'aalex.goncalves@icloud.com',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
