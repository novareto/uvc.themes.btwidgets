1# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages

name = 'uvc.themes.btwidgets'
version = '0.1-dev'
readme = open('README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read()


install_requires = [
    'dolmen.forms.ztk',  # this will go inside a conditional import
    'cromlech.browser',  # Likewise
    'fanstatic',
    'js.bootstrap',
    'zope.interface',
    ]


tests_require = [
    ]


setup(name=name,
      version=version,
      description=("UVC Theme for Bootstrap widgets"),
      long_description=readme + '\n\n' + history,
      keywords='',
      author='Novareto',
      author_email='',
      url='',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['uvc', 'uvc.themes'],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Other Audience',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
      entry_points={
        }
      )
