import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("ToDo List")
root.geometry("450x350")
tasks = []
custom_font = ("Verdana", 9, "bold")

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")
    txt_input.delete(0, "end")

def del_all():
    confirmed = messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
    if confirmed == True:
        global tasks
        tasks = []
        update_listbox()

def del_one():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

lbl_title = tk.Label(root, text="Enter your task", bg="white",font=custom_font)
lbl_title.pack()

txt_input = tk.Entry(root, width=40)
txt_input.pack(pady=6)

btn_add_task = tk.Button(root, text="Add task", fg="green", bg="white", command=add_task,font=custom_font,width=40)
btn_add_task.pack(pady=6)

btn_del_all = tk.Button(root, text="Delete All", fg="green", bg="white", command=del_all,font=custom_font,width=40)
btn_del_all.pack(pady=6)

btn_del_one = tk.Button(root, text="Delete", fg="green", bg="white", command=del_one,font=custom_font,width=40)
btn_del_one.pack(pady=6)

lb_tasks = tk.Listbox(root,width=55)
lb_tasks.pack()

root.mainloop()
