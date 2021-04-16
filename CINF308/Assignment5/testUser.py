import TimeType


def main():
	time_obj = TimeType.TimeType()
	print(time_obj)

	print("Change hours to 27")
	if time_obj.set_hours(27) == True:
		print("Hours was changed")
	else:
		print("Hours was NOT changed")
	print(time_obj)

	print("Change hours to 18")
	if time_obj.set_hours(5) == True:
		print("Hours was changed")
	else:
		print("Hours was NOT changed")
	print(time_obj)

	print("Change minutes to 456")
	if time_obj.set_minutes(456) == True:
		print("Minutes was changed")
	else:
		print("Minutes was NOT changed")
	print(time_obj)

	print("Change minutes to 35")
	if time_obj.set_minutes(37) == True:
		print("Minutes was changed")
	else:
		print("Minutes was NOT changed")
	print(time_obj)

	print("Change seconds to 529")
	if time_obj.set_seconds(529) == True:
		print("Seconds was changed")
	else:
		print("Seconds was NOT changed")
	print(time_obj)

	print("Change seconds to 29")
	if time_obj.set_seconds(36) == True:
		print("Seconds was changed")
	else:
		print("Seconds was NOT changed")
	print(time_obj)

	print("Increase seconds")
	time_obj.increase_second()
	print(time_obj)

	print("Decrease seconds")
	time_obj.decrease_second()
	print(time_obj)


	print("The hour is", time_obj.get_hours())
	print("The minute is", time_obj.get_minutes())
	print("The second is", time_obj.get_seconds())

main()
