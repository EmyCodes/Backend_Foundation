try:
	raise Exception("spam", "eggs")
except Exception as inst:
	print(type(inst))
	print(inst.args)
	print(inst)

	x, y = inst.args
	print("x = {}".format(x))
	print("y = {}".format(y))
