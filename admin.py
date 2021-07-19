import os
import pathlib
import random
import string

from user import UserAccount
from global_methods import *
from main import Main


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
                    raise ValueError
                else:
                    file = pathlib.Path("accounts.data")
                    if file.exists() and os.stat("accounts.data").st_size != 0:
                        account_list = get_file_data()
                        for item in account_list:
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
                    raise ValueError
                break
            except ValueError:
                print("Invalid PIN")
        while True:
            try:
                balance = int(input("Enter The Initial amount > 500"))
                if type(balance) is int and balance < 500:
                    raise ValueError
                break
            except ValueError:
                print("Invalid Amount")

        while True:
            try:
                transaction_limit = int(input("Enter the transaction limit"))
                if type(transaction_limit) is not int:
                    raise ValueError
                break
            except ValueError:
                print("Invalid transaction")
        return acc_no, name, pin, balance, user_id, transaction_limit

    def create_account(self):
        """

        :return:
        """
        account_no, name, pin, balance, user_id, transaction_limit = self.get_registration_details()
        user = UserAccount(acc_no=account_no, name=name, pin=pin, balance=balance, user_id=user_id,
                           transaction_limit=transaction_limit)
        file = pathlib.Path("accounts.data")
        if file.exists() and os.stat("accounts.data").st_size != 0:
            infile = open('accounts.data', 'rb')
            old_list = pickle.load(infile)
            old_list.append(user)
            infile.close()
        else:
            old_list = [user]
        outfile = open('accounts.data', 'wb')
        pickle.dump(old_list, outfile)
        outfile.close()

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
                             item.balance, item.user_id, msg))
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
                if item.user_id == id:
                    check = True
                    break
                else:
                    continue
            if check:
                for item in old_list:
                    if item.user_id != id:
                        new_list.append(item)

                        print("Account Deleted")
            else:
                print("Record not found")
            write_data_infile(my_list=new_list)
        else:
            print("No data")

    def freeze_account(self, user_id):
        """

        :param user_id:
        :param name:
        :return:
        """
        file = pathlib.Path("accounts.data")
        check = False
        if file.exists():
            old_list = get_file_data()
            new_list = []

            for item in old_list:
                if item.user_id == user_id:
                    check = True
                    break
                else:
                    continue
            if check:
                for item in old_list:
                    if item.user_id != user_id:
                        new_list.append(item)
                    else:
                        item.freeze = True
                        new_list.append(item)
                        print("Account of {} is being frozen".format(item.name))
            else:
                print("Record not found")
            write_data_infile(my_list=new_list)


    def show_transactions(self):
        """

        :return:
        """
        list_transactions = []
        try:
            with open("transactions.csv", mode="r") as file:
                count = 0
                for line in file:
                    list_transactions.append(line.strip('\n'))
        except FileNotFoundError:
            print("File of transactions not Found")
            return

        # Print in the reverse order to show the latest transactions
        total = len(list_transactions)
        i = total - 1
        while i > total - 1000 and i >= 0:
            print(list_transactions[i])
            i -= 1

    def show_report(self, input_which, type_report, choice):
        if choice == 1:
            action = "Deposit"
        else:
            action = "Withdraw"

        if type_report == 0:
            print("Daily REPORT")
        elif type_report == 1:
            print("Monthly report")
        elif type_report == 2:
            print("#Yearly report")

        try:
            input_data = None
            file = open("transactions.csv", "r")
            count = 0
            for lines in file:
                tokenized = lines.strip('\n').split(",")
                if type_report == 0:
                    input_data = int(tokenized[4].split("/")[0])
                elif type_report == 1:
                    input_data = int(tokenized[4].split("/")[1])
                elif type_report == 2:
                    input_data = int(tokenized[4].split("/")[2])

                if input_data == input_which and action == tokenized[2]:
                    print(lines)
                    count += 1

            if count == 0:
                print("No Transactions found")
        except FileNotFoundError:
            print("No transactions found to generate report")


    def admin_menu(self):
        """

        :return:
        """
        while True:
            try:
                msg = "Please Enter\n"
                value = int(input("{} 1 for Create account : \n 2 for Show Details : \n "
                                  "3 for Show Transactions : \n "
                                  "4 for Delete Account : \n 5 for Freeze Account: \n"
                                  "6 for Show Reports : \n 0 for Main menu : \n Enter here : ".format(msg)))
                if 0 > value > 6:
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
                        user_id = input("Please Enter Account Holder name : ")
                        self.freeze_account(user_id)

                    elif value == 6:
                        while 1:
                            try:
                                choiceCash = int(input("Enter the type of report:\n1.Cash in\n2.Cash out\n : "))
                                choice = int(input("1.By Day.\n2.By Month\n3.By year\n4.Exit\nEnter your choice: "))
                                if choice == 1:
                                    day = int(input("Enter a day to see the report(1-31): "))
                                    if day < 1 or day > 31:
                                        print("Input out of range")
                                    else:
                                        self.show_report(day, 0, choiceCash)
                                elif choice == 2:
                                    month = int(input("Enter a month to see the report(1-12): "))
                                    if month < 1 or month > 12:
                                        print("Input must be  of range")
                                    else:
                                        self.show_report(month, 1, choiceCash)
                                elif choice == 3:
                                    year = int(input("Enter a year to see the report: "))
                                    self.show_report(year, 2, choiceCash)
                                elif choice == 4:
                                    break
                                else:
                                    print("Wrong input try again")
                            except ValueError:
                                print("Only integers allowed")


                    elif value == 0:
                        return Main.main_menu()
            except ValueError:
                print("Invalid integer. The number must be in the range of 1-10.")


