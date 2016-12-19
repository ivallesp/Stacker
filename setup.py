# -*- coding: utf-8 -*-
__author__ = 'ivanvallesperez'

from setuptools import setup

setup(name='Stacker',
      version='2.0',
      description='Stacker for combining pattern classifiers',
      url='http://github.com/ivallesp/stacker',
      author='Ivan Valles Perez',
      author_email='ivanvallesperez@gmail.com',
      install_requires=[
          "pandas>=0.17.1",
          "numpy>=1.10.4",
          "scikit-learn>=0.17.1"
      ],
      test_requires=[
          "pandas>=0.17.1",
          "numpy>=1.10.4",
          "scikit-learn>=0.17.1",
          "xgboost==0.4"
      ],
      packages=['Stacker'],
      zip_safe=False)
