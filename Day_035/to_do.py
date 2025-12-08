import tkinter as tk

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = tk.Tk()
root.title("To-Do List")

root.geometry("300x400")  # optional
root.config(padx=10, pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(fill="x", padx=5, pady=5)

add_btn = tk.Button(root, text="Add Task", font=("Arial", 12),
                    command=add_task)
add_btn.pack(fill="x", padx=5)
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, pady=10)

scroll = tk.Scrollbar(frame)
scroll.pack(side="right", fill="y")

listbox = tk.Listbox(
    frame,
    font=("Arial", 14),
    yscrollcommand=scroll.set,
    selectmode=tk.SINGLE
)
listbox.pack(fill="both", expand=True)
scroll.config(command=listbox.yview)

del_btn = tk.Button(root, text="Delete Selected", font=("Arial", 12),
                    bg="#f19494", command=delete_task)
del_btn.pack(fill="x", padx=5, pady=5)

root.mainloop()
