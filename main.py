import os
import datetime


def get_current_date():
	"""
	Function Get the current date. Returns a string with date
	:return:
	"""
	time_count = datetime.datetime.now()
	tc = time_count.timetuple()
	date_tc = tc[:3]
	return str(date_tc)


def insert_date_in_file(date_tc):
	"""
	The function writes the current date to a file
	:param date_tc:
	:return:
	"""
	with open('date_list.txt', 'a+', encoding='utf-8') as date_list:
		date_list.writelines(date_tc)


def get_date():
	"""
	The function gets a list of dates from a file
	:return:
	"""
	with open('date_list.txt', 'r', encoding='utf-8') as date_list:
		dl = date_list.readlines()
		print(dl)
	return dl


def main_prog():
	"""
	The main program code. Checks the date, if it is in the list, immediately turns off the computer.
	If absent, turns on the timer in seconds.
	:return:
	"""
	current_date = str(get_current_date())
	last_date_in_file = get_date()
	print(current_date)
	print(get_date())
	print(current_date, last_date_in_file)
	print(str(current_date) in last_date_in_file)

	if current_date in last_date_in_file:
		os.system("shutdown -p -f")
	else:
		insert_date_in_file(current_date)
		os.system("shutdown -s -t 7200")


if __name__ == '__main__':
	if os.path.exists("date_list.txt"):
		main_prog()
	else:
		with open('date_list.txt', 'w', encoding='utf-8'):
			main_prog()
