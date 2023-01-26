import requests
import tkinter
from tkinter import messagebox
try:
   response = requests.get('https://www.google.com')
   if response.status_code == 200:
      tkinter.messagebox.showinfo(title="Internet test",message="Internet is working.")
   else:
      tkinter.messagebox.showwarning(title="Internet test",message="Internet is working but might have some issue.")
except:
   tkinter.messagebox.showerror(title="Internet test",message="Internet is dead.")