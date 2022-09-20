import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.title('Record Book')
root.resizable(0, 0)
window_width = 515
window_height = 430

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=3)

# firstname
fN_label = ttk.Label(root, text="First Name:")
fN_label.grid(column=1, row=0, sticky=tk.E, padx=5, pady=2)

fN_entry = ttk.Entry(root)
fN_entry.grid(column=2, row=0, sticky=tk.NW, padx=5, pady=2)

# surname
fN_label = ttk.Label(root, text="Surname:")
fN_label.grid(column=1, row=1, sticky=tk.E, padx=5, pady=2)

fN_entry = ttk.Entry(root)
fN_entry.grid(column=2, row=1, sticky=tk.W, padx=5, pady=2)

# age
fN_label = ttk.Label(root, text="Age:")
fN_label.grid(column=1, row=2, sticky=tk.E, padx=5, pady=2)

fN_entry = ttk.Entry(root)
fN_entry.grid(column=2, row=2, sticky=tk.W, padx=5, pady=2)

# Mobile
fN_label = ttk.Label(root, text="Mobile:")
fN_label.grid(column=1, row=3, sticky=tk.E, padx=5, pady=2)

fN_entry = ttk.Entry(root)
fN_entry.grid(column=2, row=3, sticky=tk.W, padx=5, pady=2)

# email
fN_label = ttk.Label(root, text="Email:")
fN_label.grid(column=1, row=4, sticky=tk.E, padx=5, pady=2)

fN_entry = ttk.Entry(root)
fN_entry.grid(column=2, row=4, sticky=tk.W, padx=5, pady=2)

# checkbox code
check_button_label = ttk.Label(root, text="Friend:")
check_button_label.grid(column=1, row=5, sticky=tk.E, padx=1)

check_button = ttk.Checkbutton(root)
check_button.grid(column=2, row=5, sticky=tk.W, padx=1)

# display an image label
photo = tk.PhotoImage(file='./eelon.png')
image_label = ttk.Label(root,image=photo,padding=5)
image_label.grid(column=2, row=6, sticky=tk.W, padx=5, pady=2)

# save button
save_button = ttk.Button(root, text="Save Contact")
save_button.grid(column=2, row=7, sticky=tk.W, padx=5, pady=2)

# Display button
Display_button = ttk.Button(root, text="Display Contact")
Display_button.grid(column=0, row=7, padx=5, pady=2)

# Contact List label
cL_label = ttk.Label(root, text="Contact List")
cL_label.grid(column=0, row=1, padx=5, pady=2)

# create a list box
Contacts = ('Elon Musk', 'Miley Cyrus')

var = tk.Variable(value=Contacts)

listbox = tk.Listbox(root,listvariable=var,height=10,selectmode=tk.EXTENDED)
listbox.grid(column=0, row=2, rowspan=6, sticky=tk.N, padx=30, pady=2)

def items_selected(event):
    # get all selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_Contacts = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'
    showinfo(title='Information', message=msg)

listbox.bind('<<ListboxSelect>>',items_selected)

root.mainloop()
