import os
from tkinter import *
import datetime

# ... (the rest of your code remains unchanged)

# Adding a task into the file and displaying it***start
def addTask():
    global taskname
    global duedate
    global new_display_frame_row
    taskname = taskEntry.get()
    # getting dates
    duedate = duedateEntry.get()
    dueDate_inp = duedate.split("-")
    day, month, year = (int(item) for item in dueDate_inp)
    dueDate = datetime.datetime(year, month, day)
    dateFormat = ("Due;", dueDate.strftime('%a'), dueDate.strftime('%B'), dueDate.strftime('%d'), ",", dueDate.strftime('%Y'))
    f = (f"taskname:{taskname} {dateFormat}")
    prod_list.append(f)

    # Check if the file exists, if not, create it
    if not os.path.exists(path):
        open(path, 'w').close()

    # saving into a file
    with open(path, "w") as file:
        for task in prod_list:
            file.write(task + "\n")

    # displaying the tasks in a new frame
    new_display_frame = LabelFrame(maintaskFrame)
    new_display_frame.grid(row=new_display_frame_row, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

    displaytaskname_label = Label(new_display_frame, text=taskname, font=20)
    displaytaskname_label.grid(row=0, column=1)

    displaytaskdue_label = Label(new_display_frame, text=dateFormat, font=20)
    displaytaskdue_label.grid(row=1, column=1)

    # Checkbox to mark completed
    var = IntVar()
    check_box = Checkbutton(new_display_frame, variable=var, font=15)
    check_box.grid(row=0, column=0, rowspan=2)

    # buttons for task manipulation
    # space bgn
    comp_button = Label(new_display_frame, text="                            ")
    comp_button.grid(row=0, column=2, rowspan=2, )

    comp_button = Label(new_display_frame, text="                            ")
    comp_button.grid(row=0, column=3, rowspan=2)

    comp_button = Label(new_display_frame, text="                            ")
    comp_button.grid(row=0, column=4, rowspan=2)
    # space bgn

    edit_botton = Button(new_display_frame, text='Edit', font=15, command=editTask)
    edit_botton.grid(row=0, column=5, rowspan=2)
    # space
    comp_button = Label(new_display_frame, text="     ")
    comp_button.grid(row=0, column=6, rowspan=2)

    del_button = Button(new_display_frame, text='Delete', font=15, command=lambda frame=new_display_frame: deleteTask(frame))
    del_button.grid(row=0, column=7, rowspan=2)
    new_display_frame_row += 1  # Increment the row for the next frame
    taskEntry.delete(0, END)
    duedateEntry.delete(0, END)
