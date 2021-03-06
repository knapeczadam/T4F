from datetime import timedelta
from datetime import datetime

PREPARATION_TIME = 30
DONATION_TIME = 30
AGAIN = "\nWrong input!"
ENTER = "\nPlease enter the"
CITIES = "Miskolc, Sarospatak, Szerencs, Kazincbarcika"


class Event:
	def __init__(self):
		self.event_id = None
		self.date_of_event = None
		self.start_time = None
		self.end_time = None
		self.zip_code = None
		self.city = None
		self.address = None
		self.available_beds = None
		self.planned_donors = None
		self.max_donor_number = None
		self.successful_donations = None

	def generate_event_id(self):
		"""

		:return:
		"""
		event_id = str(datetime.now().strftime("%Y%m%d%H%M%S"))[2:]
		self.event_id = event_id

	def get_date_of_event(self):
		"""

		:return:
		"""
		date_of_event = input("{} event date in the following format, 1999.12.31: ".format(ENTER))
		while Event.is_valid_date(date_of_event) is False:
			date_of_event = input("{}{} event date in the given format, 1999.12.31: ".format(AGAIN, ENTER))
		self.date_of_event = date_of_event

	@staticmethod
	def is_valid_date(date_of_event):
		"""

		:param date_of_event:
		:return:
		"""
		try:
			datetime.strptime(date_of_event, "%Y.%m.%d")
			return True
		except:
			return False

	def get_start_time(self):
		"""

		:return:
		"""
		start_time = input("{} start time of the donation event in the following format, 09:30: ".format(ENTER))
		while Event.is_valid_start_time(start_time) is False:
			start_time = input("{}{} start time of the donation event in the given format, 09:30: ".format(AGAIN, ENTER))
		self.start_time = start_time

	@staticmethod
	def is_valid_start_time(start_time):
		"""

		:param start_time:
		:return:
		"""
		try:
			datetime.strptime(start_time, "%H:%M")
			return True
		except:
			return False

	def get_end_time(self):
		"""

		:return:
		"""
		end_time = input("{} end time of the donation event in the following format, 15:30: ".format(ENTER))
		while self.is_valid_end_time(end_time) is False:
			end_time = input("{}{} end time of the donation event in the given format, 15:30: ".format(AGAIN, ENTER))
		self.end_time = end_time

	@staticmethod
	def is_valid_end_time(end_time):
		"""
		:param end_time:
		:return:
		"""
		try:
			datetime.strptime(end_time, "%H:%M")
			return True
		except:
			return False

	def get_zip_code(self):
		"""

		:return:
		"""
		zip_code = input("{} ZIP code for the address of the event in the following format, 1234: ".format(ENTER))
		while Event.is_valid_zip_code(zip_code) is False:
			zip_code = input("{} The ZIP code has to be 4 digits long and can not start with a zero.\
			{} ZIP code for the address of the event in the following format, 1234: ".format(AGAIN, ENTER))
		self.zip_code = zip_code

	@staticmethod
	def is_valid_zip_code(zip_code):
		"""

		:param zip_code:
		:return:
		"""
		return zip_code.isdigit() and len(zip_code) == 4 and zip_code[0] != "0"

	def get_city(self):
		"""

		:return:
		"""
		city = input("\nPlease type in where the event will take place. {}: ".format(CITIES))
		while Event.is_valid_city(city) is False:
			city = input("{} You can only choose from the given cities.\
			\nPlease type in one of the following cities. {}: ".format(AGAIN, CITIES))
		self.city = city

	@staticmethod
	def is_valid_city(city):
		return city.lower() in CITIES.lower()

	def get_address(self):
		"""

		:return:
		"""
		address = input("\nPlease enter in what address the event will take place: ")
		while Event.is_valid_address(address) is False:
			address = input("{} The address has to be at least 1 and at most 25 characters long.\
			\nPlease enter in what address the event will take place: ".format(AGAIN))
		self.address = address

	@staticmethod
	def is_valid_address(address):
		"""

		:param address:
		:return:
		"""
		return 0 < len(address) <= 25

	def get_available_beds(self):
		"""

		:return:
		"""
		available_beds = input("{} number of available beds: ".format(ENTER))
		while Event.is_valid_available_beds(available_beds) is False:
			available_beds = input("{} The available beds have to be a positive number.\
			\n{} number of available beds: ".format(AGAIN, ENTER))
		self.available_beds = available_beds

	@staticmethod
	def is_valid_available_beds(beds):
		"""

		:param beds:
		:return:
		"""
		return beds.isdigit() and int(beds) > 0

	def calc_max_donor_number(self):
		"""

		:return:
		"""
		event_duration_in_minutes = datetime.strptime(str(self.end_time), "%H:%M") - datetime.strptime(str(self.start_time), "%H:%M")
		event_duration_in_minutes = timedelta.total_seconds(event_duration_in_minutes) // 60
		max_donor_number = ((event_duration_in_minutes - PREPARATION_TIME) // DONATION_TIME) * int(self.available_beds)
		self.max_donor_number = int(max_donor_number)

	def get_planned_donor_number(self):
		"""

		:return:
		"""
		planned_donors = input("{} planned donor number: ".format(ENTER))
		while self.is_valid_planned_donor_number(planned_donors) is False:
			planned_donors = input("{} The planned donor number has to a positive number,\
			\nand not bigger than the maximum donor number, which is {}.{} planned donor number: "\
			.format(AGAIN, int(self.max_donor_number), ENTER))
		self.planned_donors = planned_donors

	def is_valid_planned_donor_number(self, planned_donors):
		"""

		:param planned_donors:
		:return:
		"""
		return planned_donors.isdigit() and int(planned_donors) <= self.max_donor_number

	def get_successful_donations(self):
		"""

		:return:
		"""
		successful_donations = input("\nPlease enter how many successful donations were during the event: ")
		while self.is_valid_successful_donations(successful_donations) is False:
			successful_donations = input("{} The successful donations has to be a positive number,\
			\nnot bigger than the maximum donor number, which is {}. Please enter again: "\
			.format(AGAIN, int(self.max_donor_number)))
		self.successful_donations = successful_donations

	def is_valid_successful_donations(self, successful_donations):
		"""

		:param successful_donations:
		:return:
		"""
		return successful_donations.isdigit() and int(successful_donations) <= self.max_donor_number
