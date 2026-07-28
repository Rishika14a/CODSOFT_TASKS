import tkinter as tk
from tkinter import messagebox


# ---------------- Window ----------------

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#1E1E1E")


# ---------------- Contact Storage ----------------

contacts = []


# ---------------- Functions ----------------

def add_contact():

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning(
            "Warning",
            "Name and Phone are required!"
        )
        return

    contact = f"{name} | {phone} | {email}"

    contacts.append(contact)

    contact_list.insert(
        tk.END,
        contact
    )

    clear_fields()

    messagebox.showinfo(
        "Success",
        "Contact Added!"
    )


def delete_contact():

    selected = contact_list.curselection()

    if selected:
        index = selected[0]

        contact_list.delete(index)

        contacts.pop(index)

    else:
        messagebox.showwarning(
            "Warning",
            "Select a contact first!"
        )


def search_contact():

    search = search_entry.get().lower()

    contact_list.delete(
        0,
        tk.END
    )

    for contact in contacts:

        if search in contact.lower():

            contact_list.insert(
                tk.END,
                contact
            )


def show_all():

    contact_list.delete(
        0,
        tk.END
    )

    for contact in contacts:

        contact_list.insert(
            tk.END,
            contact
        )


def clear_fields():

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)



# ---------------- Title ----------------

title = tk.Label(
    root,
    text="Contact Book",
    font=("Arial", 28, "bold"),
    bg="#1E1E1E",
    fg="white"
)

title.pack(pady=20)



# ---------------- Input Section ----------------

frame = tk.Frame(
    root,
    bg="#1E1E1E"
)

frame.pack()


tk.Label(
    frame,
    text="Name",
    font=("Arial",14),
    bg="#1E1E1E",
    fg="white"
).grid(row=0,column=0,pady=5)


name_entry = tk.Entry(
    frame,
    font=("Arial",14),
    width=25
)

name_entry.grid(
    row=0,
    column=1
)



tk.Label(
    frame,
    text="Phone",
    font=("Arial",14),
    bg="#1E1E1E",
    fg="white"
).grid(row=1,column=0,pady=5)


phone_entry = tk.Entry(
    frame,
    font=("Arial",14),
    width=25
)

phone_entry.grid(
    row=1,
    column=1
)



tk.Label(
    frame,
    text="Email",
    font=("Arial",14),
    bg="#1E1E1E",
    fg="white"
).grid(row=2,column=0,pady=5)


email_entry = tk.Entry(
    frame,
    font=("Arial",14),
    width=25
)

email_entry.grid(
    row=2,
    column=1
)



# ---------------- Buttons ----------------

button_frame = tk.Frame(
    root,
    bg="#1E1E1E"
)

button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="Add Contact",
    font=("Arial",12,"bold"),
    width=15,
    command=add_contact
).grid(row=0,column=0,padx=5)


tk.Button(
    button_frame,
    text="Delete",
    font=("Arial",12,"bold"),
    width=15,
    command=delete_contact
).grid(row=0,column=1,padx=5)



tk.Button(
    button_frame,
    text="Clear",
    font=("Arial",12,"bold"),
    width=15,
    command=clear_fields
).grid(row=1,column=0,padx=5,pady=10)


tk.Button(
    button_frame,
    text="Show All",
    font=("Arial",12,"bold"),
    width=15,
    command=show_all
).grid(row=1,column=1,padx=5,pady=10)



# ---------------- Search ----------------

search_frame = tk.Frame(
    root,
    bg="#1E1E1E"
)

search_frame.pack(pady=10)


search_entry = tk.Entry(
    search_frame,
    font=("Arial",14),
    width=25
)

search_entry.grid(
    row=0,
    column=0
)


tk.Button(
    search_frame,
    text="Search",
    font=("Arial",12,"bold"),
    command=search_contact
).grid(
    row=0,
    column=1,
    padx=5
)



# ---------------- Contact List ----------------

contact_list = tk.Listbox(
    root,
    font=("Arial",14),
    width=45,
    height=10
)

contact_list.pack(
    pady=20
)



# ---------------- Run ----------------

root.mainloop()