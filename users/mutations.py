import logging
import uuid

import stripe
from django.conf import settings
from django.db import transaction
from django.db.utils import IntegrityError
from graphene import Field, String, InputObjectType, Boolean
from graphene.relay import ClientIDMutation
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from .models import User
from .schema import UserNode
from csu.utils import update_object

logger = logging.getLogger(__name__)


class RegisterUserInputObject(InputObjectType):
    email = String(required=True)
    password = String(required=True)
    first_name = String(required=True)
    last_name = String(required=True)


class Register(ClientIDMutation):
    class Input:
        user = RegisterUserInputObject(required=True)

    user = Field(UserNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        try:
            input_user = input.get('user')
            user_email = input_user.get('email')

            if User.objects.filter(email=user_email).exists():
                msg = f"Unable to complete registration, User with email {user_email} already exists"
                logger.warning(msg)
                raise GraphQLError(msg)

            with transaction.atomic():
                user = User()
                user.set_password(input_user.pop('password'))
                update_object(user, input_user)

            msg = f"Successfully registered user with email {user_email}"
            logger.info(msg)

            return Register(user=user)
        except GraphQLError as e:
            raise e

        except Exception:
            msg = f"Failed to register user with email {user_email}"
            logger.error(msg)
            raise GraphQLError(msg)
