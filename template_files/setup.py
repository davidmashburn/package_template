from distutils.core import setup

# Read the version number
with open("package_template/_version.py") as f:
    exec(f.read())

setup(
    name='package_template',
    version=__version__, # use the same version that's in _version.py
    author='David N. Mashburn',
    author_email='david.n.mashburn@gmail.com',
    packages=['package_template'],
    scripts=[],
    url='http://pypi.python.org/pypi/package_template/',
    license='LICENSE.txt',
    description='<ADD DESCRIPTION>',
    long_description=open('README.txt').read(),
    install_requires=[
                      
                     ],
)