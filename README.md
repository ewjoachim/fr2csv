fr2csv
======

[![PyPI version](https://badge.fury.io/py/fr2csv.svg)](http://badge.fury.io/py/fr2csv)
[![Build Status](https://travis-ci.org/ewjoachim/fr2csv.svg?branch=master)](https://travis-ci.org/ewjoachim/fr2csv)

Transforms a CSV file that can be either well written or oddly writen
(with commas as decimal separator and semicolon as field separator) to a
normal CSV file (as in RFC 4180).

CLI Usage :
===========

    fr2csv.py <inputfile> <outputfile>

For both in and out, "-" means standard in/output.

As a lib :
==========

Import AgnosticReader and use it like csv.dictReader. If you need to access
the csv.DictReader used internally, it's myreader.dict_reader


Run tests
=========

python -m unittest test
