"""
Unit tests for hospital module.
"""
import unittest
from org.hospital import Hospital
from org.patient import Patient
from data.patients import patients


class TestHospital(unittest.TestCase):
    """
    Tests for hospital.
    """
    hospital = Hospital()

    def test_add_patient(self):
        """
        Make sure hospital adds the right kind of patient.
        """
        hospital = Hospital()

        for patient in patients(100): 
            self.added_patient = hospital.add_patient(patient["patient_id"], patient["has_insurance"], patient["kind"])
            if patient["kind"] is "outpatient":
                self.assertEqual(patient["kind"], hospital.add_patient("56398", "true", "outpatient"))

    def test_patient_summary(self):
        """
        Confirm that the summary returns info on all patients.
        """
        hospital = Hospital()
        for patient in patients(100):
            added_patient = hospital.add_patient(patient["patient_id"], patient["has_insurance"], patient["kind"])
            for procedure in patient["procedures"]:
                self.added_patient = hospital.add_patient(patient["patient_id"], patient["has_insurance"], patient["kind"])
                info_list = added_patient.summary()
                self.assertAlmostEquals(info_list, patient["patient_id"])



if __name__ == "__main__":
    unittest.main()
