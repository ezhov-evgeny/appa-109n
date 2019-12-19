import sys

from setuptools import setup
from setuptools.command.install import install
from setuptools.command.test import test

version = "0.1"


class Install(install):
    def run(self):
        install.run(self)


class Test(test):
    user_options = [('pytest-args=', 'a', "")]

    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='appa-windmm-python',
    version=version,
    packages=['windmm'],
    install_requires=['pyserial'],
    test_suite='tests',
    cmdclass={'install': Install, 'test': Test},
    url='https://github.com/ezhov-evgeny/appa-windmm-python',
    license='Apache License 2.0',
    author='Evgeny Ezhov',
    author_email='ezhov.evgeny@gmail.com',
    description='Python cross platform driver for multimeters APPA',
    keywords='serial, windmm, python, module, library, packet, multimeter, windmm',
    classifiers=[
        'Environment :: Console',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
