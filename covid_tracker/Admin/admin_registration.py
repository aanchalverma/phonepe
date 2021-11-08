"""
Admin
"""
from Users.register_user import User


class AdminRegistration(User):
    """
    Admin functionalities
    """
    def __init__(self, username=None, user_mobile=None, user_pin=None):
        super().__init__()

    def update_covid_result(self, username, result):
        """
        Update covid result of a patient
        :return:
        """
        if username in self.map_user_pincode.values():
            username.is_covid_positive = result
        else:
            print(f'User not found')
