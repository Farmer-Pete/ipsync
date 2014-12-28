ipsync
======
"A script to update DDNS"

[![Build Status](http://img.shields.io/travis/jon-walton/ipsync/master.svg)](https://travis-ci.org/jon-walton/ipsync)
[![Coverage Status](http://img.shields.io/coveralls/jon-walton/ipsync/master.svg)](https://coveralls.io/r/jon-walton/ipsync)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/jon-walton/ipsync.svg)](https://scrutinizer-ci.com/g/jon-walton/ipsync/?branch=master)
[![PyPI Version](http://img.shields.io/pypi/v/ipsync.svg)](https://pypi.python.org/pypi/ipsync)


Getting Started
===============

Requirements
------------

* Python 2.7+ or Python 3.3+
* libyaml-devel

Installation
------------

ipsync can be installed with pip:

```
$ pip install ipsync
```

or directly from the source code:

```
$ git clone https://github.com/jon-walton/ipsync.git
$ cd ipsync
$ python setup.py install
```

Basic Usage
===========


For Contributors
================

Requirements
------------

* Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation
* Pandoc: http://johnmacfarlane.net/pandoc/installing.html
* Graphviz: http://www.graphviz.org/Download.php

Installation
------------

Create a virtualenv:

```
$ make env
```

Run the tests:

```
$ make test
$ make tests  # includes integration tests
```

Build the documentation:

```
$ make doc
```

Run static analysis:

```
$ make pep8
$ make pep257
$ make pylint
$ make check  # includes all checks
```

Prepare a release:

```
$ make dist  # dry run
$ make upload
```
