import os

from setuptools import find_packages, setup

BASE_PATH = os.path.dirname(__file__)


setup(
    name='skoleni',
    version="0.0.1",
    description="skoleni RedHat",
    packages=find_packages(),
    license='GPLv3+',
    author='Red Hat',
    author_email='busovaha@gmail.com',
    url='https://github.com/busovaha/skoleni_redhat',
    zip_safe=True
)
