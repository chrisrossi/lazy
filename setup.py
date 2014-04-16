import os
from sys import version

from setuptools import setup, find_packages

VERSION = '1.0'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = []
tests_require = install_requires + ['coverage', 'nose']
docs_require = install_requires + ['sphinx']

if version < '2.7':
    tests_require.append('unittest2')

setup(name='lazy',
      version=VERSION,
      description='Provides lazy sequences from iterators.',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "License :: Repoze Public License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        ],
      keywords='functional',
      author="Chris Rossi",
      author_email="chris@archimedeanco.com",
      #url="http://docs.pylonsproject.org",
      #license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={
          'tests': tests_require,
          'docs': docs_require},
      test_suite="lazy",
     )
