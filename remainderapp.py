from tkinter import *
from plyer import notification
from tkinter import messagebox
import time


root = Tk()

root.title("Remainder")
root.geometry("600x300")
root.config(background="black")
root.resizable(0,0)

#get task details
def get_details():
    get_task = task_name.get()
    get_desc = task_desc.get()
    get_due = due.get()

    if get_task == "" or get_desc == "" or get_due == "":
      messagebox.showerror("Alert","Fill all the fields")
    else:
        times = int(float(get_due))
        minute_to_second = times*60
        messagebox.showinfo("Remainder set","Are you sure?")
        root.destroy()
        time.sleep(minute_to_second)

        notification.notify(title = get_task,
                            message = get_desc,
                            app_name = "notifier",
                            timeout = 10
        )
#task name
l1 = Label(root, text="Task Name")  
l1.place(x=30,y =80)

task_name = Entry(root, width="25")
task_name.place(x = 150, y = 80)

#task description
l2 = Label(root, text = "Task Description")
l2.place(x=30,y=110)

task_desc = Entry(root, width="55")
task_desc.place(x = 150, y = 110)

#remainder time
l3 = Label(root, text = "Set Time")
l3.place(x= 30, y= 140)

due = Entry(root, width="5")
due.place(x = 150, y = 140)

l4 = Label(root, text = "min")
l4.place(x= 185, y= 140)

done = Button(root,text = "Set Remainder", fg = "#ffffff" ,bg="blue", width="20", relief="raised",
              command = get_details)
done.place(x=180, y = 200)

root.mainloop()