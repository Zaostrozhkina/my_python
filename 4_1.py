from sys import argv


def salary():
    try:
        name, work, rate, premium = argv
        print(float(work) * float(rate) + float(premium))
    except ValueError:
        print("All values must be numbers (3 numbers)")


salary()
