import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime


def Main_Menu():
    root = tk.Tk()
    root.geometry("1300x600")
    root.title("State Bank")

    frame1 = tk.Frame(root)
    frame1.pack(side="top")
    bg_image = tk.PhotoImage(file="coin_pile.gif")
    x = tk.Label(image=bg_image)
    x.place(y=-400)

    l_title = tk.Message(text="BANKING SYSTEM", width=700, fg="black")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")

    img_create_acc = tk.PhotoImage(file="create_new_account.gif")
    img_create = img_create_acc.subsample(2, 2)
    button_create = tk.Button(image=img_create, command=Create_Account)
    button_create.image = img_create

    img_login = tk.PhotoImage(file="login.gif")
    img_log = img_login.subsample(2, 2)
    button_login = tk.Button(image=img_log, command=lambda: Login_Account(root))
    button_login.image = img_log

    img_quit = tk.PhotoImage(file="quit.GIF")
    img_q = img_quit.subsample(2, 2)
    button_quit = tk.Button(image=img_q, command=root.destroy)
    button_quit.image = img_q

    button_create.place(x=800, y=300)
    button_login.place(x=800, y=200)
    button_quit.place(x=920, y=400)
    root.mainloop()


def Create_Account():
    root_create = tk.Tk()
    root_create.geometry("600x300")
    root_create.title("Create Account")

    l_title = tk.Message(root_create, text="STATE BANK", fg="black")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")

    label_name = tk.Label(root_create, text="Enter Name:", relief="raised")
    label_name.pack(side="top")
    entry_name = tk.Entry(root_create)
    entry_name.pack(side="top")

    label_balance = tk.Label(root_create, text="Enter opening balance:", relief="raised")
    label_balance.pack(side="top")
    entry_balance = tk.Entry(root_create)
    entry_balance.pack(side="top")

    label_pin = tk.Label(root_create, text="Enter desired PIN:", relief="raised")
    label_pin.pack(side="top")
    entry_pin = tk.Entry(root_create, show="*")
    entry_pin.pack(side="top")

    button_submit = tk.Button(root_create, text="Submit",
                              command=lambda: Write_Account(root_create, entry_name.get().strip(),
                                                            entry_balance.get().strip(), entry_pin.get().strip()))
    button_submit.pack(side="top")
    root_create.bind("<Return>", lambda x: Write_Account(root_create, entry_name.get().strip(),
                                                         entry_balance.get().strip(), entry_pin.get().strip()))
    return


def Write_Account(master, name, balance, pin):
    if (is_number(name)) or (is_number(balance) == 0) or (is_number(pin) == 0) or name == "":
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    file = open("Account_Record.txt", 'r')
    account_no = int(file.readline())
    account_no += 1
    file.close()

    file = open("Account_Record.txt", 'w')
    file.write(str(account_no))
    file.close()

    account_file = open(str(account_no) + ".txt", "w")
    account_file.write(pin + "\n")
    account_file.write(balance + "\n")
    account_file.write(str(account_no) + "\n")
    account_file.write(name + "\n")
    account_file.close()

    file_rec = open(str(account_no) + "-rec.txt", 'w')
    file_rec.write("Date                             Credit      Debit     Balance\n")
    file_rec.write(
        str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + balance + "              " + balance + "\n")
    file_rec.close()

    messagebox.showinfo("Details", "Your Account Number is:" + str(account_no))
    master.destroy()
    return


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0


def Login_Account(master):
    master.destroy()
    root_login = tk.Tk()
    root_login.geometry("600x300")
    root_login.title("Log in")

    l_title = tk.Message(root_login, text="STATE BANK", fg="black")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")

    label_acc = tk.Label(root_login, text="Enter account number:", relief="raised")
    label_acc.pack(side="top")
    entry_acc = tk.Entry(root_login)
    entry_acc.pack(side="top")

    label_pin = tk.Label(root_login, text="Enter your PIN:", relief="raised")
    label_pin.pack(side="top")
    entry_pin = tk.Entry(root_login, show="*")
    entry_pin.pack(side="top")

    button_submit = tk.Button(root_login, text="Submit",
                              command=lambda: Login_Check(root_login, entry_acc.get().strip(), entry_pin.get().strip()))
    button_submit.pack(side="top")

    button_home = tk.Button(text="HOME", relief="raised", command=lambda: Return_Home(root_login))
    button_home.pack(side="top")

    root_login.bind("<Return>", lambda x: Login_Check(root_login, entry_acc.get().strip(), entry_pin.get().strip()))


def Login_Check(master, acc_no, pin):
    try:
        file = open(acc_no + ".txt", 'r')
        file_pin = file.readline()
        if int(file_pin) == int(pin):
            master.destroy()
            Logged_in_Menu(acc_no)
        else:
            messagebox.showinfo("Error", "Invalid PIN\nPlease try again.")
            return
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invalid Account Number!\nTry Again!")
        return
    file.close()


