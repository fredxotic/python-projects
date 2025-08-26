from tkinter import Label, Tk
import time

app = Tk()  
app.title("🕒Digital Clock")  
app.geometry("300x100")  
app.resizable(False, False)  
app.configure(bg='black')
 
clock_label = Label(app, font=('Helvetica', 40), bg='black', fg='cyan', relief='flat')  
clock_label.pack(padx=20, pady=20)

def update_clock():  
    current_time = time.strftime('%H:%M:%S')  
    clock_label.config(text=current_time)  
    clock_label.after(1000, update_clock) 

update_clock()  
app.mainloop()  