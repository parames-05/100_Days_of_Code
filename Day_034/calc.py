import tkinter as tk

def button_click(value):
    current = display.get()

    if value == "=":
        try:
            result = str(eval(current))
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    elif value == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, value)


root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, font=("Arial", 20), borderwidth=5, justify="right")
display.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="we")
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]

row = 1
col = 0

for button in buttons:
    tk.Button(
        root,
        text=button,
        width=5,
        height=2,
        font=("Arial", 16),
        command=lambda b=button: button_click(b)
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(
    root,
    text="C",
    width=5,
    height=2,
    font=("Arial", 16),
    bg="#f19494",
    command=lambda: button_click("C")
).grid(row=row, column=0, columnspan=4, sticky="we", padx=5, pady=5)

root.mainloop()
