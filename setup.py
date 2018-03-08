from setuptools import setup, find_packages

setup(
    name='bestpkg',
    version='0.0.0',
    description='import the best X pkg',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
