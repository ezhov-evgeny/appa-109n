from setuptools import setup

version = "0.1"

setup(
    name='appa-python',
    version=version,
    packages=['appa'],
    install_requires=['pyserial'],
    test_suite='tests',
    url='https://github.com/ezhov-evgeny/appa-109n',
    license='Apache License 2.0',
    author='Evgeny Ezhov',
    author_email='ezhov.evgeny@gmail.com',
    description='Python cross platform driver for multimeters APPA',
    keywords='serial, appa, python, module, library, packet, multimeter, windmm',
    classifiers=[
        'Environment :: Console',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
