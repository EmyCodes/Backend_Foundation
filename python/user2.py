import datetime as dt

firstName = input("What is out first name? ")
lastName = input("What's your surname? ")
middleName = input("What's middle name? (Optional) ")
firstName = firstName.capitalize()
lastName = lastName.capitalize()
middleName = middleName.capitalize()
now = dt.date.today()  # dt.datetime.now() cn also be used to get today's date from computer internal clock


def username(**kwargs):  # Practice function
    """Docstring here"""
    print("\n Last Logged in at {}\n".format(now))
    if len(middleName) > 0:
        print("Hey {} {} {}!".format(firstName, lastName, middleName))
    else:
        print("Hey {} {}!".format(firstName, lastName))
