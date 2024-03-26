#!/usr/bin/python3
"""creating a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for city object"""

    state_id = ""
    name = ""
