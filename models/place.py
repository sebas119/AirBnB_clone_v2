#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.amenities import Amenity


place_amenity = Table('place_amenity', Base.metadata,
						Column('place_id', primary_key=True, String(60), ForeignKey('places.id'), nullable=False),
						Column('amenity_id', primary_key=True, String(60), ForeignKey('places.id'), nullable=False)
						)

class Place(BaseModel, Base):
	"""This is the class for Place
	Attributes:
		city_id: city id
		user_id: user id
		name: name input
		description: string of description
		number_rooms: number of room in int
		number_bathrooms: number of bathrooms in int
		max_guest: maximum guest in int
		price_by_night:: pice for a staying in int
		latitude: latitude in flaot
		longitude: longitude in float
		amenity_ids: list of Amenity ids
	"""
	__tablename__ = 'places'
	city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
	user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
	name = Column(String(128), nullable=False)
	description = Column(String(1024), nullable=True)
	number_rooms = Column(Integer, default=0, nullable=False)
	number_bathrooms = Column(Integer, default=0, nullable=False)
	max_guest = Column(Integer, default=0, nullable=False)
	price_by_night = Column(Integer, default=0, nullable=False)
	latitude = Column(Float, nullable=True)
	longitude = Column(Float, nullable=True)
	amenity_ids = []
	reviews = relationship('Review', backref="place",
								cascade="all, delete-orphan")

	if os.getenv('HBNB_TYPE_STORAGE') == 'db':
		amenities = relationship("Amenity", secondary="place_amenity",
									viewonly=False)
		@property
		def reviews(self):
			revs = []
			for rev in self.reviews:
				if rev.place_id == self.id:
					revs.append(rev)
			return revs


	elif os.getenv('HBNB_TYPE_STORAGE') == 'file':
		@property
		def amenities(self):
			amenities_list = []
			for amen in amenity_ids:
				if amen.id == self.id
					amenities_list.append(amen)
			return amenities_list

		@amenities.setter
		def amenities(self, amen):
			if amen.__class__.__name__ == 'Amenity':
				self.amenity_ids.append(amen)
