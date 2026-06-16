from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="#DCE3EA")
root.resizable(False, False)

expression = ""

display_frame = Frame(root, bg="white", bd=8, relief=RIDGE)
display_frame.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=10,
    sticky="nsew"
)

#history
history_label = Label(
    display_frame,
    text="",
    anchor="e",
    bg="white",
    fg="gray",
    font=("Arial", 12)
)
history_label.pack(fill="both", padx=5, pady=(5, 0))

# Main display label
display = Label(
    display_frame,
    text="",
    anchor="e",
    bg="white",
    fg="black",
    font=("Arial", 28)
)
display.pack(fill="both", padx=5, pady=(0, 5))


#operators 
def press(value):
    global expression
    expression += str(value)
    display.config(text=expression)


def clear():
    global expression
    expression = ""
    display.config(text="")
    history_label.config(text="")


def backspace():
    global expression
    expression = expression[:-1]
    display.config(text=expression)


def calculate():
    global expression

    try:
        calculation = expression
        result = eval(expression)

        if result == int(result):
            result = int(result)

        history_label.config(text=f"{calculation} =")
        display.config(text=result)

        expression = str(result)

    except ZeroDivisionError:
        display.config(text="Cannot divide by 0")
        history_label.config(text="")
        expression = ""

    except:
        display.config(text="Error")
        history_label.config(text="")
        expression = ""


number_color = "#AAB7C4"
operator_color = "#5B8FB9"
special_color = "#7D8CA3"
equal_color = "#2E5984"


#grid
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

buttons = [
    ("C", 1, 0, special_color, clear),
    ("⌫", 1, 1, special_color, backspace),
    ("/", 1, 2, operator_color, lambda: press("/")),
    ("*", 1, 3, operator_color, lambda: press("*")),

    ("7", 2, 0, number_color, lambda: press("7")),
    ("8", 2, 1, number_color, lambda: press("8")),
    ("9", 2, 2, number_color, lambda: press("9")),
    ("-", 2, 3, operator_color, lambda: press("-")),

    ("4", 3, 0, number_color, lambda: press("4")),
    ("5", 3, 1, number_color, lambda: press("5")),
    ("6", 3, 2, number_color, lambda: press("6")),
    ("+", 3, 3, operator_color, lambda: press("+")),

    ("1", 4, 0, number_color, lambda: press("1")),
    ("2", 4, 1, number_color, lambda: press("2")),
    ("3", 4, 2, number_color, lambda: press("3")),
    ("=", 4, 3, equal_color, calculate),
]

for text, row, col, color, command in buttons:
    Button(
        root,
        text=text,
        font=("Arial", 16, "bold"),
        bg=color,
        fg="white",
        bd=0,
        activebackground=color,
        command=command
    ).grid(
        row=row,
        column=col,
        padx=2,
        pady=2,
        sticky="nsew"
    )


Button(
    root,
    text="0",
    font=("Arial", 16, "bold"),
    bg=number_color,
    fg="white",
    bd=0,
    activebackground=number_color,
    command=lambda: press("0")
).grid(
    row=5,
    column=0,
    columnspan=2,
    padx=2,
    pady=2,
    sticky="nsew"
)

# Decimal button
Button(
    root,
    text=".",
    font=("Arial", 16, "bold"),
    bg=number_color,
    fg="white",
    bd=0,
    activebackground=number_color,
    command=lambda: press(".")
).grid(
    row=5,
    column=2,
    columnspan=2,
    padx=2,
    pady=2,
    sticky="nsew"
)

root.mainloop()

#RISHITA SARKAR 
#Pinnacle Labs Task for Python Development Internship
