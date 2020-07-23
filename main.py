import pickle
import os
import pathlib


class Account:
    account_number = 0
    account_name = ""
    account_type = ""
    account_balance = 0

    def __init__(self, number, name, typ, balance):
        self.account_number = number
        self.account_name = name
        self.account_type = typ
        self.account_balance = balance


def update_file(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        lis = pickle.load(infile)
        infile.close()
        lis.append(account)
        os.remove("accounts.data")
    else:
        lis = [account]
    outfile = open("new_accounts.data", "wb")
    pickle.dump(lis, outfile)
    outfile.close()
    os.rename("new_accounts.data", "accounts.data")
    print("\nAccount Created")


def deposit_withdraw(acc_num, num):
    file = pathlib.Path("accounts.data")
    found = False
    if file.exists():
        infile = open("accounts.data", "rb")
        lis = pickle.load(infile)
        infile.close()
        for item in lis:
            if item.account_number == acc_num:
                os.remove("accounts.data")
                found = True
                if num == 1:
                    amount = int(input("Enter amount to be deposited: "))
                    item.account_balance += amount
                    print("Amount deposited successfully")
                elif num == 2:
                    amount = int(input("Enter withdraw amount: "))
                    if amount <= item.account_balance:
                        item.account_balance -= amount
                        print("Please collect your amount")
                    else:
                        print("Insufficient amount")
        if found:
            outfile = open("new_accounts.data", "wb")
            pickle.dump(lis, outfile)
            outfile.close()
            os.rename("new_accounts.data", "accounts.data")
        else:
            print("You need to create account")
    else:
        print("You need to create account")


def balance_enquiry(acc_no):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        lis = pickle.load(infile)
        infile.close()
        found = False
        for item in lis:
            if item.account_number == acc_no:
                found = True
                print("Your account balance is:", item.account_balance)
        if not found:
            print("You need to create account")
    else:
        print("You need to create account")


def display_all():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        lis = pickle.load(infile)
        infile.close()
        for item in lis:
            print(item.account_number, " ", item.account_name, " ", item.account_type, " ", item.account_balance)
    else:
        print("No accounts to display")


def delete_account(acc_num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        lis = pickle.load(infile)
        infile.close()
        os.remove("accounts.data")
        new_lis = []
        for item in lis:
            if item.account_number != acc_num:
                new_lis.append(item)
        outfile = open("new_accounts.data", "wb")
        pickle.dump(new_lis, outfile)
        outfile.close()
        os.rename("new_accounts.data", "accounts.data")
        print("Account deleted successfully")
    else:
        print("No account found")


def modify_account(acc_num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        lis = pickle.load(infile)
        infile.close()
        found = False
        for item in lis:
            if item.account_number == acc_num:
                os.remove("accounts.data")
                found = True
                item.account_name = input("Enter your name: ")
                item.account_type = input("Enter account type: ")
        if found:
            outfile = open("new_accounts.data", "wb")
            pickle.dump(lis, outfile)
            outfile.close()
            os.rename("new_accounts.data", "accounts.data")
            print("Account updated successfully")
        else:
            print("You need to create an account")
    else:
        print("You need to create an account")


# Program Start
while 1:
    print("\n1. New Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Balance Enquiry")
    print("5. List of all account")
    print("6. Modify an account")
    print("7. Close an account")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        number = int(input("Enter the account no: "))
        name = input("Enter your name: ")
        typ = input("Enter account type [C/S]: ")
        balance = int(input("Enter initial amount to be deposited: "))
        account = Account(number, name, typ, balance)
        update_file(account)
    elif choice == 2:
        number = int(input("Enter account no: "))
        deposit_withdraw(number, 1)
    elif choice == 3:
        number = int(input("Enter account no: "))
        deposit_withdraw(number, 2)
    elif choice == 4:
        number = int(input("Enter account no: "))
        balance_enquiry(number)
    elif choice == 5:
        display_all()
    elif choice == 6:
        number = int(input("Enter account no: "))
        modify_account(number)
    elif choice == 7:
        number = int(input("Enter account no: "))
        delete_account(number)
    elif choice == 8:
        print("\nThank you for using bank management system")
        exit()
    else:
        print("Invalid choice")
