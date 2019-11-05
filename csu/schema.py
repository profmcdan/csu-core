import logging

import graphene
import graphql_jwt
from graphene import Field
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required

from users.models import User
from users.schema import Query as UserQuery
from users.mutations import Register


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    register = Register.Field()


class Query(UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
