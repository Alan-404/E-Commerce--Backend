import graphene
from graphene_file_upload.scalars import Upload

# Input DTO
class UserInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    bdate = graphene.Date()
    gender = graphene.String()
    address = graphene.String()

class RegisterUserInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    bdate = graphene.Date()
    gender = graphene.String()
    address = graphene.String()
    password = graphene.String()
    role = graphene.Boolean()
    avatar = Upload()


