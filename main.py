from gwn10package.teves import teves_profile
from gwn10package.bataller import bataller_profile
from gwn10package.sario import sario_profile
from gwn10package.gonato import gonato_profile
from gwn10package.miguel import miguel_profile

def main_menu():
    """ Main program to display team member profiles. """
    print("\n++ GWN10 Team members ++")
    print("1. Gwen Teves")
    print("2. Christian Bataller")
    print("3. Gerald Sario")
    print("4. Alexa Gonato")
    print("5. Kian Miguel")
    print("0. Exit")

    return input("\nEnter your choice: ").strip()

while True:
    choice = main_menu()

    match choice:
        case "1":
            teves_profile()
        case "2":
            bataller_profile()
        case "3":
            sario_profile()
        case "4":
            gonato_profile()
        case "5":
            miguel_profile()
        case "0":
            print("\nExiting the program...")
            break
        case _:
            print("\nInvalid choice. Please try again.")
