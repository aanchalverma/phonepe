
"""
Covid tracker app:
- Registers a new user/admin
- Return the Covid risk for each user based on assessment
- Update covid results of patients(Admin)
- Mark Zone as safe, unsafe
"""
from Admin.admin_registration import AdminRegistration
from Users.register_user import User

def user_registration(name, phone, pin):
    new_user = User(name, phone, pin)
    is_user_created = new_user.register_user()
    if is_user_created:
        print(f'{new_user.username} has been successfully registered')
    else:
        print(f'Error occurred while users registeration')
    return new_user


# Register a new user
user = user_registration("Bob", "9107654897", "431213")
import pdb
pdb.set_trace()
# self assessment
if user:
    user.user_self_assessment(["fever"], "True", "False")

# Register Admin
admin = AdminRegistration("Paul", "9107564897", "431673")

# Update covid result
admin.update_covid_result('Bob', 'positive')
