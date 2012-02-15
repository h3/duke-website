from setuptools import setup, find_packages

setup(
    name = "duke-website",
    version = "0.0.1",
    url = 'https://github.com/h3/duke-website',
    license = 'BSD',
    description = "Duke website",
    author = 'Maxime Haineault',
    packages = find_packages('.duke/eggs/'),
    package_dir = {'': '.'},
    install_requires = ['distribute'],
)
