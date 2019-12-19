from setuptools import setup

version = "0.1"

setup(
    name='appa-windmm-python',
    version=version,
    packages=['windmm'],
    install_requires=['pyserial'],
    test_suite='tests',
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
