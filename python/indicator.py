title = "Light Indicator"
print(title.upper())
print()
light = input("Enter a light color (R for RED, Y for YELLOW and G for GREEN): ")
low_light = light.lower()
if low_light == "r" or low_light == "red":
    print("Danger! Stop!")
elif low_light == "y" or low_light == "yellow":
    print("Safe, No Danger")
elif low_light == "g" or low_light == "green":
    print("GO!")
else:
    print("I don't understand what you mean. Choose from the listed Colour:\nR for RED\nY for YELLOW\nG for GREEN")
    print("Run the program again with the right input.\nThanks!")
