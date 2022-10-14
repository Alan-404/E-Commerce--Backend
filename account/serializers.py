from account.models import Account
from graphene_django import DjangoObjectType


class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        fields = "__all__"