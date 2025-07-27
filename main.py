#importing modules
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="poah",
    database="password_manager"
)


login=Tk()
login.geometry('543x232+50+100')
login.maxsize(543,232)
login.minsize(532,232)
login.iconbitmap("iconpm.ico")
login.title('Login Page')
login.configure(bg='#49beb7')


def login_command():
    if mainpage_entry.get() == "poah" :  #Set your password/masterkey here --------
        mainpage_entry.delete(0,'end')
        return mainwindow()
        print(mainwindow())

    else:
        messagebox.showerror("Please Try Again","Access Denied!")
        

Label(login, text ="___Login___",font = "Monaco 20 bold",relief="ridge",bg="#f38181", borderwidth=5).pack(fill = X)
Label(login, text="Master Key", font="Calibri 20 bold" ,bg ='#49beb7').place(x=8,y=55)
login_pass = StringVar()
mainpage_entry = Entry(login, textvariable=login_pass,show="*",font = "monaco 10 ")
mainpage_entry.pack(side ='top',ipadx=20 , ipady=10  ,pady=10)
Login_button=Frame(login, bg="#247e6c", relief="sunken", borderwidth=5)
Login_button.pack(side="bottom",anchor="s")
Button(Login_button, text="Login",font="Dubai",command = login_command).grid(ipadx =50)

def mainwindow():
    root = Tk()
    root.geometry("570x532+630+220")
    root.iconbitmap("iconpm.ico")
    root.minsize(570, 532)
    root.maxsize(570, 532)

    root.title("Password Manager")

    def add():
        def add_entry():
            mycur = mydb.cursor()
            command = f"insert into datb values('{websiteentry.get()}', '{usernameentry.get()}', '{passwordentry.get()}')"
            mycur.execute(command)
            messagebox.showinfo("Password Manager", "Your details have been submitted!")

            mydb.commit()

            websiteentry.delete(0, 'end')
            usernameentry.delete(0, 'end')
            passwordentry.delete(0, 'end')

        def close():
            addwin.destroy()

        addwin = Tk()
        addwin.geometry("393x300+200+400")
        addwin.maxsize(393, 300)
        addwin.minsize(393, 300)
        addwin.configure(bg='#E5C4F6')
        addwin.iconbitmap("iconpm.ico")
        addwin.title("New Entry")
        Label(addwin, text=" Website's Name ", font="Helvetica 12 bold", bg="#E5C4F6").grid(row=0)
        Label(addwin, text="Username", font="Helvetica 12 bold", bg="#E5C4F6").grid(row=1)
        Label(addwin, text="Password", font="Helvetica 12 bold", bg="#E5C4F6").grid(row=2)

        Websiteval = StringVar()
        Usernameval = StringVar()
        Passwordval = StringVar()

        websiteentry = Entry(addwin, textvariable=Websiteval)
        usernameentry = Entry(addwin, textvariable=Usernameval)
        passwordentry = Entry(addwin, textvariable=Passwordval)

        websiteentry.grid(row=0, column=1, ipady=5, ipadx=5)
        usernameentry.grid(row=1, column=1, ipady=5, ipadx=5)
        passwordentry.grid(row=2, column=1, ipady=5, ipadx=5)
        button_frame = Frame(addwin, bg="#ff496c", relief="raised", borderwidth=6)
        button_frame.place(y=240)
        Button(button_frame, text="Submit", font="Dubai", command=add_entry).grid(row=0, ipadx=65)
        Button(button_frame, text="Close", font="Dubai", command=close).grid(row=0, column=1, ipadx=70)


        addwin.mainloop()

    def logoff():
        root.destroy()

#Defining previous data
    def prevdata():
        prev = Tk()
        prev.geometry("595x600+1250+100")
        prev.maxsize(595, 600)
        prev.minsize(595, 600)
        prev.configure(bg='#f08080')
        prev.iconbitmap("iconpm.ico")
        prev.title("All Passwords")

        frame_data = Frame(prev, bg="#11cbd7", borderwidth=2, relief="sunken")
        frame_data.pack()

        # treeview table definition

        tree_scrollbar = Scrollbar(frame_data)
        tree_scrollbar.pack(side=RIGHT, fill=Y)
        my_tree = ttk.Treeview(frame_data, yscrollcommand=tree_scrollbar.set)
        my_tree.pack(ipady=200)

        tree_scrollbar.config(command=my_tree.yview)

        my_tree['columns'] = ("Website", "Username", "Password")

        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Website", anchor="center", width=200)
        my_tree.column("Username", anchor=CENTER, width=170)
        my_tree.column("Password", anchor=CENTER, width=200)

        my_tree.heading("#0", text="", anchor="w")
        my_tree.heading("Website", text="Website", anchor="center")
        my_tree.heading("Username", text="Username", anchor="center")
        my_tree.heading("Password", text="Password", anchor="center")


        mycur = mydb.cursor()
        mycur.execute("SELECT * FROM DATB")
        result = mycur.fetchall()

        count = 0
        for rec in result:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(rec[0], rec[1], rec[2]))
            count += 1

        prev.mainloop()

    # main loop code
    frame_label = Frame(root, bg="#40a6c3", relief="groove", borderwidth=5)
    frame_label.pack(fill=X)
    Label(frame_label, text="Password Manager", font="Monaco 20 bold").pack()

    frame_button = Frame(root, bg="#40a6c3", relief="groove", borderwidth=5)
    frame_button.pack(side="bottom", anchor="s", fill=X)
    Button(frame_button, text="Add New", font="Monaco 15", command=add).grid(ipadx =20)
    Button(frame_button ,text="Show All Passwords",font="Monaco 15" ,command= prevdata).grid(row=0, column=1)
    Button(frame_button, text="Log Off", font="Monaco 15", command=logoff).grid(row=0, column=2 ,ipadx=40)

    # Image Source
    photo = PhotoImage(file="password.png",master=root)
    bg =Label(root,image= photo)
    bg.image=photo
    bg.pack(padx=20,pady=20)

login.mainloop()



