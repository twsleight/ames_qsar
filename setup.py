from setuptools import setup

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
   name='amesQSAR',
   version='1.0',
   description='small hydrocarbon QSAR for direct acting Ames test mutagens',
   author='Trevor Sleight',
   author_email='twsleight@gmail.com',
   packages=['amesQSAR'],  #same as name
   install_requires=requirements, #external packages as dependencies
)
