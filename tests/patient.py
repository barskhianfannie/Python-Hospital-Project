"""
Unit tests for patient module.
"""
import unittest
from org.hospital import Hospital
from org.patient import Patient
from data.__init__ import PROCEDURES


class TestPatient(unittest.TestCase):
    """
    Tests for patient.
    """

    def test_add_procedure(self):
        """
        Check procedure addition.
        """

        for procedure in PROCEDURES["intpatient"]:
            self.assertAlmostEquals(procedure, Patient.add_procedure)

    def test_summary(self):
        """
        Check that the summary calculates correctly and handles promotions.
        """
        test_botox_price = Patient.summary("botox")
        self.assertEqual(test_botox_price, 1900)



if __name__ == "__main__":
    unittest.main()
