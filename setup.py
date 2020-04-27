from setuptools import setup, find_packages


required = []
with open('requirements.txt') as f:
    for i in f.read().splitlines():
        if i[0:3] == 'git':
            name = i.split('/')[-1]
            required.append('%s @ %s@master' % (name, i))
        else:
            required.append(i)

setup(name='thematrix',
      description="Devito benchmark matrix",
      url='http://www.devitoproject.org',
      author="Devito Codes",
      author_email='g.gorman@imperial.ac.uk',
      license='MIT',
      packages=find_packages(),
      install_requires=required)
