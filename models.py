import datetime
from peewee import *

DATABASE = SqliteDatabase("locations.db")


class LocationData(Model):
	description = CharField(unique=True, max_length = 120)
	latitude = CharField(unique=True)
	longitude = CharField(unique=True)
	registered = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE
		order_by = ("-registered",) #newest locations at the top

	@classmethod
	def add_location(cls, description, latitude, longitude):
		try:
			with DATABASE.transaction():
				cls.create(
					description=description,
					latitude=latitude,
					longitude=longitude)

		except IntegrityError:
			raise ValueError("Location already exists")


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([LocationData], safe=True)
	DATABASE.close()