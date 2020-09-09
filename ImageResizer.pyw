# Importing required modules
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Storing UI settings in variables
bg_color = 'white'
button_color = '#4885ed'

# Creating window object
root = Tk()

# setting the window title
root.title('Image Resizer with Python')

# setting UI color and dimension
root.configure(bg=bg_color)
root.geometry('500x600')

# making window not resizable
root.resizable(0, 0)

# Initializing text variables for labels
label_file_path = StringVar()
label_file_path.set('File\'s path will appear here')

label_ouput_path = StringVar()
label_ouput_path.set('Output path will appear here')

# Initializing variables
file_name = ''
output = ''


# function for selecting a file from computer
def mfileopen():
    global file_name
    file_name = filedialog.askopenfile().name
    label_file_path.set(file_name)

# function for resizing image
def resize():
    im = Image.open(file_name)
    im1 = im
    try:
        im1 = im.resize((int(e1.get()), int(e2.get())))
    except:
        pass
    im1.save(os.path.join(output, e3.get()))
    messagebox.showinfo('Success', 'Image successfully resized')

# functoin for selecting output path
def output_path():
    global output
    output = filedialog.askdirectory()
    label_ouput_path.set(output)

# function for resetting all input fields and labels
def reset():
    label_file_path.set('File\'s path will appear here')
    label_ouput_path.set('Output path will appear here')
    e1.delete('0', 'end')
    e2.delete('0', 'end')
    e3.delete('0', 'end')


# Creating buttons and labels

b1 = Button(root, text = 'Choose file to resize', bg=button_color, fg='white', font=('Helvetica', 14),  command = mfileopen)
b1.place(x=250, y=50, anchor=CENTER, width=250)


l1 = Label(root,  textvariable = label_file_path, bg=bg_color, font=('Helvetica', 12))
l1.place(x=250, y=100, anchor=CENTER)

l2 = Label(root, bg=bg_color,  text = 'Enter width of output file', font=('Helvetica', 12))
l2.place(x=25, y=150)

e1 = Entry(root, bd=2, relief='groove', font=('Helvetica', 12))
e1.place(x=450, y=150, anchor=NE, width=150)

l2_1 = Label(root, bg=bg_color,  text = 'px', font=('Helvetica', 12))
l2_1.place(x=450, y=150, width=25)

l3 = Label(root, bg=bg_color,  text = 'Enter height of output file', font=('Helvetica', 12))
l3.place(x=25, y=200)

e2 = Entry(root, bd=2, relief='groove', font=('Helvetica', 12))
e2.place(x=450, y=200, anchor=NE, width=150)

l3_1 = Label(root, bg=bg_color,  text = 'px', font=('Helvetica', 12))
l3_1.place(x=450, y=200, width=25)


l4 = Label(root, bg=bg_color,  text = 'Enter output file\'s name with extension', font=('Helvetica', 12))
l4.place(x=25, y=250)

e3 = Entry(root, bd=2, relief='groove', font=('Helvetica', 12))
e3.place(x=475, y=250, anchor=NE, width=175)

b2 = Button(root, text = 'Choose output path',bg=button_color, fg='white', font=('Helvetica', 14), command = output_path)
b2.place(x=250, y=315, anchor=CENTER, width=250)


l5 = Label(root, bg=bg_color,  textvariable = label_ouput_path, font=('Helvetica', 12))
l5.place(x=250, y=365, anchor=CENTER)

b3 = Button(root, text = 'Resize',bg=button_color, fg='white', font=('Helvetica', 14), command = resize)
b3.place(x=250, y=415, anchor=CENTER, width=250)

b4 = Button(root, text = 'Reset',bg=button_color, fg='white', font=('Helvetica', 14), command = reset)
b4.place(x=250, y=515, anchor=CENTER, width=250)



root.mainloop()
