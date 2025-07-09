import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyshorteners
import webbrowser

def shorten_url():
    url = url_entry.get().strip()

    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        result_var.set(short_url)
        copy_button.config(state="normal")
        open_button.config(state="normal")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        result_var.set("")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Short URL copied to clipboard!")

def open_url():
    webbrowser.open(result_var.get())

# Setup main window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f4f7")

style = ttk.Style()
style.configure("TButton", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))

# UI Elements
title_label = tk.Label(root, text="URL Shortener", font=("Arial", 18, "bold"), bg="#f0f4f7", fg="#333")
title_label.pack(pady=20)

url_entry = ttk.Entry(root, width=40)
url_entry.pack(pady=10)

shorten_button = ttk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 10), fg="blue", bg="#f0f4f7", cursor="hand2")
result_label.pack(pady=10)

# Buttons for extra actions
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state="disabled")
copy_button.pack(pady=5)

open_button = ttk.Button(root, text="Open URL", command=open_url, state="disabled")
open_button.pack(pady=5)

# Run the app
root.mainloop()

# this part is new
print("welcome")


print("RAJDEEP DAR PATHSHALA")


print("RDP")

