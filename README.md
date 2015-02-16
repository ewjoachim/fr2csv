Transforms a CSV file that can be either well written or oddly writen
(with commas as decimal separator and semicolon as field separator) to a
normal CSV file (as in RFC 4180).

Usage :
=======

    fr2csv.py <inputfile> <outputfile>

For both in and out, "-" means standard in/output.

As a lib
========

Import AgnosticReader and use it like csv.dictReader. If you need to access
the csv.DictReader used internally, it's myreader.dict_reader