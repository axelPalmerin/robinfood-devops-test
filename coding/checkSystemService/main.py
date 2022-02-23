#!/usr/bin/env python3

"""
This microservice checks some automated system valitations using pytest.
"""

from tests.tests import TestCases
from defs import constants as c

class CheckSystem(object):

    def __init__(self):
        runTests = TestCases()

if __name__ == "__main__":
    CheckSystem()
