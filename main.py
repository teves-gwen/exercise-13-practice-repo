from gwn10package.teves import teves_profile
from gwn10package.bataller import bataller_profile

def main_menu():
    """ Main program to display team member profiles. """
    print("\n++ GWN10 Team members ++")
    print("1. Gwen Teves")
    print("2. Christian Bataller")
    print("0. Exit")

    return input("\nEnter your choice: ").strip()

while True:
    choice = main_menu()

    match choice:
        case "1":
            teves_profile()
        case "2":
            bataller_profile()
        case "0":
            print("\nExiting the program...")
            break
        case _:
            print("\nInvalid choice. Please try again.")
