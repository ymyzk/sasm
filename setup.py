#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup


setup(name='sasm',
      version='0.2.1',
      description='Simple Assembler for SIMPLE Architecture',
      author='Yusuke Miyazaki',
      author_email='miyazaki.dev@gmail.com',
      url='https://github.com/ymyzk/sasm',
      packages=['sasm'],
      scripts=['scripts/sasm'],
      test_suite='tests',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Assemblers'
      ]
      )
