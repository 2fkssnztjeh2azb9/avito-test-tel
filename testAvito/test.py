import unittest
from tests.testcheckoutphonenumber import TestCheckoutPhoneNumber

tests = [TestCheckoutPhoneNumber('test_tel')]
suite = unittest.TestSuite()
for test in tests:
    suite.addTest(test)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
