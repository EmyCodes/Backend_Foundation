import datetime as dt

name = input("What is your name: ")
now = dt.datetime.now()
if now.hour < 12:
    print(f"Good Morning, {name}!")
    print("How was your night rest?")
elif 12 <= now.hour < 18:
    print(f"Good Afternoon, {name}!")
    print("How is our day going?")
else:
    print(f"Good Evening, {name}!")
    print("How was your day? I trust it was good and fine. Smiles!")
print("I, your computer, wait for your instruction(s)!")
