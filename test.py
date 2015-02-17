# -*- coding: utf-8 -*-

# Copyright (c) 2015 Joachim Jablon

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Python Future imports
from __future__ import unicode_literals

# Python System imports
from unittest import TestCase
import subprocess


class Fr2CsvTest(TestCase):
    def test_cli_stdin_stdout(self):
        """
        Tests that Command Line Interface produces the right result on a
        simple test.
        """
        process = subprocess.Popen(
            ["fr2csv", "-", "-"],
            stdout=subprocess.PIPE, stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        stdout = process.communicate(input=b"""a;b\n1,2;azerty""")[0]

        self.assertEqual(stdout, b"""a,b\r\n1.2,azerty\r\n""")
