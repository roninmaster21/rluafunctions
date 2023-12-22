import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rfunctions',
    version='0.0.2',
    author='roninmaster21',
    author_email='',
    description='Use common rlua functions and libraries in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/roninmaster21/rfunctions',
    project_urls = {},
    license='MIT',
    packages=['rfunctions'],
)
