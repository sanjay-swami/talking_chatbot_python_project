from tkinter import *
from tkinter import messagebox
import main_app


def login_here():
    user = user_entry.get()
    pwd =password_entry.get()
    
    if user == 'admin' and pwd == 'admin123':
        messagebox.showinfo("Login Successful", "Welcome to Project")
        root.destroy()
        main_app.my_app_gui()

    else:
        messagebox.showerror("Login Unsuccessful", "Try again with correct details")


root = Tk()
root.config(bg="black")
root.title("Login Screen")
root.geometry("1920x1080")

photoImg = PhotoImage(file=r"user.png")
photo_label = Label(root, image=photoImg, text='Login Here', compound=TOP, bg='black',
                     fg='white', font=("Times New Roman", 25, 'bold'))
photo_label.pack(pady=20)

user_frame = Frame(root, bg='black')
user_frame.pack(pady=20)


user_label = Label(user_frame, text='Username', bg='black',
                     fg='white', font=("Times New Roman", 20, 'bold'))
user_label.pack(side=LEFT, padx=20)

user_entry = Entry(user_frame, font=("Times New Roman", 20, 'bold'))
user_entry.pack()


password_frame = Frame(root, bg='black')
password_frame.pack(pady=20)

password_label = Label(password_frame, text='Password', bg='black',
                     fg='white', font=("Times New Roman", 20, 'bold'))
password_label.pack(side=LEFT, padx=20)

password_entry = Entry(password_frame, font=("Times New Roman", 20, 'bold'), show="*")
password_entry.pack()

btn_frame = Frame(root, bg='black')
btn_frame.pack()

login_btn = Button(btn_frame, command=login_here, text= 'Login', bg='green',
                     fg='white', font=("Times New Roman", 20, 'bold') )
login_btn.pack()


root.mainloop()