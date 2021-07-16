import os
import pathlib
import pickle
import random
import string

import util
from user import UserAccount

from main import main_menu


class Admin:
    def __init__(self):
        self.id = "admin"
        self.pas = "admin"


    def login(self, id, pas):
        """

        :param id:
        :param pas:
        :return:
        """

        if self.id == id and self.pas == pas:
            print("login Successful")
            self.admin_menu()
        else:
            print("Invalid Credentials")
            return

    def get_registration_details(self):
        """

        :return:
        """
        acc_no = "AQ3114{}".format(''.join(random.choices(string.digits, k=8)))
        name = input("Enter the account holder name : ")

        while True:

            try:
                user_id = str(input("Enter the ID, ID must be between 10 to 20 characters"))
                if len(user_id) > 20 or len(user_id) < 10:
                    raise ValueError  # this will send it to the print message and back to the input option
                else:
                    file = pathlib.Path("accounts.data")
                    if file.exists() and os.stat("accounts.data").st_size != 0:
                        infile = open('accounts.data', 'rb')
                        list = pickle.load(infile)
                        infile.close()
                        for item in list:
                            if item.user_id == user_id:
                                raise ValueError
                        break
                    else:
                        break
            except ValueError:
                print("Invalid Operation or ID Already Taken")
        while True:
            try:
                pin = int(input("Enter the pin of account, PIN must be 4 digited : "))
                if type(pin) is int and len(str(pin)) != 4:
                    raise ValueError  # this will send it to the print message and back to the input option
                break
            except ValueError:
                print("Invalid PIN")
        while True:
            try:
                balance = int(input("Enter The Initial amount > 500"))
                if type(balance) is int and balance < 500:
                    raise ValueError  # this will send it to the print message and back to the input option
                break
            except ValueError:
                print("Invalid Amount")
        return acc_no, name, pin, balance, user_id

    def create_account(self):
        """

        :return:
        """
        account_no, name, pin, balance, id = self.get_registration_details()
        user = UserAccount(acc_no=account_no, name=name, pin=pin, balance=balance, user_id=id)
        file = pathlib.Path("accounts.data")
        if file.exists() and os.stat("accounts.data").st_size != 0:
            infile = open('accounts.data', 'rb')
            old_list = pickle.load(infile)
            old_list.append(user)
            infile.close()
            #os.remove('accounts.data')
        else:
            old_list = [user]
        outfile = open('accounts.data', 'wb')
        pickle.dump(old_list, outfile)
        outfile.close()
        #os.rename('newaccounts.data', 'accounts.data')

    def show_details(self):
        """

        :return:
        """
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            my_list = pickle.load(infile)
            for item in my_list:
                if not item.freeze:
                    msg = "Active Account"
                else:
                    msg = "Frozen Account"
                print("Account No : {}\nAccount Holder Name : {}\nBalance : {}\n User_ID : {} \n Account Status : {}".
                                                                                        format(item.accNo,
                                                                                        item.name,
                                                                                        item.balance, item.user_id,  msg))
            infile.close()
        else:
            print("No records to display")

    def delete_account(self, id):
        """

        :param id:
        :return:
        """
        file = pathlib.Path("accounts.data")
        check = False
        if file.exists():
            infile = open('accounts.data', 'rb')
            old_list = pickle.load(infile)
            infile.close()
            new_list = []

            for item in old_list:
                if item.id == id:
                    check = True
                    break
                else:
                    continue
            if check:
                for item in old_list:
                    if item.name != id:
                        new_list.append(item)

                        print("Account Deleted")
            else:
                print("Record not found")
            #os.remove('accounts.data')
            outfile = open('accounts.data', 'wb')
            pickle.dump(new_list, outfile)
            outfile.close()
            #os.rename('tempaccounts.data', 'accounts.data')

    def freeze_account(self, name):
        """

        :param name:
        :return:
        """
        file = pathlib.Path("accounts.data")
        check = False
        if file.exists():
            infile = open('accounts.data', 'rb')
            old_list = pickle.load(infile)
            infile.close()
            new_list = []

            for item in old_list:
                if item.name == name:
                    check = True
                    break
                else:
                    continue
            if check:
                for item in old_list:
                    if item.name != name:
                        new_list.append(item)
                    else:
                        item.freeze = True
                        new_list.append(item)
                        print("Account of {} is being freezed".format(item.name))
            else:
                print("Record not found")
            #os.remove('accounts.data')
            outfile = open('accounts.data', 'wb')
            pickle.dump(new_list, outfile)
            outfile.close()
            #os.rename('tempaccounts.data', 'accounts.data')

    def admin_menu(self):
            """

            :return:
            """
            while True:
                try:
                    msg = "Please Enter\n"
                    value = int(input("{} 1 for Create account\n 2 for Show Details\n 3 for Show Transactions\n "
                                      "4 for Delete Account\n 5 for Freeze Account \n 6 for Set Transaction limit \n "
                                      "7 for Show Reports\n 0 for Main menu \n Enter here : ".format(msg)))
                    if 0 > value > 7:
                        print("Please Enter valid num from menu")
                    else:
                        if value == 1:
                            self.create_account()

                        elif value == 2:
                            self.show_details()

                        elif value == 3:
                            self.show_transactions()

                        elif value == 4:
                            name = input("Please Enter Account Holder name : ")
                            self.delete_account(name)

                        elif value == 5:
                            name = input("Please Enter Account Holder name : ")
                            self.freeze_account(name)

                        elif value == 6:
                            self.set_transaction_limit()

                        elif value == 7:
                            self.show_report()

                        elif value == 0:
                            return main_menu()
                except ValueError:
                    print("Invalid integer. The number must be in the range of 1-10.")

    def show_transactions(self):
        pass

    def set_transaction_limit(self):
        pass

    def show_report(self):
        pass
