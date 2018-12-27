from setuptools import setup, find_packages

import noobSQL.__version__ as VERSION


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='noobSQL',
    version=VERSION,
    description='SQL for noobs',
    long_description=readme,
    author='Malte Groth, Nikolas Morshuis',
    author_email='malte.groth@gmx.net, jnmorshuis@gmail.com',
    url='https://github.com/grothesk/noobSQL',
    license=license,
    packages=find_packages(exclude=('tests'))
)
