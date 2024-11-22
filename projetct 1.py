import tkinter as tk 
window = tk.Tk()

fahren_var = tk.StringVar()
Lbl_celsius = tk.StringVar()

def Temp_fahren():
    fahren = int(fahren_var.get())
    celsius = (fahren - 32) * 5/9
    Lbl_celsius['text'] = celsius
    fahren_var.set("")


Entry_temp = tk.Entry(textvariable=fahren_var)
Lbl_temp = tk.Label(text='°F')
temp_button = tk.Button(text='------>',command=Temp_fahren)
Lbl_celsius = tk.Label()

Entry_temp.grid(row=0,column=1)
Lbl_temp.grid(row=0,column=2)
temp_button.grid(row=0,column=3)
Lbl_celsius.grid(row=0,column=4)

window.mainloop()