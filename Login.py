import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#BDEDFF') 

# search up colors code for range of colors 

def login():
    username = "COSC23"
    password = "1111"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#BDEDFF')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#BDEDFF', fg="#A9A9A9", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#BDEDFF', fg="#A9A9A9", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#BDEDFF', fg="#A9A9A9", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#BDEDFF", fg="#A9A9A9", font=("Arial", 16), command=login)

# Widgets adjustment
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=50)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=40)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=40)
login_button.grid(row=3, column=0, columnspan=2, pady=50)

frame.pack()

window.mainloop()
