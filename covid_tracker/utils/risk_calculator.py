"""
This module will help in calculating user's covid-19 risk
"""
class RiskCalculator():
    def __init__(self):
        self.risk = None
        self.symptoms = ['fever', 'cold', 'cough']

    def risk_calculator(self, symptoms, travel_history, contact_with_patient):
        """
        :param symptoms:
        :param travel_history:
        :param contact_with_patient:
        :return:
        """
        # Edge cases
        if travel_history is None or contact_with_patient is None:
            print(f'Please enter the travel history and other details')
        try:
            if not any(symptoms) and not travel_history and not contact_with_patient:
                return 5
            elif symptoms in any(self.symptoms) and travel_history or contact_with_patient:
                return 50
            elif len(symptoms) == 2 and symptoms in self.symptoms and travel_history or contact_with_patient:
                return 75
            elif len(symptoms) > 2 and symptoms in self.symptoms and travel_history or contact_with_patient:
                return 95
        except Exception as exc:
            raise ValueError
            print(f'Exception occured {exc} while calculating risks')

