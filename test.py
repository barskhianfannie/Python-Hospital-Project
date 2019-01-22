"""
All unit tests.
"""
import unittest
import tests


MDOULES = [
    tests.hospital
]


class Test(unittest.TestCase):
    """
    Run all tests.
    """
    for module in MDOULES:
        suite = unittest.TestLoader().loadTestsFromModule(module)
        unittest.TextTestRunner(verbosity=2).run(suite)
