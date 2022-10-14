import graphene
from utils.lib import store_media
from user.DTOs import RegisterUserInput
from user.DTOs import UserInput
from user.models import User
from user.services import UserService
from account.services import AccountService
from user.serializers import UserType
from graphene_file_upload.scalars import Upload

user_service = UserService()
account_service = AccountService()



class UserQuery(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return user_service.all_users()


class UploadFile(graphene.Mutation):
    class Arguments:
        user_id = graphene.String(required=True)
        file = Upload(required=True)
    success = graphene.Boolean()
    def mutate(root, info, file=None, user_id=None):
        store_media(file)
        return UploadFile(success=True)


class RegisterUser(graphene.Mutation):
    class Arguments:
        register_data = RegisterUserInput(required=True)
    user = graphene.Field(UserType)
    success = graphene.Boolean()
    
    def mutate(root, info, register_data=None):
        user_instance = user_service.create_user(register_data)
        account_service.create_account(register_data, user_instance)
        return RegisterUser(success=True, user=user_instance)



class UserMutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    upload_file = UploadFile.Field()

