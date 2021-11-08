"""
This module will register new user based on their name, mobile number and pincode
"""
import json
import requests

from utils.risk_calculator import RiskCalculator

users = set()

class User(object):
    """
    This class defines User's operations and properties
    """
    def __init__(self, username=None, user_mobile_no=None, user_pincode=None):
        """
        Defining user object
        :param username:
        :param user_mobile_no:
        :param user_pincode:
        :return None
        """
        self.username = username
        self.user_mobile_no = user_mobile_no
        self.user_pincode = user_pincode
        self.map_user_pincode = {} # {'45123': [username1, ]}
        self.is_covid_positive = False

    def register_user(self):
        """
        Registeration of a new user :
        - Create a new user
        - Upon success, return 200 else 400
        :return: StatusCode(int)
        """
        users_credentials = json.dumps(self.__dict__)
        # users.append()
        if not self.map_user_pincode:
            self.map_user_pincode[self.user_pincode] = [self.username]
        else:
            self.map_user_pincode[self.user_pincode].append(self.username)
        if len(self.user_pincode)<6:
            print(f'Error : Failed to register, please enter the right pincode')
            return None
        # TODO: check the connection error
        # requests.post('https://localhost:8800/api/users', data=users_credentials)
        # TODO: Update the count
        return self.username

    def user_self_assessment(self, symptoms, travel_history, contact_with_patient):
        """
        Calculate risk on the basis of user's self assessment
        :param symptoms:
        :param travel_history:
        :param contact_with_patient:
        :return: None
        """
        risk = RiskCalculator()
        risk_involved = risk.risk_calculator(symptoms, travel_history, contact_with_patient)

        if risk_involved == 5:
            print(f'Percentage of risk involved with user is {risk_involved} %')

        if risk_involved == 50:
            print(f'Percentage of risk involved with user is {risk_involved} %')

        if risk_involved == 75:
            print(f'Percentage of risk involved with user is {risk_involved} %')

        if risk_involved == 95:
            print(f'Percentage of risk involved with user is {risk_involved} %')
