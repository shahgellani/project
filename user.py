
import pathlib
import pickle

import main


class UserAccount:
    def __init__(self, name=None, pin=None, acc_no=None, balance=None, user_id=None):
            self.name = name
            self.pin = pin
            self.accNo = acc_no
            self.balance = balance
            self.user_id = user_id
            self.freeze = False


    def deposit(self,):
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            my_list = pickle.load(infile)
            infile.close()
            for item in my_list:
                if item.user_id == self.user_id:
                    amount = int(input("Enter the amount to deposit : "))
                    item.balance += amount
                    print("Your account is updted")
            outfile = open('accounts.data', 'wb')
            pickle.dump(my_list, outfile)
            outfile.close()
        else:
            print("No records to Search")

    def check_amount(self):
        """

        :return:
        """
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            my_list = pickle.load(infile)
            infile.close()
            for item in my_list:
                if item.user_id == self.user_id:
                    print("Balance : {}".format(item.balance))

    def print_statement(self):
        """

        :return:
        """
        pass























    def with_drwal_amount(self):
        """

        :return:
        """
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            my_list = pickle.load(infile)
            infile.close()
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
                    except ValueError:
                        print("Invalid Operation")
            outfile = open('accounts.data', 'wb')
            pickle.dump(my_list, outfile)
            outfile.close()

    def change_pin_code(self):
        """

        :return:
        """
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            my_list = pickle.load(infile)
            infile.close()
            pin = int(input("Please Enter PIN code"))
            for item in my_list:
                if pin == item.pin:
                    new_pin = int(input("Please Enter new PIN"))
                    temp_pin = int(input("Re-Enter new PIN"))
                    if new_pin == temp_pin:
                        item.pin = new_pin
                        print("PIN Changed")
                        out_file = open('accounts.data', 'wb')
                        pickle.dump(my_list , out_file)
                        out_file.close()
                        return 

                    else:
                        print("PIN missmatched")











    def print_trasaction_history(self):
        """

        :return:
        """
        pass

    def show_reports(self):
        """

        :return:
        """
        pass

    def user_menu(self):
        """

        :return:
        """
        while True:
            try:
                msg = "Please Enter\n"

                value = int(input("{} 1 for Deposit Amount\n 2 Withdrawal  Amount\n 3 for Show Transactions History\n "
                                  "4 Print Statement \n 5 for Transfer Amount \n "
                                  "6 for change PIN \n 7 for Reports \n 0 for Main menu \nEnter here : ".format(msg)))
                if value > 7 or value < 0:
                    print("Please Enter valid num from menu")
                else:
                    if value == 1:
                        self.deposit()

                    elif value == 2:
                        self.with_drwal_amount()

                    elif value == 3:
                        self.print_trasaction_history()

                    elif value == 4:
                        self.print_statement()

                    elif value == 5:
                        name = input("Please Enter Account Holder name : ")
                        self.transfer_amount()

                    elif value == 6:
                        self.change_pin_code()

                    elif value == 7:
                        self.show_reports()

                    elif value == 0:
                        return main.main_menu()
            except ValueError:
                print("Invalid integer. The number must be in the range of 1-10.")
