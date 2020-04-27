from setuptools import setup

with open('requirements.txt') as f:
    required=f.read().splitlines()

setup(name='thematrix',
      description="Devito benchmark matrix",
      url='http://www.devitoproject.org',
      author="Devito Codes",
      author_email='g.gorman@imperial.ac.uk',
      license='MIT',
      packages=['thematrix'],
      install_requires=required)
