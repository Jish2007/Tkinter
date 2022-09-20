import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

CLIENT_NUMBER = "98065030"
PASSWORD = "0pens3sam3"


root = tk.Tk()
window_width = 300
window_height = 150

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)


root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.title('Log onto NetBank')

email = tk.StringVar()
password = tk.StringVar()

signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

email_label = ttk.Label(signin, text="Client Number:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, show="*", textvariable=password)
password_entry.pack(fill='x', expand=True)

def check():
    
    if email.get() == CLIENT_NUMBER and password.get() == PASSWORD:
        print("Login Successful")   
    else:
        print("Login Failed. Incorrect Password. Try again!")

login_button = ttk.Button(signin, text="Log on", command=check)
login_button.pack(fill='x', expand=True, pady=10)




root.mainloop()
