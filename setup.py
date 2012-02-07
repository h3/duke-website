from setuptools import setup, find_packages

setup(
    name = "duke-website",
    version = "1.0",
    url = 'https://github.com/h3/duke-website',
    license = 'BSD',
    description = "Duke website",
    author = 'Maxime Haineault',
    packages = find_packages('eggs'),
    package_dir = {'': 'eggs'},
    install_requires = ['distribute'],
)
