"""
Hospital flow.
Fannie Barskhian. 2019
"""
from data.patients import patients
from org.hospital import Hospital
from org.patient import Patient
import random 

class Run(object):
    """
    Run the hospital flow.
    """

    def flow(self):
        """
        Run the patients through the system:
            * Get data for all 100 patients.
            * Add them to hospital to get patient objects.
            * Add procedures to the patient object.
            * Generate and print hospital patient summary.
        """
    hospital = Hospital()
    #Print format for Item Desciptions at top of list.
    print("%-5s%-10s%10s%15s%18s%18s" %("#", "ID:", "Ins:", 
                "INP / OUTP:", "Total:", "Liability:"))
                
    n = 1
    #Generating through 100 Patient Profiles to add to hospital. 
    for patient in patients(100): 
        added_patient = hospital.add_patient(patient["patient_id"], patient["has_insurance"], patient["kind"])
        for procedure in patient["procedures"]: 
            added_patient.add_procedure(procedure)
            info_list = added_patient.summary()
        print("%-5d%-10d%10s%15s%18.2f%18.2f" %(n, info_list[0], info_list[1], 
                info_list[2], info_list[3], info_list[4]))
        n+=1
        
            
            
            

if __name__ == "__main__":
    Run().flow()
