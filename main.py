# This is a sample Python script.
import os
import pathlib
import pickle
import admin

import user


def main_menu():
    """
    It is main menu
    :return:
    """
    check = True
    while True:
        try:
            value = int(input("Press 1 for Admin: \nPress 2 for User: \nPress 0 to exit() Value = "))

            if value == 1:
                print("Admin")
                admin_obj = admin.Admin()
                while True:
                    admin_user_name = input(str("Please Enter admin username : "))
                    admin_user_pass = input(str("Please Enter admin password : "))
                    admin_obj.login(admin_user_name, admin_user_pass)

            elif value == 2:
                while True:
                    user_id = input(str("Please Enter User ID : "))
                    user_pass = input(str("Please Enter user password : "))
                    file = pathlib.Path("accounts.data")
                    if file.exists() and os.stat("accounts.data").st_size != 0:

                        infile = open('accounts.data', 'rb')
                        my_list = pickle.load(infile)
                        for item in my_list:
                            if item.user_id == user_id and item.pin == int(user_pass):
                                check = False
                                if item.freeze:
                                    print("Inactive account, PLease contact Admin")
                                else:
                                    user_obj = user.UserAccount(user_id=user_id)
                                    user_obj.user_menu()
                        infile.close()
                    if check:
                        print("Invalid Credentials or User not exists")
                        break




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
