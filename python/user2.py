import datetime as dt

firstName = input("What is out first name? ")
lastName = input("What's your surname? ")
middleName = input("What's middle name? (Optional) ")
firstName = firstName.capitalize()
lastName = lastName.capitalize()
middleName = middleName.capitalize()
now = dt.date.today()  # dt.datetime.now() cn also be used to get today's date from computer internal clock


def username(fname=firstName, surname=lastName, last_logged=now, midname=middleName):  # Practice function
    """Docstring here"""
    print("\n Last Logged in at {}\n".format(last_logged))
    if len(midname) > 0:
        print("Hey {} {} {}!".format(fname, surname, midname))
    else:
        print("Hey {} {}!".format(fname, surname))


username()
