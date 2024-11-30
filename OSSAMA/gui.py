import tkinter as tk
from tkinter import messagebox
from adb_operations import get_devices, get_accounts, get_phone_number

def show_devices():
    devices = get_devices()
    if devices:
        device_list.delete(0, tk.END)
        for device in devices:
            device_list.insert(tk.END, device)
    else:
        messagebox.showwarning("No Devices", "No devices connected.")

def show_accounts():
    accounts = get_accounts()
    if accounts:
        accounts_text.delete(1.0, tk.END)
        for account in accounts:
            accounts_text.insert(tk.END, account + "\n")
    else:
        messagebox.showwarning("No Accounts", "No accounts found.")

def show_phone_number():
    phone_number = get_phone_number()
    messagebox.showinfo("Phone Number", phone_number)

# إعداد واجهة المستخدم
root = tk.Tk()
root.title("ADB Device Manager")

# الأزرار
btn_show_devices = tk.Button(root, text="Show Devices", command=show_devices)
btn_show_devices.pack(pady=10)

btn_show_accounts = tk.Button(root, text="Show Accounts", command=show_accounts)
btn_show_accounts.pack(pady=10)

btn_show_phone_number = tk.Button(root, text="Show Phone Number", command=show_phone_number)
btn_show_phone_number.pack(pady=10)

# قائمة الأجهزة المتصلة
device_list = tk.Listbox(root, height=6, width=35)
device_list.pack(pady=10)

# مربع نص لعرض الحسابات
accounts_text = tk.Text(root, height=6, width=35)
accounts_text.pack(pady=10)

root.mainloop()
