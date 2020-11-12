from setuptools import setup

setup(
   name='ames_qsar',
   version='1.0',
   description='small hydrocarbon QSAR for direct acting Ames test mutagens',
   author='Trevor Sleight',
   author_email='twsleight@gmail.com',
   packages=['ames_qsar'],  #same as name
   install_requires=['numpy~=1.19', 'pandas>=1.1'], #external packages as dependencies
)
