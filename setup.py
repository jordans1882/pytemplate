import re
from setuptools import setup, find_packages


def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop),
                       open(project + '/_version.py').read())
    return result.group(1)


with open("readme.md", "r") as fh:
    long_description = fh.read()

PROJECT_NAME = "pytemplate"

setup(
    name="pytemplate",
    version=get_property('__version__', PROJECT_NAME),
    author="Jordan Schupbach",
    author_email="jordans1882@gmail.com",
    description="A template python library",
    keywords="python, template",
    long_description=open('readme.md').read(),
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jordans1882/pytemplate",
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="GPL3",
    # license=read_text("LICENSE.txt"),
    include_package_data=True,
    # package_data={'': ['_assets/example_images/*.png']},
)
