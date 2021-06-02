from setuptools import setup
from os.path import join, dirname


setup(
    name = 'custom_serialiser_by_lena',
    version = '1.0',
    long_description = open(join(dirname(__file__),"README.md")).read(),
    author = 'Elena Barkovskaya',
    packages = ['custom_serializer'],
    entry_points = {
        'console_scripts': ['custom_serialiser = console_app:main',
         ], 
    }

)