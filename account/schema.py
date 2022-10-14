import graphene
from account.DTOs import LoginAccountInput
from user.services import UserService
from account.services import AccountService
from utils.middleware import MiddleWare

user_service = UserService()
account_service = AccountService()
middleware = MiddleWare()

class LoginAccount(graphene.Mutation):
    class Arguments:
        login_data = LoginAccountInput(required=True)
    
    # Output DTO
    success = graphene.Boolean()
    access_token = graphene.String()

    def mutate(root, info, login_data=None):
        user = user_service.get_user_by_email(login_data.email)
        if user is None:
            return LoginAccount(success=False, access_token=None)
        account = account_service.get_account_by_user(user)
        if account is None:
            return LoginAccount(success=False, access_token=None)
        confirmed_password = account_service.confirm_password(account, login_data.password)
        if confirmed_password == False:
            return LoginAccount(success=False, access_token=None)
        print("OK")
        token = middleware.generate_token(account.id)
        return LoginAccount(success=True, access_token=token)


class AccountMutation(graphene.ObjectType):
    login_account = LoginAccount.Field()
    