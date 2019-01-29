"""
Hospital unit.
"""
from data import patients
from org.patient import Patient


patient_list = []
class Hospital(object):
    
    """
    All aspects of the hospital.
    """
    
    # def __init__(self):
    #     self.patient_list = []

    def add_patient(self, patient_id, has_insurance, kind):
        """
        Add patient as inpatient or outpatient and return patient object.
            - patient_id: Patient ID as a string.
            - has_insurance: Boolean flag.
            - kind: One of "inpatient" or "outpatient" strings.
        """
       
        patient_info = Patient.get_patient(patient_id, has_insurance, kind)
        patient_list.append(patient_info) 

        return  patient_info
        
    def patient_summary(self):
        """
        Show list of patients with their info (patient_id, has_insurance, and kind), along with
        total billing amount.
        """
        
        return [patient.summary() for patient in patient_list]
        
