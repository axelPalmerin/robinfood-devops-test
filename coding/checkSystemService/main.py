#!/usr/bin/env python3


"""
This microservice checks some automated system valitations.
"""

import os
import sys
import logging

from testinfra import get_host
from unittest import TextTestRunner, makeSuite, TestSuite
from xmlrunner import XMLTestRunner

from tests.tests import SomeChecks
from defs import constants as c

class CheckSystem(object):

    def __init__(self):
        logfile = "out.log"
        if not os.path.isfile(logfile):
            open(logfile, "a+")
        logging.basicConfig(level=logging.INFO, filename=logfile)
        self.host = get_host(os.getenv("HOST", "local://"))

    def setUpTest(self, testClass):
        testClass.host = self.host
        return testClass

    def geTestInfo(self):
        logging.debug('\nHost: {}\nProject: {}\nEnv: {}\n'.format(self.host,
         c.project, c.env))

    def runChecks(self):
        currentTest = self.setUpTest(SomeChecks)
        ts = TestSuite(makeSuite(currentTest, 'test'))
        result = XMLTestRunner(output='%s' % c.xmlPathToSave).run(ts)

if __name__ == "__main__":
    app = CheckSystem()
    app.geTestInfo()
    app.runChecks()
