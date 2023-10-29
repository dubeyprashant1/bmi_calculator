import tkinter as tk

root = tk.Tk()
root.title("Vertical Scrollbar Example")

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a listbox and attach the scrollbar to it
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
for i in range(1, 101):
    listbox.insert(tk.END, f"Item {i}")
listbox.pack(side=tk.LEFT)

# Configure the scrollbar to scroll the listbox
scrollbar.config(command=listbox.yview)

root.mainloop()
