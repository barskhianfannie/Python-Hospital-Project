"""
Patient object.
"""

from data import PROCEDURES 

procedure_list = []
not_covered = []
liability = 0
total_billing = 0


class Patient(object):
    """
    Base patient class.
    """
    

    def __init__(self, patient_id, has_insurance, kind):
        self.patient_id = patient_id
        self.has_insurance = has_insurance
        self.kind = kind
        self.procedure_list = []
        self.liability = 0
        self.total_billing = 0
        
    @staticmethod
    def get_patient(patient_id, has_insurance, kind):
        if kind is "inpatient":
           return _InPatient(patient_id, has_insurance, kind)  
        else:
            return _OutPatient(patient_id, has_insurance, kind)

   

    def add_procedure(self, procedure):
        """
        Add procedure to patient.
            - procedure: Procedure ID.
        """
        self.procedure_list.append(procedure)
        
        return self.procedure_list
        

    def summary(self):
        """
        Populawith common  info.
        """
        if "botox" in self.procedure_list:
            self.liability -=100
        if len(self.procedure_list) >=3:
            self.liability -= self.liability * 0.2
            
        return (self.patient_id, self.has_insurance, self.kind)
     
class _InPatient(Patient):
    """
    Inpatient.
    """
    def __init__(self, patient_id, has_insurance, kind):
        super().__init__(patient_id, has_insurance, kind)
        self.liability = liability
        self.total_billing = total_billing
       

    def summary(self):
        super().summary()
        for procedure in self.procedure_list:
            if self.has_insurance:
                if procedure is "botox":
                    self.total_billing += PROCEDURES[self.kind]["botox"]["cost"]
                    self.liability += PROCEDURES[self.kind]["botox"]["cost"] -100
                elif procedure is "ekg":
                    self.total_billing += PROCEDURES["outpatient"]["ekg"]["cost"]
                    self.liability += PROCEDURES["outpatient"]["ekg"]["cost"]
                elif procedure is "checkup":
                    self.total_billing += PROCEDURES["outpatient"]["checkup"]["cost"]
                    self.liability += PROCEDURES["outpatient"]["checkup"]["copay"]
                else:
                    self.total_billing += PROCEDURES[self.kind][procedure]["cost"]
                    self.liability += PROCEDURES[self.kind][procedure]["copay"]
            else:
                if procedure is "botox":
                    self.total_billing += PROCEDURES[self.kind]["botox"]["cost"]
                    self.liability += PROCEDURES[self.kind]["botox"]["cost"] -100
                elif procedure is "ekg":
                    self.total_billing += PROCEDURES["outpatient"]["ekg"]["cost"]
                    self.liability += PROCEDURES["outpatient"]["ekg"]["cost"]
                elif procedure is "checkup":
                    self.total_billing += PROCEDURES["outpatient"]["checkup"]["cost"]
                    self.liability += PROCEDURES["outpatient"]["checkup"]["cost"]
                else:
                    self.total_billing += PROCEDURES[self.kind][procedure]["cost"]
                    self.liability += PROCEDURES[self.kind][procedure]["cost"]


        if ("ultrasound" and "angioplasty") in self.procedure_list:
            self.liability -= 500.0
        if ("ultrasound" and "stent") in self.procedure_list:
                self.liability -= 250.0
                
        
        return self.patient_id, self.has_insurance, self.kind, self.total_billing, self.liability
       

class _OutPatient(Patient):
    """
    Outpatient.
    """
    def __init__(self, patient_id, has_insurance, kind ):
        super().__init__(patient_id, has_insurance, kind)
        self.total_billing = total_billing
        self.liability = liability

    def summary(self):
        super().summary()
        for procedure in self.procedure_list:
            if self.has_insurance:
                if procedure is "botox":
                    self.total_billing += PROCEDURES["inpatient"]["botox"]["cost"]
                    self.liability += PROCEDURES["inpatient"]["botox"]["cost"] - 100
                elif procedure is "ekg":
                    self.total_billing += PROCEDURES[self.kind]["ekg"]["cost"]
                    self.liability += PROCEDURES[self.kind]["ekg"]["cost"]
                elif procedure is "stent":
                    self.total_billing += PROCEDURES["inpatient"]["stent"]["cost"]
                    self.liability += PROCEDURES["inpatient"]["stent"]["copay"]
                elif procedure is "angioplasty":
                    self.total_billing += PROCEDURES["inpatient"]["angioplasty"]["cost"]
                    self.liability += PROCEDURES["inpatient"]["angioplasty"]["copay"]
                else:
                    self.total_billing += PROCEDURES[self.kind][procedure]["cost"]
                    self.liability += PROCEDURES[self.kind][procedure]["copay"] - (PROCEDURES[self.kind][procedure]["copay"]* .3)
            else:
                if procedure is "botox":
                    self.total_billing += PROCEDURES["inpatient"]["botox"]["cost"]
                    self.liability += PROCEDURES["inpatient"]["botox"]["cost"] - 100
                elif procedure is "ekg":
                    self.total_billing += PROCEDURES[self.kind]["ekg"]["cost"]
                    self.liability += PROCEDURES[self.kind]["ekg"]["cost"]
                elif procedure is "stent":
                    self.total_billing += PROCEDURES["inpatient"]["stent"]["cost"]
                    self.liability += PROCEDURES["inpatient"]["stent"]["cost"]
                elif procedure is "angioplasty":
                    self.total_billing += PROCEDURES["inpatient"]["angioplasty"]["cost"]
                    self.liability += PROCEDURES["inpatient"]["angioplasty"]["cost"]
                else:
                    self.total_billing += PROCEDURES[self.kind][procedure]["cost"]
                    self.liability += PROCEDURES[self.kind][procedure]["cost"] 

        
        return self.patient_id, self.has_insurance, self.kind, self.total_billing, self.liability