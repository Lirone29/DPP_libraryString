from setuptools import setup, find_packages

setup(
    name='makeWordsFunny',
    version='1.4',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Library for DPP lab 10',
    long_description=open('README.md').read(),
    install_requires=[''],
    url='https://github.com/Lirone29/DPP_libPython',
    author='Eliza',
    author_email='kalata.eliza@gmail.com'
)