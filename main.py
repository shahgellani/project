# This is a sample Python script.
import admin


def main_menu():
    """
    It is main menu
    :return:
    """
    while True:
        try:
            value = int(input("Press 1 for Admin: \nPress 2 for User: \nPress 0 to exit() Value = "))

            if value == 1:
                print("Admin")
                admin_obj = admin.Admin()
                while True:
                    user_name = input(str("Please Enter admin username : "))
                    user_pass = input(str("Please Enter admin password : "))
                    admin_obj.login(user_name, user_pass)

            elif value == 2:

                print("User")

            elif value == 0:
                break
            else:
                print("Num must be 1 or 2")
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")







# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_menu()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
