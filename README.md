# Hospital

The Pasadena Community Hospital is updating their patient management system and hired you to write the initial version of the software. Below are the requirements they want you to follow:

* The hospital has a 100 bed facility and a clinic and accepts both inpatients and outpatients, each with their own set of procedures and pricing structures. Most procedures, but not all, are covered by insurance.
* If a procedure is covered by insurance and the patient has insurance, he is liable for the deductible part of the cost (less any discounts); otherwise, he has to pay the full amount (less discounts).
* When a patient visits the hospital, he is first added to the hospital system with his patient id and insurance info, as an inpatient or outpatient.
* As the patient goes through different procedures, each procedure is added to the patient record.
* Occasionally however, an invalid procedure (one that is not avaiable in the hospital or for the patient kind of inpatient or outpatient) gets entered, and such events need to be handled as exceptions and logged.
* To help patients control costs, the hospital offers a 20% discount if the patient undergoes 3 or more procedures. Also, the clinic currently has a $100-off promotion for Botox procedures.
* Insurance companies are offering their own promotion waiving 50% of the deductibles for angioplasty and stent procedures for inpatients if they have also had an ultrasound. They are also waiving 30% of the deductibles on all procedures for outpatients.
* Periodically, the billing department needs to generate patient summary reports showing the patient id, insurance info, inpatient/outpatiend kind, total billed amount, and the patient liability.

To test whether the software is running correctly, the hospital asked you to create unit tests and an integration test that adds patients and their procedures and then generates a patient summary report. For this, you are asked to use their test data for 100 patients, which you can get by calling patients(100).