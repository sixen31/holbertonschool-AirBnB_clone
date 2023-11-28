#!/usr/bin/python3
"""User class module"""


from models.base_model import BaseModel


class User(BaseModel):
    """Defines the User class which inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
