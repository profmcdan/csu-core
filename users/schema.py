import graphene
import logging
from django.conf import settings
from graphene import String, relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from .models import User

logger = logging.getLogger(__name__)


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'email': ['exact', 'icontains', 'istartswith'],
            'first_name': ['exact', 'icontains', 'istartswith'],
            'last_name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

    @classmethod
    @login_required
    def get_node(cls, info, id):
        current_user = info.context.user

        if str(current_user.id) != id:
            msg = "You do not have permission to perform this action"
            logger.warning(msg)
            raise GraphQLError(msg)

        return current_user

    @classmethod
    def resolve_password(cls, root, info, **kwargs):
        msg = "Cannot retrieve password. Action is forbidden."
        logger.warning(msg)

        raise GraphQLError(msg)


class Query(object):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    @staticmethod
    @login_required
    def resolve_user(root, info):
        return User.objects.get(id=info.context.user.id)

    def resolve_all_users(root, info):
        return User.objects.all()
