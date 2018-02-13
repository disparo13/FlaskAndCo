def who_do_you_know():
    known_people = input("Enter the people you know: ").strip().split(',')
    return known_people


def ask_user():
    person = input("Enter the name: ")
    if person in known:
        print("You know {}!".format(person))
    else:
        print("You don't know {}!".format(person))

known = who_do_you_know()
ask_user()
