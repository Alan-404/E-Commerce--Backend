import graphene
from graphene_file_upload.scalars import Upload

class LoginAccountInput(graphene.InputObjectType):
    email = graphene.String()
    password = graphene.String()
    avatar = Upload()