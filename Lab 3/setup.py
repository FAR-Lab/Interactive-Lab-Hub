from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from os import path
import io

here = path.abspath(path.dirname(__file__))

setup(

    name='sparkfun-qwiic-joystick',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version='0.9.0',

    description='SparkFun Electronics qwiic Joystick',

    # The project's main homepage.
    url='https://www.sparkfun.com/products/15168',

    # Author details
    author='SparkFun Electronics',
    author_email='info@sparkfun.com',

    install_requires=['sparkfun_qwiic_i2c'],

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
       'Programming Language :: Python :: 2.7',
       'Programming Language :: Python :: 3.5',
       'Programming Language :: Python :: 3.6',
       'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='electronics, maker',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    py_modules=["qwiic_joystick"],

)