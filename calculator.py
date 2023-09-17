# SIMPLE CALCULATOR
# USING TKINTER IN PYTHON

from tkinter import*
root=Tk()
root.geometry('400x300')
root.resizable(0,0)
root.title("Calculator")
root.configure(background="gold",relief="groove")

# FUNCTIONS

def show(op):
    a.set(a.get()+op)

def eql():
    exp = a.get()
    a.set(eval(exp))

def clear():
    a.set(" ")

# ENTRY BOX

a=StringVar()
ent=Entry(root,justify='right',font = ('Arial',25),textvariable = a)
ent.place(x = 10, y = 245,width =370,height = 50)

# BUTTONS 
#CHANGE COLOURS AS PER YOUR WISH

but7=Button(root, text='7', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
but7.place(x=10 ,y=10 , width=70 , height= 40 )
but7.configure(command = lambda: show('7'))

but4=Button(root, text='4', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
but4.place(x=10 ,y=70, width=70 , height= 40 )
but4.configure(command = lambda: show('4'))

but1=Button(root, text='1', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
but1.place(x=10 ,y=130, width=70 , height= 40 )
but1.configure(command = lambda: show('1'))

butC=Button(root, text='C', font=('Ariel',20), activebackground='gray', bg='red', fg='white')
butC.place(x=10 ,y=187, width=70 , height= 50 )
butC.configure(command = clear )

but8=Button(root, text='8', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
but8.place(x=110 ,y=10 , width=70 , height= 40 )
but8.configure(command = lambda: show('8'))

but5=Button(root, text='5', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
but5.place(x=110 ,y=70 , width=70 , height= 40 )
but5.configure(command = lambda: show('5'))

but2=Button(root, text='2', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
but2.place(x=110 ,y=130 , width=70 , height= 40 )
but2.configure(command = lambda: show('2'))

but9=Button(root, text='9', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
but9.place(x=210 ,y=10 , width=70 , height= 40 )

butP=Button(root, text='+', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
butP.place(x=310 ,y=10 , width=70 , height= 80 )
butP.configure(command = lambda: show('+'))

but6=Button(root, text='6', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
but6.place(x=210 ,y=70 , width=70 , height= 40 )
but6.configure(command = lambda: show('6'))

but3=Button(root, text='3', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
but3.place(x=210 ,y=130 , width=70 , height= 40 )
but3.configure(command = lambda: show('3'))

butM=Button(root, text='-', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
butM.place(x=310 ,y=105 , width=70 , height= 60 )
butM.configure(command = lambda: show('-'))

butEq=Button(root, text='=', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
butEq.place(x=310 ,y=180 , width=70 , height= 60 )
butEq.configure(command = eql)

butMu=Button(root, text='x', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
butMu.place(x=210 ,y=187 , width=70 , height= 50 )
butMu.configure(command = lambda: show('*'))

butD=Button(root, text='/', font=('Ariel',20), activebackground='gray', bg='lime green', fg='black')
butD.place(x=110 ,y=187 , width=70 , height= 50 )
butD.configure(command = lambda: show('/'))

root.mainloop()

#THANKYOU!
