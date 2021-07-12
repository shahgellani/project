import os
import pathlib
import pickle
import random
import string

from main import main_menu


class Admin:
    accNo = 0
    name = ''
    pin = 0
    balance = ''
    freeze = 0

    def __init__(self):
        self.id = "admin"
        self.pas = "admin"

    def line(self):
        print("                                                                                        ")
        print("----------------------------------------------------------------------------------------")
        print("                                                                                        ")

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
        self.accNo = "AQ3114{}".format(''.join(random.choices(string.digits, k=8)))
        self.name = input("Enter the account holder name : ")
        while True:
            try:
                self.pin = int(input("Enter the pin of account, PIN must be 4 digited : "))
                if type(self.pin) is int and len(str(self.pin)) != 4:
                    raise ValueError  # this will send it to the print message and back to the input option
                break
            except ValueError:
                print("Invalid PIN")

        while True:
            try:
                self.balance = int(input("Enter The Initial amount > 500"))
                if type(self.balance) is int and self.balance < 500:
                    raise ValueError  # this will send it to the print message and back to the input option
                break
            except ValueError:
                print("Invalid Amount")

    def create_account(self):
        admin = Admin()
        admin.get_registration_details()
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            oldlist = pickle.load(infile)
            oldlist.append(admin)
            infile.close()
            os.remove('accounts.data')
        else:
            oldlist = [admin]
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')

    def show_details(self):
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            mylist = pickle.load(infile)
            for item in mylist:
                self.line()
                print("Account No : {}\nAccount Holder Name : {}\nBalance : {}".format(item.accNo,
                                                                                        item.name,
                                                                                        item.balance))
            infile.close()
        else:
            print("No records to display")

    def delete_account(self, name):
        file = pathlib.Path("accounts.data")
        check = False
        if file.exists():
            infile = open('accounts.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            newlist = []

            for item in oldlist:
                if item.name == name:
                    check = True
                    break
                else:
                    continue
            if check:
                for item in oldlist:
                    if item.name != name:
                        newlist.append(item)

                        print("Account Deleted")
            else:
                self.line()
                print("Record not found")
            os.remove('accounts.data')
            outfile = open('tempaccounts.data', 'wb')
            pickle.dump(newlist, outfile)
            outfile.close()
            os.rename('tempaccounts.data', 'accounts.data'

    def freeze_account(self, name):
        file = pathlib.Path("accounts.data")
        check = False
        if file.exists():
            infile = open('accounts.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            newlist = []

            for item in oldlist:
                if item.name == name:
                    check = True
                    break
                else:
                    continue
            if check:
                for item in oldlist:
                    if item.name != name:
                        newlist.append(item)
                    else:
                        item.
            else:
                self.line()
                print("Record not found")
            os.remove('accounts.data')
            outfile = open('tempaccounts.data', 'wb')
            pickle.dump(newlist, outfile)
            outfile.close()
            os.rename('tempaccounts.data', 'accounts.data')

    def admin_menu(self):
            """

            :return:
            """
            while True:
                try:
                    msg = "Please Enter\n"
                    self.line()
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
                            self.freeze_account()

                        elif value == 6:
                            self.set_transaction_limit()

                        elif value == 7:
                            self.show_report()

                        elif value == 0:
                            break
                except ValueError:
                    print("Invalid integer. The number must be in the range of 1-10.")

    def show_transactions(self):
        pass

    def freeze_account(self):
        pass

    def set_transaction_limit(self):
        pass

    def show_report(self):
        pass
