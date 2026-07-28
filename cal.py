import tkinter as tk

# ---------------- Window ----------------
root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.resizable(False, False)
root.configure(bg="#1E1E1E")

expression = ""

# ---------------- Display ----------------
display = tk.Entry(
    root,
    font=("Arial", 24),
    bd=8,
    relief="sunken",
    justify="right"
)
display.grid(row=0, column=0, columnspan=4,
             padx=10, pady=15, sticky="nsew")

# ---------------- Functions ----------------
def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(0, expression)


def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        expression = ""


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def backspace():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
    display.insert(0, expression)


# ---------------- Buttons ----------------
buttons = [
    ("C", clear), ("⌫", backspace), ("%", lambda: press("%")), ("/", lambda: press("/")),
    ("7", lambda: press("7")), ("8", lambda: press("8")), ("9", lambda: press("9")), ("*", lambda: press("*")),
    ("4", lambda: press("4")), ("5", lambda: press("5")), ("6", lambda: press("6")), ("-", lambda: press("-")),
    ("1", lambda: press("1")), ("2", lambda: press("2")), ("3", lambda: press("3")), ("+", lambda: press("+")),
    ("0", lambda: press("0")), (".", lambda: press(".")), ("=", equal)
]

row = 1
col = 0

for text, command in buttons:
    if text == "=":
        btn = tk.Button(
            root,
            text=text,
            command=command,
            font=("Arial", 18, "bold"),
            bg="#4CAF50",
            fg="white"
        )
        btn.grid(row=row, column=col, columnspan=2,
                 sticky="nsew", padx=4, pady=4)
        col += 2
    else:
        btn = tk.Button(
            root,
            text=text,
            command=command,
            font=("Arial", 18)
        )
        btn.grid(row=row, column=col,
                 sticky="nsew", padx=4, pady=4)
        col += 1

    if col > 3:
        col = 0
        row += 1

# ---------------- Responsive Grid ----------------
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for i in range(7):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()