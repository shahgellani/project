import pathlib
import pickle
from datetime import date

from main import Main
from global_methods import *


class UserAccount:
    """

    """

    def __init__(self, name=None, pin=None, acc_no=None, balance=None, user_id=None, transaction_limit=None):
        """
        Constructor for creation of user. We can pass none or any value to parameters.
        :param name:
        :param pin:
        :param acc_no:
        :param balance:
        :param user_id:
        :param transaction_limit:
        """
        self.name = name
        self.pin = pin
        self.accNo = acc_no
        self.balance = balance
        self.user_id = user_id
        self.transaction_limit = transaction_limit
        self.freeze = False

    def set_all_attributes(self):
        my_list = get_file_data()
        for item in my_list:
            if self.user_id == item.user_id:
                self.accNo = item.accNo
                self.name = item.name
                self.transaction_limit = item.transaction_limit

    def to_write_csv(self, amount, type):
        towrite = "{},{},{},{},{}\n".format(self.user_id, self.name, type, amount, date.today().strftime("%d/%m/%Y"))

        transaction_file = open("transactions.csv", 'a')
        transaction_file.write(towrite)
        transaction_file.close()

    def deposit(self):
        """
        Method to deposit amount in user account

        :return:
        """
        my_list = get_file_data()  # Getting data from binary file
        for item in my_list:
            if item.user_id == self.user_id:
                amount = int(input("Enter the amount to deposit : "))
                item.balance += amount
                print("Your account is updted")
                self.to_write_csv(amount=amount, type="Deposit")
        write_data_infile(my_list=my_list)  # Writing data in accounts file

    def check_amount(self):
        """

        :return:
        """
        my_list = get_file_data()  # Getting data from binary file
        for item in my_list:
            if item.user_id == self.user_id:
                print("Balance : {}".format(item.balance))

    def with_drwal_amount(self):
        """
        Method for amount withdrawal

        :return:
        """
        my_list = get_file_data()  # Getting data from binary file
        for item in my_list:
            if item.user_id == self.user_id:
                try:
                    amount_tobe_withdrawl = int(input("Enter the amount to withdrawl : "))
                    if type(amount_tobe_withdrawl) is not int:
                        raise ValueError  # this will send it to the print message and back to the input option

                    if amount_tobe_withdrawl > item.balance:
                        print("Low Balance")
                    elif item.balance - amount_tobe_withdrawl < 500:
                        print("You can't withdrawl this amount")
                    elif amount_tobe_withdrawl % 500 != 0:
                        print("Amount must be multiple of 500")
                    else:
                        item.balance -= amount_tobe_withdrawl
                        self.to_write_csv(type="withdraw", amount=amount_tobe_withdrawl)
                except ValueError:
                    print("Invalid Operation")
        write_data_infile(my_list)  # Writing data from binary file

    def change_pin_code(self):
        """
        Method for changing PIN of user account

        :return:
        """
        my_list = get_file_data()  # Getting data from binary file
        pin = int(input("Please Enter PIN code"))
        for item in my_list:
            if pin == item.pin:
                new_pin = int(input("Please Enter new PIN"))
                temp_pin = int(input("Re-Enter new PIN"))
                if new_pin == temp_pin:
                    item.pin = new_pin
                    print("PIN Changed")
                    write_data_infile(my_list=my_list)  # Writing data in binary file
                    return

                else:
                    print("PIN mismatched")

    def print_transaction_history(self, show=10):
        """

        :return:
        """
        list_transactions = []
        try:
            with open("transactions.csv", mode="r") as file:
                count = 0
                for line in file:
                    if line.split(',')[0] == self.user_id:
                        list_transactions.append(line.strip('\n'))
        except FileNotFoundError:
            print("File of transactions not Found")
            return

        # Print in the reverse order to show the latest transactions
        total = len(list_transactions)
        i = total - 1
        while i > total - show and i >= 0:
            print(list_transactions[i])
            i -= 1

    def transfer_amount(self, account_no):
        """
        Method to transfer account in another account
        :return:
        """
        check = True
        transfer = False
        my_list = get_file_data()
        # Checking amount validity for transaction
        while check:
            amount = int(input("Please Enter Amount"))
            if type(amount) is not int:
                print("Please enter valid amount")  # If amount is not integer
                continue
            elif amount > self.transaction_limit:  # If amount is greater than transaction limit
                print("Transaction Limit exceeded")
                continue
            else:
                check = False
        # Make transaction
        try:
            for item in my_list:
                if item.user_id == self.user_id:
                    if amount > item.balance:  # Transfer amount is greater than current balance
                        print("Low Balance")
                    elif item.balance - amount < 500:  # Min amount must be >= 500
                        print("You can't transfer this amount")
                    else:
                        transfer = True
            # Amount update
            if transfer:
                for item in my_list:
                    if item.accNo != self.accNo and item.accNo == account_no:
                        item.balance += amount  # Amount added after transfer

                for item in my_list:
                    if item.accNo == self.accNo:
                        item.balance -= amount  # Amount subtracted from current user's account
                write_data_infile(my_list)
                self.to_write_csv(type="Transfer" , amount=amount)
        except:
            print("Invalid value")


    def user_menu(self):
        """
        User menu

        :return:
        """
        self.set_all_attributes()
        while True:
            try:
                msg = "Please Enter\n"

                value = int(input("{} 1 for Deposit Amount\n 2 Withdrawal  Amount\n 3 for Show Transactions History\n "
                                  "4 Print Statement \n 5 for Transfer Amount \n "
                                  "6 for change PIN \n 0 for Main menu \nEnter here : ".format(msg)))
                if value > 6 or value < 0:
                    print("Please Enter valid num from menu")
                else:
                    if value == 1:
                        self.deposit()

                    elif value == 2:
                        self.with_drwal_amount()

                    elif value == 3:
                        self.print_transaction_history(1000)

                    elif value == 4:
                        self.print_transaction_history()

                    elif value == 5:
                        account = False
                        account_no = input("Please Enter Account num : ")
                        my_list = get_file_data()
                        for item in my_list:
                            if item.accNo == account_no:
                                self.transfer_amount(account_no)
                                account = True
                        if account:
                            continue
                        else:
                            print("Account not found")
                            continue
                    elif value == 6:
                        self.change_pin_code()


                    elif value == 0:
                        return Main.main_menu()
            except ValueError:
                print("Invalid integer. The number must be in the range of 1-10.")
