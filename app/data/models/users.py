from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator

from app.core.session import session

constants = session.constants


class Users(models.Model):
    id = fields.IntField(pk=True)
    ensname = fields.CharField(max_length=constants.lengths["strings"][0], null=False, unique=True)
    password_hash = fields.CharField(max_length=constants.lengths["strings"][1], null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class PydanticMeta:
        exclude = ["password_hash"]


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
