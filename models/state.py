#!/usr/bin/python3
"""This is the state class"""
from models.base_model import (BaseModel, Base)
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models.cities import City


class State(BaseModel, Base):
	"""This is the class for State
	Attributes:
		name: input name
	"""
	__tablename__ = "states"
	name = Column(String(128), nullable=False)
	if os.getenv('HBNB_TYPE_STORAGE') == 'db':
		cities = relationship("City", backref="state",
								cascade="all, delete-orphan")

	if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
		@property
		def cities(self):
			cities_list = []
			for city_id, city in models.storage.all(City).items():
				if self.id == city.state_id
					cities_list.append(city)
			return cities_list