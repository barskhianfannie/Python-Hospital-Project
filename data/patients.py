"""
Patient data.
"""
import random
from data import PROCEDURES


PROCEDURE_NAMES = set(PROCEDURES["inpatient"]) | set(PROCEDURES["outpatient"])


def patients(count):
    """
    Generate patients.
    """
    for _ in range(count):
        yield {
            "patient_id": random.randint(100000, 999999),
            "has_insurance": random.random() > 0.3,
            "kind": "inpatient" if random.random() > 0.7 else "outpatient",
            "procedures": (pn for pn in PROCEDURE_NAMES if random.random() > 0.5)
        }
