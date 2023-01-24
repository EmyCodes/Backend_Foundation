import sys

try:
	f = open("people.txt")
	s = f.readline()
	i = int(s.strip())
except OSError as err:
	print("OSError: ".format(err))
except ValueError:
	print("Could not convert value to an integer")
except Exception as err:
	print(f"Unexpected {err=}, {type(err)=}")
	raise
