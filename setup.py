# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='POsint',
    version="1.2",
    packages=find_packages(),
    author="BossNetworkk",
    author_email="bossnetworrkk@gmail.com",
    install_requires=["termcolor","bs4","httpx","trio","argparse","tqdm"],
    description="Bir nece sosyal mediada nomrenin varligini yoxlamaq.",
    include_package_data=True,
    url='http://github.com/megadose/phone-osint',
    entry_points = {'console_scripts': ['ignorant = ignorant.core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
