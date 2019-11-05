import base64
import datetime
import decimal
import time
from calendar import mdays
from datetime import datetime, timedelta

import pytz
import sendgrid

from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from graphene.types import Scalar
from graphql.language import ast
from graphql_jwt.exceptions import PermissionDenied
from inflection import underscore
from sendgrid.helpers.mail import Mail, Email


def auth_resolver(attname, default_value, root, info, **args):
    if info.context.user.is_authenticated:
        return getattr(root, attname, default_value)
    raise PermissionDenied()


def update_object(object, data):
    for key, value in data.items():
        if key is not 'id' and value is not None:
            setattr(object, key, value)
    object.save()

    return object


def remove_query_kwargs(kwargs):
    keys_to_remove = ['before', 'after', 'first', 'last']

    return {k: v for k, v in kwargs.items() if k not in keys_to_remove}


def convert_order_by(order_by):
    if order_by is None:
        return order_by

    if order_by[0] == '-':
        return "-%s" % underscore(order_by[1:])
    return underscore(order_by)


def send_email(to_email, template_data, template_id, attachments=None):
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

    from_email = Email(name='CSU-FUTA', email=EMAIL_HOST_USER)

    message = Mail(
        from_email=from_email,
        to_emails=to_email,
    )

    message.dynamic_template_data = template_data
    message.template_id = template_id

    if attachments:
        for attachment in attachments:
            message.add_attachment(attachment)

    sg.send(message)
