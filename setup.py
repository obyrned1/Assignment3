from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='ledGrid',
    version=__version__,
    description='A package to turn on and off lights on a grid',
    long_description=long_description,
    url='https://github.com/obyrned1/ledGrid',
    download_url='https://github.com/obyrned1/ledGrid/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    entry_points={'console_scripts':['ledGrid=ledGrid.main:main']},
    include_package_data=True,
    author='Daniel O Byrne',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='daniel.obyrne@ucdconnect.ie'
)
