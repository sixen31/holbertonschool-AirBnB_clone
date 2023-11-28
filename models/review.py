#!/usr/bin/python3
"""Review class module"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the Review class which inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
