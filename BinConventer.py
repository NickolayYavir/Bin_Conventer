from tkinter import *
from tkinter.ttk import Combobox
#from PIL import Image, ImageTk
from tkinter import messagebox  

root = Tk()
#imgS = ImageTk.PhotoImage(Image.open("image.jpg"))
#root.iconbitmap(r'./icon.ico')
root.title("BIN CONVERTER")
root.geometry('210x190') #210x220
root.resizable(False, False) 
lbl = Label(root, text = "Input number", font=("Consolas", 12))
lbl2 = Label(root, text = "Result", font=("Consolas", 12))
lbl3 = Label(root, text = "XineZan", font=("Consolas", 10))
e = Entry(root, width=20)
selected = IntVar()
combo = Combobox(root, width=2)  
combo['values'] = ('0','0b','0o','0x')  
combo.current(0) 
#canvas = Canvas(root,width=210,height=90)
#imagesprite = canvas.create_image(100,30,image=imgS)

def Convert():

    try:

        i = e.get()

        if combo.get() == '0b': 
            i = int(i,2)
        elif combo.get() == '0o': 
            i = int(i,8)
        elif combo.get() == '0x':  
            i = int(i, 16)
        else:
            i = int(i)

        if selected.get() == 1: 
            l['text'] = ' '.join(str(i))
        elif selected.get() == 2:
            l['text'] = ' '.join(bin(i))
        elif selected.get() == 3:
            l['text'] = ' '.join(oct(i))
        elif selected.get() == 4:
            l['text'] = ' '.join(hex(i))
        else:
            l['text'] = ' '.join(str(i))

    except ValueError:
         messagebox.showerror('Error', 'Invalid Data')  

rad1 = Radiobutton(root, text='Int', value=1, variable=selected)
rad2 = Radiobutton(root, text='Bin', value=2, variable=selected)  
rad3 = Radiobutton(root, text='Oct', value=3, variable=selected) 
rad4 = Radiobutton(root, text='Hex', value=4, variable=selected) 
Button = Button(root, text="Convert", width=15, command = Convert)
l = Label(root, bg='black', fg='green', width=30)

lbl.grid(column=0, row=0, columnspan = 4)
combo.grid(column=0, row=1,sticky=W, padx=5,columnspan = 4)
e.grid(column=0, row=1,columnspan = 4) 
rad1.grid(column=0, row=2, pady = 8, padx = 4) 
rad2.grid(column=1, row=2, pady = 8, padx = 4) 
rad3.grid(column=2, row=2, pady = 8, padx = 4) 
rad4.grid(column=3, row=2, pady = 8, padx = 4) 
Button.grid(column=0, row=3,columnspan = 4) 
lbl2.grid(column=0, row=4,columnspan = 4) 
l.grid(column=0, row=5,columnspan = 4) 
lbl3.grid(column=0, row=6, columnspan = 4, sticky = E, pady = 5, padx = 10)
#canvas.grid(column=0, row=6,columnspan = 4, sticky = N)

root.mainloop()


