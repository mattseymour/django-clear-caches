import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-clear-caches',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Django management command for clearing caches',
    long_description='''
    Django management command which allows for the user to clear any (or all)
    the defined setting CACHES.
    ''',
    url='https://www.mattseymour.net/',
    author='Matt Seymour',
    author_email='mattaseymour@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
