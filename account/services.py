from account.models import Account
from django.contrib.auth.hashers import make_password, check_password
from utils.lib import create_id
class AccountService:
    def create_account(self, account_data, user):
        account_instance = Account()
        for key in account_data.__dict__.keys():
            insert_value = account_data.__dict__[key]
            if key != "password":
                account_instance.__dict__[key] = insert_value
            else:
                account_instance.__dict__[key] = make_password(insert_value)
        account_instance.user = user
        account_instance.id = create_id()
        account_instance.save()
        return account_instance

    def get_account_by_user(self, user):
        return Account.objects.get(user=user)

    def confirm_password(self, account, password):
        return check_password(password, account.password)
