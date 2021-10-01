# Table of Contents

# pyTemplate

This is a template python package. There's mostly some basic statistics and linear algebra routines.

## Environment Setup

### Python

This python library uses Anaconda as a package manager, so we will begin with it's
installation

## Anaconda3

To install Anaconda3 on MacOS or Windows, visit the install page
[here](https://docs.anaconda.com/anaconda/install/mac-os/) for MacOS or
[here](https://docs.anaconda.com/anaconda/install/windows/) for Windows, and
follow the directions.

Alternatively, if you use [homebrew](https://brew.sh/) on MacOS, you can install with

```bash
brew install --cask anaconda
```

or if you use [chocolatey](https://chocolatey.org) on Windows, you can install with

```bash
choco install anaconda3
```

### Linux

On Linux installation instructions are provided
[here](https://docs.anaconda.com/anaconda/install/linux/) for on a Linux machine
which we repeat below for Debian based systems. First, install the prerequisites
by running

```bash
apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
```

Then, install the installer with something like:

```bash
wget --directory-prefix=$HOME/Downloads https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
```

Then, run the installer

```bash
bash ~/Downloads/Anaconda3-2020.02-Linux-x86_64.sh
```
and follow any instructions.

<a id="org2edd6b8"></a>

## Virtual Environment

Once you have Anaconda installed, we will use it to create a virtual environment
to install any module prerequisites. Create the virtual environment named
template-python by running the following in your shell

```bash
conda env create -f environment.yml
```

Alternatively, if you have make installed on your system, you can run
```bash
make create_environment
```

Once the environment is created, we can activate it with

```bash
conda activate pytemplate
```

You may need to run `conda init` if this is the first time activating an Anaconda
virtual environment. Now, once you have the anaconda environment activated, we
use pip to install the package to our environment.

```bash
pip install .
```

You will need to do this step every time you want to use new code in a python
shell/repl. Now that we have installed the project, we can test it
out by opening a python shell and running the following code:

```python
import pytemplate
```

and check the package version by running

```python
pytemplate.__version__
```

### Package tooling
(TODO: move this section to CONTRIBUTING.md and keep this document for installation and usage)

Installed in the conda environment are several python packages providing tools
for package development. In particular, we are using
[tox](https://github.com/tox-dev/tox) for automating running tests (using
[pytest](https://github.com/pytest-dev/pytest)), benchmarks (using
[pytest-benchmark](https://github.com/ionelmc/pytest-benchmark/)), coverage
(using and [Coverage.py](https://github.com/nedbat/coveragepy) and
[pytest-cov](https://github.com/pytest-dev/pytest-cov),
[flake8](https://github.com/pycqa/flake8) for linting and documentation (using
[Sphinx](https://github.com/sphinx-doc/sphinx/)).

Everything is automated so that you can run
```bash
tox
```

from within the pytemplate conda environment.

Alternatively, you can run pytest, or sphinx individually within the
console/command prompt. There is a Makefile that gives commands for this
workflow. If you do not already have Make installed, you can install by
following the instructions
[here](https://www.gnu.org/software/make/). Alternatively, on MacOS, you can
follow the instructions
[here](https://stackoverflow.com/questions/10265742/how-to-install-make-and-gcc-on-a-mac)
or install via homebrew:

```bash
brew install make
```

On windows, you can also install via chocolatey:

```bash
choco install make
```


See the CONTRIBUTING.md document for more instructions on this workflow.
