from setuptools import setup

setup (
        name='bingback',
        version='1.0',
        description='This package have 3 method. one for get the url of the day you want. one for get a list of urls by pass the range. one for set background by pass the day. It can run from command line and change desktop background.',
        url='https://git.pe42.ir/roozbeh/Bingback-Package',
        author='Wabbajack',
        author_email='roozbeh279@gmail.com',
        packages=['bingback'],
        install_requires=['datetime'],
        zip_safe=False,
    )
