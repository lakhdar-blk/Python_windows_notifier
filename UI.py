from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview

from threading import Timer

from win10toast import ToastNotifier



def send_notification(notification, body, index):
    
    toast = ToastNotifier()

    toast.show_toast(
        notification,
        body,
        duration = 10,
        icon_path = "icon.ico",
        threaded = True,
    )

    notifications.delete(index)

def scheduler(hour, minutes, seconds, label, body, index):
    
    total_seconds = int(hour)*3600+int(minutes)*60+int(seconds)

    t = Timer(total_seconds, send_notification, [label, body, index])
    t.start()
    
def create_notification(window, notification_e, body_t, l_hour, l_minutes, l_seconds):
    
    label_txt   = notification_e.get()
    body_txt    = body_t.get("1.0",END)    
    l_hour      = l_hour.get()
    l_minutes   = l_minutes.get()
    l_seconds   = l_seconds.get()
    

    if(label_txt==''):
        
        messagebox.showerror("Error","Please fill required fields") 
        window.mainloop()

    elif (l_hour=='0' and l_minutes=='0' and l_seconds=='0'):
        messagebox.showerror("Error", "You must set the time") 
        window.mainloop()

    else:

        global index
        notifications.insert(parent='',index='end',iid=index,text='',
        values=(label_txt, l_hour+':'+l_minutes+':'+l_seconds))
        scheduler(l_hour, l_minutes, l_seconds, label_txt, body_txt, index)
        index += 1
        window.destroy()


def openwindow():

    newWindow = Toplevel(window)
    newWindow.geometry("400x400")
    newWindow.title("Add notification")
    newWindow.resizable(False, False) 

    notification_l = Label(newWindow, foreground="black",text="Label(*):", font=('Calibri 15 bold'))
    notification_l.place(x=40,y=20)
    
    notification_I = Entry(newWindow, width=29, font=("Helvetica", 15), borderwidth=0)
    notification_I.place(x=40,y=60)

    body_l = Label(newWindow, foreground="black",text="Body:", font=('Calibri 15 bold'))
    body_l.place(x=40,y=100)
    
    body_I = Text(newWindow, height = 4, width = 40, borderwidth=0)
    body_I.configure(font=("Calibri", 12))
    body_I.place(x=40,y=130)

    hour_l = Label(newWindow, foreground="black",text="Hour(*)", font=('Calibri 12 bold'))
    hour_l.place(x=40,y=220)
    hours = [x for x in range(13)]
    hour_I = Combobox(newWindow, width=5,values=hours)
    hour_I.current(0)
    hour_I.place(x=40,y=250)
    
    minute_l = Label(newWindow, foreground="black",text="Minutes(*)", font=('Calibri 12 bold'))
    minute_l.place(x=160,y=220)
    minutes = [x for x in range(60)]
    minutes = Combobox(newWindow, width=5,values=minutes)
    minutes.current(0)
    minutes.place(x=170,y=250)

    second_l = Label(newWindow, foreground="black",text="Seconds(*)", font=('Calibri 12 bold'))
    second_l.place(x=280,y=220)
    seconds = [x for x in range(60)]
    seconds = Combobox(newWindow, width=5,values=seconds)
    seconds.current(0)
    seconds.place(x=300,y=250)


    add_btn = Button(newWindow, text="Create", width=15, font=("Calibri", 15) ,bg="white", fg="Blue", borderwidth=0, cursor='hand2', command=lambda: create_notification(newWindow, notification_I, body_I, hour_I, minutes, seconds))
    add_btn.place(x=120,y=300)


def delete():

    try:
        selected_item = notifications.selection()[0]
        notifications.delete(selected_item)
    except:
        pass

def cancel_all():

    window.destroy()

if __name__=='__main__':

    index = 0

    window = tkinter.Tk()
    window.title("Notifier")
    window.geometry("400x500")
    window.configure(bg='#198BF4')
    #window.iconbitmap('logo.ico')
    window.resizable(False, False) 

    #bt_image = PhotoImage('')
    
    create_bt = Button(window, text="Create a notification", width=20, font=("Calibri", 15) ,bg="white", fg="Blue", borderwidth=0, cursor='hand2', command=openwindow)
    create_bt.place(x=100,y=50)

    label1 = Label(window, text="Notifications:", background='#198BF4' , foreground="white", font=('Calibri 15 bold'))
    label1.place(x=40,y=120)

    canvas1 = Canvas(window ,width=310, height=350,bg="white")
    canvas1.place(x=40,y=150)
    
    frame = Frame(canvas1)
    frame.pack()

    notifications = Treeview(frame)
    notifications['columns'] = ('Label', 'Time')
    notifications.column("#0", width=0, stretch=NO)
    notifications.column('Label', anchor=CENTER, width=180)
    notifications.column('Time', anchor=CENTER, width=140)
    notifications.heading("#0",text="",anchor=CENTER)
    notifications.heading("Label",text="Label",anchor=CENTER)
    notifications.heading("Time",text="Time",anchor=CENTER)
    notifications.pack()
    
    delete_nt = Button(window, text="Cancel All", width=10, font=("Calibri", 15) ,bg="white", fg="Blue", borderwidth=0, cursor='hand2', command=cancel_all)
    delete_nt.place(x=150,y=420)

    window.mainloop()