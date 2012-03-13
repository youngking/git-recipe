# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="git-recipe",
    version='0.0.1',
    description='Simple buildout recipe for downloading git repositories. It uses system git command and its syntax',
    author='Young King',
    author_email='yanckin@gmail.com',
    url='http://github.com/youngking/git-recipe',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Natural Language :: Russian',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.5',
        'Topic :: Software Development :: Version Control',
    ],
    namespace_packages=['recipe'],
    packages=find_packages(),
    install_requires=['setuptools', 'zc.recipe.egg'],
    entry_points={'zc.buildout': ['default = recipe.git:GitRecipe']},
    zip_safe=False,
    long_description=open('README.rst').read(),
)
