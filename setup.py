from setuptools import setup

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
   name='ames_qsar',
   version='1.0',
   description='small hydrocarbon QSAR for direct acting Ames test mutagens',
   author='Trevor Sleight',
   author_email='twsleight@gmail.com',
   packages=find_packages(),  #same as name
   install_requires=requirements, #external packages as dependencies
)