def Logged_in_Menu(acc_no):
    root = tk.Tk()
    root.geometry("1600x500")
    root.title("STATE BANK")

    fr1 = tk.Frame(root)
    fr1.pack(side="top")
    l_title = tk.Message(root, text="STATE BANK", fg="black")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")

    img_credit = tk.PhotoImage(file="credit_amount.gif")
    image_credit = img_credit.subsample(2, 2)
    button_credit = tk.Button(image=image_credit, command=lambda: Credit_Amount(acc_no))
    button_credit.image = image_credit

    img_debit = tk.PhotoImage(file="debit_amount.gif")
    image_debit = img_debit.subsample(2, 2)
    button_debit = tk.Button(image=image_debit, command=lambda: Debit_Amount(acc_no))
    button_debit.image = image_debit

    img_balance = tk.PhotoImage(file="check_balance.gif")
    image_balance = img_balance.subsample(2, 2)
    button_balance = tk.Button(image=image_balance, command=lambda: Display_Balance(acc_no))
    button_balance.image = image_balance

    img_transaction = tk.PhotoImage(file="transaction_history.gif")
    image_trans = img_transaction.subsample(2, 2)
    button_transaction = tk.Button(image=image_trans, command=lambda: Display_Transaction_History(acc_no))
    button_transaction.image = image_trans

    img_logout = tk.PhotoImage(file="logout.gif")
    img_q = img_logout.subsample(2, 2)
    button_logout = tk.Button(image=img_q, relief="raised", command=lambda: Logout(root))
    button_logout.image = img_q

    button_credit.place(x=100, y=180)
    button_debit.place(x=100, y=270)
    button_balance.place(x=900, y=180)
    button_transaction.place(x=900, y=270)
    button_logout.place(x=500, y=400)


def Credit_Amount(acc_no):
    root_credit = tk.Tk()
    root_credit.geometry("600x300")
    root_credit.title("Credit Amount")

    l_title = tk.Message(root_credit, text="STATE BANK", fg="black")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")

    label_credit = tk.Label(root_credit, relief="raised", text="Enter Amount to be credited: ")
    label_credit.pack(side="top")
    entry_credit = tk.Entry(root_credit, relief="raised")
    entry_credit.pack(side="top")
    button_credit = tk.Button(root_credit, text="Credit", relief="raised",
                              command=lambda: Write_Credit(root_credit, entry_credit.get(), acc_no))
    button_credit.pack(side="top")
    root_credit.bind("<Return>", lambda x: Write_Credit(root_credit, entry_credit.get(), acc_no))


def Write_Credit(master, amount, acc_no):
    if is_number(amount) == 0:
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    file = open(acc_no + ".txt", 'r')
    file_pin = file.readline()
    file_amount = int(file.readline())
    temp = file.readline()
    name = file.readline()
    file.close()
    credited_amount = int(amount) + file_amount

    file = open(acc_no + ".txt", 'w')
    file.write(file_pin)
    file.write(str(credited_amount) + "\n")
    file.write(acc_no + "\n")
    file.write(name + "\n")
    file.close()

    file_rec = open(str(acc_no) + "-rec.txt", 'a+')
    file_rec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + str(amount) + "              " +
                   str(credited_amount) + "\n")
    file_rec.close()

    messagebox.showinfo("Operation Successful!!", "Amount Credited Successfully!!")
    master.destroy()
    return


def Debit_Amount(acc_no):
    root_debit = tk.Tk()
    root_debit.geometry("600x300")
    root_debit.title("Debit Amount")

    l_title = tk.Message(root_debit, text="STATE BANK", fg="black")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")

    label_debit = tk.Label(root_debit, relief="raised", text="Enter Amount to be debited: ")
    label_debit.pack(side="top")
    entry_debit = tk.Entry(root_debit, relief="raised")
    entry_debit.pack(side="top")

    button_debit = tk.Button(root_debit, text="Debit", relief="raised",
                             command=lambda: Write_Debit(root_debit, entry_debit.get(), acc_no))
    button_debit.pack(side="top")

    root_debit.bind("<Return>", lambda x: Write_Debit(root_debit, entry_debit.get(), acc_no))


def Write_Debit(master, amount, acc_no):
    if is_number(amount) == 0:
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    file = open(acc_no + ".txt", 'r')
    file_pin = file.readline()
    file_amount = int(file.readline())
    temp = file.readline()
    name = file.readline()
    file.close()

    if int(amount) > file_amount:
        messagebox.showinfo("Error!!", "You don't have that amount left in your account\nPlease try again.")
    else:
        debited_amount = file_amount - int(amount)
        file = open(acc_no + ".txt", 'w')
        file.write(file_pin)
        file.write(str(debited_amount) + "\n")
        file.write(acc_no + "\n")
        file.write(name + "\n")
        file.close()

        file_rec = open(str(acc_no) + "-rec.txt", 'a+')
        file_rec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + "              " + str(amount) +
                       "              " + str(debited_amount) + "\n")
        file_rec.close()

        messagebox.showinfo("Operation Successful!!", "Amount Debited Successfully!!")
        master.destroy()
        return


def Display_Balance(acc_no):
    file = open(acc_no + ".txt", 'r')
    file.readline()
    bal = file.readline()
    file.close()
    messagebox.showinfo("Balance", bal)


def Display_Transaction_History(acc_no):
    root_display = tk.Tk()
    root_display.geometry("900x600")
    root_display.title("Transaction History")

    l_title = tk.Message(root_display, text="STATE BANK", fg="black",)
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")

    fr1 = tk.Frame(root_display)
    fr1.pack(side="top")
    label_transaction = tk.Message(root_display, text="Your Transaction History:", width=1000, bg="blue", fg="white",
                                   relief="raised")
    label_transaction.pack(side="top")

    fr2 = tk.Frame(root_display)
    fr2.pack(side="top")
    file_rec = open(acc_no + "-rec.txt", 'r')
    for line in file_rec:
        label = tk.Message(root_display, anchor="w", text=line, relief="raised", width=2000)
        label.pack(side="top")
    button_quit = tk.Button(root_display, text="Quit", relief="raised", command=root_display.destroy)
    button_quit.pack(side="top")
    file_rec.close()


def Logout(master):
    messagebox.showinfo("Logged Out", "You Have Been Successfully Logged Out!!")
    master.destroy()
    Main_Menu()


def Return_Home(master):
    master.destroy()
    Main_Menu()


Main_Menu()
