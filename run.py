"""
Hospital flow.
"""


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


if __name__ == "__main__":
    Run().flow()
