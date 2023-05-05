import tkinter as tk
import time

def clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(100, clock)

root = tk.Tk()
root.title("Reloj Digital")
root.configure(background='black')

label = tk.Label(root, font=("Helvetica", 40, "bold"), bg="black", fg="red")
label.pack(fill="both", expand=1)

clock()

root.mainloop()
