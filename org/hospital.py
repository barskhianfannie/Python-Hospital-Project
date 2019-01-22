"""
Hospital unit.
"""


class Hospital(object):
    """
    All aspects of the hospital.
    """

    def add_patient(self, patient_id, has_insurance, kind):
        """
        Add patient as inpatient or outpatient and return patient object.
            - patient_id: Patient ID as a string.
            - has_insurance: Boolean flag.
            - kind: One of "inpatient" or "outpatient" strings.
        """

    def patient_summary(self):
        """
        Show list of patients with their info (patient_id, has_insurance, and kind), along with
        total billing amount.
        """
