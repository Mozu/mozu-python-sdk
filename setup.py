from distutils.core import setup

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mozurestsdk'))
from config import __version__

long_description="""
    1. https://github.com/mozu/mozu-pyton-sdk/ - README
    2. https://developer.mozu.com/api - API Reference
  """

license='Apache License'
if os.path.exists('LICENSE'):
  license = open('LICENSE').read()

setup(
  name="mozurestsdk",
  version= __version__,
  author='Mozu',
  author_email='integrations@mozu.com',
  packages=['mozurestsdk'],
  scripts=[],
  url="https://github.com/mozu/mozu-python-sdk",
  license=license,
  description='Mozu Rest SDK.',
  long_description=long_description,
  install_requires=['requests>=2.7.0', 'six>=1.9.0'],
  classifiers=[
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  keywords=['mozu', 'rest', 'sdk']
)
