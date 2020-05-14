
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()


with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='AITraining-Project1',
    version='0.1.0',
    description='AI training project for 10 days',
    long_description=readme,
    author='Bikash Gupta',
    author_email='bikashgup@hotmail.com',
    url='https://github.com/bikashgup/AITraining-Project1',
    license=license,
    packages=find_packages()
)
