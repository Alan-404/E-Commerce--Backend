import graphene
from user.schema import UserQuery, UserMutation
from account.schema import AccountMutation

class Query(UserQuery):
    pass


class Mutation(UserMutation, AccountMutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)