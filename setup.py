#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup


setup(name='sasm',
      version='0.2',
      description='Simple Assembler for SIMPLE Architecture',
      author='Yusuke Miyazaki',
      author_email='miyazaki.dev@gmail.com',
      url='https://github.com/litesystems/sasm',
      packages=['sasm'],
      scripts=['scripts/sasm'],
      test_suite='tests',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Assemblers'
      ]
      )
