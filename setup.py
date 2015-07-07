#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='neutrinet_add_event',
      version='0.1',
      description='add an event to neutrinet\'s wiki',
      author='Laurent Peuch',
      #long_description='',
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/neutrinet_add_event',
      install_requires=open("./requirements.txt", "r").read().split("\n"),
      packages=[],
      py_modules=[],
      license= '',
      scripts=['add_event'],
      keywords='',
     )
