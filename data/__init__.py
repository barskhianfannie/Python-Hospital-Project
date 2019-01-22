"""
Hospital data.
"""


PROCEDURES = {
    "inpatient": {
        "angioplasty": {
            "cost": 8000,
            "insurance": True,
            "copay": 1000
        },
        "botox": {
            "cost": 2000,
            "insurance": False
        },
        "endoscopy": {
            "cost": 5000,
            "insurance": True,
            "copay": 500
        },
        "stent": {
            "cost": 15000,
            "insurance": True,
            "copay": 500
        },
        "ultrasound": {
            "cost": 2000,
            "insurance": True,
            "copay": 100
        }
    },
    "outpatient": {
        "checkup": {
            "cost": 200,
            "insurance": True,
            "copay": 10
        },
        "ekg": {
            "cost": 500,
            "insurance": False
        },
        "endoscopy": {
            "cost": 5000,
            "insurance": True,
            "copay": 500
        },
        "ultrasound": {
            "cost": 1500,
            "insurance": True,
            "copay": 100
        }
    }
}
