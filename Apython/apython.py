from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# login function
def login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "admin@gmail.com" and password == "1234":
        messagebox.showinfo("Login Status", "Login Successful")
    else:
        messagebox.showerror("Login Status", "Invalid Email or Password")

root = Tk()
root.title("Student Form")
root.iconbitmap("pixel2.ico")

root.geometry('500x500+0+0')
root.configure(background='#00704A')

# image
img = Image.open('py.png')
resize_img = img.resize((100,70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root, image=img)
img_label.pack(pady=10, padx=20)

# title
text_label = Label(root,
                   text="amili  Bucks",
                   font=('Arial',18,'bold'),
                   bg='#00704A',
                   fg='white')
text_label.pack(pady=10, padx=20)

# email
email_label = Label(root,
                    text="Email",
                    font=('Arial',18,'bold'),
                    bg='#00704A',
                    fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root,
                    font=('Arial',18,'bold'),
                    fg='white',
                    bg='grey')
email_entry.pack(pady=(5,10))

# password
password_label = Label(root,
                       text="Password",
                       font=('Arial',18,'bold'),
                       bg='#00704A',
                       fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root,
                       font=('Arial',18,'bold'),
                       fg='white',
                       bg='grey',
                       show="*")
password_entry.pack(pady=(5,10))

# login button
login_btn = Button(root,
                   text="Login",
                   font=('Arial',18,'bold'),
                   bg='#00704A',
                   fg='white',
                   command=login)
login_btn.pack(pady=(10,10))

root.mainloop()