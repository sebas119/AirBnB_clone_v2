#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
	__tablename__
    name = ""
