import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rluafunctions',
    version='0.0.2',
    author='roninmaster21',
    author_email='',
    description='Use common rlua functions and libraries in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/roninmaster21/rluafunctions',
    project_urls = {"Bug Tracker":'https://github.com/roninmaster21/rluafunctions'},
    license='MIT',
    packages=['rluafunctions'],
)
