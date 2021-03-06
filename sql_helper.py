import mysql.connector
from mysql.connector import errorcode
from time import sleep
import configparser


def run_create_sql():
	database_connector, cursor = connect_to_server()
	with open('create.sql', 'r') as c_file:
		commands = c_file.read()
	split_commands = commands.split(";")
	try:
		for command in split_commands:
			cursor.execute(command)
	except mysql.connector.Error as err:
			print(err)


def connect_to_server():
	try:
		database_connector = mysql.connector.connect(user='root', password="12345", host="127.0.0.1")
		cursor = database_connector.cursor()
		return database_connector, cursor
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("default")


def table_is_empty(string_name):
	database_connector, cursor = connect_to_server()
	cursor.execute("USE BloodDonationStorage")
	cursor.execute("SELECT * FROM {}".format(string_name))
	if len(cursor.fetchall()) == 0:
		print("File is empty!")
		sleep(2)
		return True


def id_in_table(string_name, user_input):
	database_connector, cursor = connect_to_server()
	cursor.execute("USE BloodDonationStorage")
	cursor.execute("SELECT ID_number FROM {}".format(string_name))
	pure_data = cursor.fetchall()
	ids = [id[0] for id in pure_data]
	return user_input in ids