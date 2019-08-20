from Tkinter import*
from tkMessageBox import*
import random
from datetime import datetime
root1=Tk()
root1.title('Camlin Stationery Management System')
Label(root1,text='Camlin Stationery Management System',relief='ridge',font='times 60 bold',bg='yellow').grid(row=0,column=0)
a=PhotoImage(file='image1.gif')
Label(root1,image=a).grid(row=1,column=0,padx=20,pady=20)
def fun():
   
    root4=Tk()
    root4.title('Camlin Stationery Mnagement System: Orders')
    root4.configure(background='light green')
    f2=Frame(root4,width=460,height=600,bd=5,relief='ridge',bg='red')
    f2.grid(row=0,column=0)

    f3=Frame(root4,width=460,height=600,bd=5,relief='ridge',bg='red')
    f3.grid(row=0,column=1)

    f5=Frame(root4,width=460,height=800,bd=5,relief='ridge',bg='yellow')
    f5.grid(row=0,column=2)

    f4=Frame(root4,width=1300,height=100,bd=5,relief='ridge',bg='blue')
    f4.grid(row=1,column=0,columnspan=2)
    def close():
        close=askyesno('Exit system','Do you want to Exit ?')
        if close>0:
            root4.destroy()
            return
    def ref():
        x=random.randint(20987,45987)
        randomRef=str(x)
        refe.set(randomRef)

        v1 =int(pencil.get())
        v2 =int(pen.get())
        v3 =int(eraser.get())
        v4 =int(scale.get())
        v5 =int(sharpner.get())
        v6 =int(a4sheet.get())
        v7 =int(large.get())
        v8 =int(medium.get())
        v9 =int(small.get())
        v10 =int(files.get())
        v11  =int(dbook.get())
        v12 =int(dsheet.get())
        v13 =int(gbox.get())
        v14 =int(pbox.get())
        v15 =int(wcolor.get())
        v16 =int(sketch.get())
        v17 =int(crayon.get())
        v18 =int(pcolor.get())
        v19 =int(board.get())
        v20 =int(brush.get())
        v21 =int(stapler.get())
        v22 =int(pin.get())
        v23 =int(glue.get())
        v24 =int(tape.get())

        c1=v1 * 28
        c2=v2 * 5
        c3=v3 * 3
        c4=v4 * 5
        c5=v5 * 3
        c6=v6 * 1
        c7=v7 * 60
        c8=v8 * 45
        c9=v9 * 20
        c10=v10 * 10
        c11=v11 * 25
        c12=v12 * 7
        c13=v13 * 150
        c14=v14 * 80
        c15=v15 * 50
        c16=v16 * 70
        c17=v17 * 45
        c18=v18 * 90
        c19=v19 * 110
        c20=v20 * 10
        c21=v21 * 40
        c22=v22 * 70
        c23=v23 * 75
        c24=v24 * 55

        ccost=(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24)
        ctax=((c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24)*0.12)
        cpay=(ctax+(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24))
        
        cost.set(ccost)
        tax.set(ctax)
        pay.set(cpay)


    
    def reset():
        
        pencil.set("0")
        pen.set("0")
        eraser.set("0")
        sharpner.set("0")
        scale.set("0")
        a4sheet.set("0")
        large.set("0")
        medium.set("0")
        small.set("0")
        files.set("0")
        dbook.set("0")
        dsheet.set("0")
        gbox.set("0")
        pbox.set("0")
        wcolor.set("0")
        sketch.set("0")
        crayon.set("0")
        pcolor.set("0")
        board.set("0")
        brush.set("0")
        stapler.set("0")
        pin.set("0")
        glue.set("0")
        tape.set("0")
        cost.set("0")
        tax.set("0")
        pay.set("0")
        refe.set("")

        text.delete('1.0',END)
    
    def calc():
         root5=Tk()
         root5.title('my calculator')
         e=Entry(root5,width=16,bd=5,font='times 30 bold',justify='right')
         e.grid(row=0,column=0,columnspan=4)
         def insert(x):
            e.insert(16,x)
         def result():
             y=eval(e.get())
             e.delete(0,END)
             e.insert(16,y)
         def clear():
             e.delete(0,END)
         Button(root5,text='9',width=10,height=5,bd=3,command=lambda:insert(9)).grid(row=1,column=0)
         Button(root5,text='8',width=10,height=5,bd=3,command=lambda:insert(8)).grid(row=1,column=1)
         Button(root5,text='7',width=10,height=5,bd=3,command=lambda:insert(7)).grid(row=1,column=2)
         Button(root5,text='C',width=10,height=5,bd=3,command=clear).grid(row=1,column=3)
         Button(root5,text='6',width=10,height=5,bd=3,command=lambda:insert(6)).grid(row=2,column=0)
         Button(root5,text='5',width=10,height=5,bd=3,command=lambda:insert(5)).grid(row=2,column=1)
         Button(root5,text='4',width=10,height=5,bd=3,command=lambda:insert(4)).grid(row=2,column=2)
         Button(root5,text='+',width=10,height=5,bd=3,command=lambda:insert('+')).grid(row=2,column=3)
         Button(root5,text='3',width=10,height=5,bd=3,command=lambda:insert(3)).grid(row=3,column=0)
         Button(root5,text='2',width=10,height=5,bd=3,command=lambda:insert(2)).grid(row=3,column=1)
         Button(root5,text='1',width=10,height=5,bd=3,command=lambda:insert(1)).grid(row=3,column=2)
         Button(root5,text='-',width=10,height=5,bd=3,command=lambda:insert('-')).grid(row=3,column=3)
         Button(root5,text='0',width=10,height=5,bd=3,command=lambda:insert(0)).grid(row=4,column=0)
         Button(root5,text='*',width=10,height=5,bd=3,command=lambda:insert('*')).grid(row=4,column=1)
         Button(root5,text='=',width=10,height=5,bd=3,command=result).grid(row=4,column=2)
         Button(root5,text='/',width=10,height=5,bd=3,command=lambda:insert('/')).grid(row=4,column=3)
         root5.mainloop()

    
    pencil=StringVar()
    pen=StringVar()
    eraser=StringVar()
    sharpner=StringVar()
    scale=StringVar()
    a4sheet=StringVar()
    large=StringVar()
    medium=StringVar()
    small=StringVar()
    files=StringVar()
    dbook=StringVar()
    dsheet=StringVar()
    gbox=StringVar()
    pbox=StringVar()
    wcolor=StringVar()
    sketch=StringVar()
    crayon=StringVar()
    pcolor=StringVar()
    board=StringVar()
    brush=StringVar()
    stapler=StringVar()
    pin=StringVar()
    glue=StringVar()
    tape=StringVar()
    cost=StringVar()
    tax=StringVar()
    pay=StringVar()
    refe=StringVar()

    pencil.set("0")
    pen.set("0")
    eraser.set("0")
    sharpner.set("0")
    scale.set("0")
    a4sheet.set("0")
    large.set("0")
    medium.set("0")
    small.set("0")
    files.set("0")
    dbook.set("0")
    dsheet.set("0")
    gbox.set("0")
    pbox.set("0")
    wcolor.set("0")
    sketch.set("0")
    crayon.set("0")
    pcolor.set("0")
    board.set("0")
    brush.set("0")
    stapler.set("0")
    pin.set("0")
    glue.set("0")
    tape.set("0")
    cost.set("0")
    tax.set("0")
    pay.set("0")
    refe.set("")
        
    Label(f2,text='Item',font='times 15 bold').grid(row=0,column=0,sticky=W)
    Label(f2,text='Enter Quantity',font='times 15 bold').grid(row=0,column=1)

    Label(f3,text='Item',font='times 15 bold').grid(row=0,column=0,sticky=W)
    Label(f3,text='Enter Quantity',font='times 15 bold').grid(row=0,column=1)
    
    lpen=Label(f2,font=('arial',16),bg='red',text='Pen',anchor='w')
    lpen.grid(row=1,column=0,sticky= W)
    
    leraser=Label(f2,font=('arial',16),bg='red',text='Eraser',anchor='w')
    leraser.grid(row=2,column=0,sticky= W)
    
    lsharpner=Label(f2,font=('arial',16),bg='red',text='Sharpner',anchor='w')
    lsharpner.grid(row=3,column=0,sticky= W)
    
    lscale=Label(f2,font=('arial',16),bg='red',text='Scale',anchor='w')
    lscale.grid(row=4,column=0,sticky= W)

    la4sheet=Label(f2,font=('arial',16),bg='red',text='A4Sheet',anchor='w')
    la4sheet.grid(row=5,column=0,sticky= W)

    llarge=Label(f2,font=('arial',16),bg='red',text='Large Notebook',anchor='w')
    llarge.grid(row=6,column=0,sticky= W)

    lmedium=Label(f2,font=('arial',16),bg='red',text='Medium Notebook',anchor='w')
    lmedium.grid(row=7,column=0,sticky= W)

    lsmall=Label(f2,font=('arial',16),bg='red',text='Small Notebook',anchor='w')
    lsmall.grid(row=8,column=0,sticky= W)

    lfiles=Label(f2,font=('arial',16),bg='red',text='Files',anchor='w')
    lfiles.grid(row=9,column=0,sticky= W)

    ldbook=Label(f2,font=('arial',16),bg='red',text='Drawing Book',anchor='w')
    ldbook.grid(row=10,column=0,sticky= W)

    ldsheet=Label(f2,font=('arial',16),bg='red',text='Drawing Sheet',anchor='w')
    ldsheet.grid(row=11,column=0,sticky= W)

    lgbox=Label(f2,font=('arial',16),bg='red',text='Geometry Box',anchor='w')
    lgbox.grid(row=12,column=0,sticky= W)

    lpbox=Label(f2,font=('arial',16),bg='red',text='Pencil box',anchor='w')
    lpbox.grid(row=13,column=0,sticky= W)

    lpencil=Label(f2,font=('arial',16),bg='red',text='Pencil',anchor='w')
    lpencil.grid(row=14,column=0,sticky= W)

    lsketch=Label(f3,font=('arial',16),bg='red',text='Sketch Pen',anchor='w')
    lsketch.grid(row=1,column=0,sticky= W)

    lcrayon=Label(f3,font=('arial',16),bg='red',text='Crayon',anchor='w')
    lcrayon.grid(row=2,column=0,sticky= W)

    lpcolor=Label(f3,font=('arial',16),bg='red',text='Pencil Colour',anchor='w')
    lpcolor.grid(row=3,column=0,sticky= W)

    lboard=Label(f3,font=('arial',16),bg='red',text='Exam Board',anchor='w')
    lboard.grid(row=4,column=0,sticky= W)

    lbrush=Label(f3,font=('arial',16),bg='red',text='Paint Brush',anchor='w')
    lbrush.grid(row=5,column=0,sticky= W)

    lstapler=Label(f3,font=('arial',16),bg='red',text='Stapler',anchor='w')
    lstapler.grid(row=6,column=0,sticky= W)

    lpin=Label(f3,font=('arial',16),bg='red',text='Stapler Pin',anchor='w')
    lpin.grid(row=7,column=0,sticky= W)

    lglue=Label(f3,font=('arial',16),bg='red',text='Glue',anchor='w')
    lglue.grid(row=8,column=0,sticky= W)

    ltape=Label(f3,font=('arial',16),bg='red',text='Tape',anchor='w')
    ltape.grid(row=9,column=0,sticky= W)

    lwcolor=Label(f3,font=('arial',16),bg='red',text='Water Colour',anchor='w')
    lwcolor.grid(row=10,column=0,sticky= W)

    lcost=Label(f3,font=('arial',16),bg='yellow',text='Cost(INR)',anchor='w')
    lcost.grid(row=11,column=0,sticky= W)

    ltax=Label(f3,font=('arial',16),bg='yellow',text='Tax(INR)',anchor='w')
    ltax.grid(row=12,column=0,sticky= W)
    
    lpay=Label(f3,font=('arial',16),bg='yellow',text='Payment(INR)',anchor='w')
    lpay.grid(row=13,column=0,sticky= W)

    lrefe=Label(f3,font=('arial',16),bg='yellow',text='Reference No.',anchor='w')
    lrefe.grid(row=14,column=0,sticky= W)

    tpen=Entry(f2,font=('arial',16),textvariable=pen,bd=5,insertwidth=4,justify='right')
    tpen.grid(row=1,column=1)

    teraser=Entry(f2,font=('arial',16),textvariable=eraser,bd=5,insertwidth=4,justify='right')
    teraser.grid(row=2,column=1)


    tsharpner=Entry(f2,font=('arial',16),textvariable=sharpner,bd=5,insertwidth=4,justify='right')
    tsharpner.grid(row=3,column=1)

    tscale=Entry(f2,font=('arial',16),textvariable=scale,bd=5,insertwidth=4,justify='right')
    tscale.grid(row=4,column=1)

    ta4sheet=Entry(f2,font=('arial',16),textvariable=a4sheet,bd=5,insertwidth=4,justify='right')
    ta4sheet.grid(row=5,column=1)

    tlarge=Entry(f2,font=('arial',16),textvariable=large,bd=5,insertwidth=4,justify='right')
    tlarge.grid(row=6,column=1)

    tmedium=Entry(f2,font=('arial',16),textvariable=medium,bd=5,insertwidth=4,justify='right')
    tmedium.grid(row=7,column=1)

    tsmall=Entry(f2,font=('arial',16),textvariable=small,bd=5,insertwidth=4,justify='right')
    tsmall.grid(row=8,column=1)

    tfiles=Entry(f2,font=('arial',16),textvariable=files,bd=5,insertwidth=4,justify='right')
    tfiles.grid(row=9,column=1)

    tdbook=Entry(f2,font=('arial',16),textvariable=dbook,bd=5,insertwidth=4,justify='right')
    tdbook.grid(row=10,column=1)

    tdsheet=Entry(f2,font=('arial',16),textvariable=dsheet,bd=5,insertwidth=4,justify='right')
    tdsheet.grid(row=11,column=1)

    tgbox=Entry(f2,font=('arial',16),textvariable=gbox,bd=5,insertwidth=4,justify='right')
    tgbox.grid(row=12,column=1)

    tpbox=Entry(f2,font=('arial',16),textvariable=pbox,bd=5,insertwidth=4,justify='right')
    tpbox.grid(row=13,column=1)

    tpencil=Entry(f2,font=('arial',16),textvariable=pencil,bd=5,insertwidth=4,justify='right')
    tpencil.grid(row=14,column=1)


    

    tsketch=Entry(f3,font=('arial',16),textvariable=sketch,bd=5,insertwidth=4,justify='right')
    tsketch.grid(row=1,column=1)

    tcrayon=Entry(f3,font=('arial',16),textvariable=crayon,bd=5,insertwidth=4,justify='right')
    tcrayon.grid(row=2,column=1)

    tpcolor=Entry(f3,font=('arial',16),textvariable=pcolor,bd=5,insertwidth=4,justify='right')
    tpcolor.grid(row=3,column=1)

    tboard=Entry(f3,font=('arial',16),textvariable=board,bd=5,insertwidth=4,justify='right')
    tboard.grid(row=4,column=1)

    tbrush=Entry(f3,font=('arial',16),textvariable=brush,bd=5,insertwidth=4,justify='right')
    tbrush.grid(row=5,column=1)

    tstapler=Entry(f3,font=('arial',16),textvariable=stapler,bd=5,insertwidth=4,justify='right')
    tstapler.grid(row=6,column=1)

    tpin=Entry(f3,font=('arial',16),textvariable=pin,bd=5,insertwidth=4,justify='right')
    tpin.grid(row=7,column=1)

    tglue=Entry(f3,font=('arial',16),textvariable=glue,bd=5,insertwidth=4,justify='right')
    tglue.grid(row=8,column=1)

    ttape=Entry(f3,font=('arial',16),textvariable=tape,bd=5,insertwidth=4,justify='right')
    ttape.grid(row=9,column=1)

    twcolor=Entry(f3,font=('arial',16),textvariable=wcolor,bd=5,insertwidth=4,justify='right')
    twcolor.grid(row=10,column=1)

    tcost=Entry(f3,font=('arial',16),textvariable=cost,bd=5,insertwidth=4,justify='right')
    tcost.grid(row=11,column=1)

    ttax=Entry(f3,font=('arial',16),textvariable=tax,bd=5,insertwidth=4,justify='right')
    ttax.grid(row=12,column=1)

    tpay=Entry(f3,font=('arial',16),textvariable=pay,bd=5,insertwidth=4,justify='right')
    tpay.grid(row=13,column=1)

    trefe=Entry(f3,font=('arial',16),textvariable=refe,bd=5,insertwidth=4,justify='right')
    trefe.grid(row=14,column=1)

    
    Label(f5,text='Camlin Store Receipt',font='times 20 bold underline',bd=2).grid(row=0,column=0)

    text=Text(f5,width=59,height=33,bd=8,bg='yellow',font=('arial',11,'bold'))
    text.grid(row=1,column=0)
   
    def receipt():
        c=str(datetime.now())
        text.delete("1.0",END)
        text.insert(END,'Reference No.:\t\t\t\t'+refe.get()+'\n')
        text.insert(END,'Date-Time of order:\t\t\t\t'+c+'\n\n')
        text.insert(END,'Item:\t\t\t\tNumber \n')
        text.insert(END,'No. of Pencil(28):\t\t\t\t'+pencil.get()+'\n')
        text.insert(END,'No. of Pen(5):\t\t\t\t'+pen.get()+'\n')
        text.insert(END,'No. of Eraser(3):\t\t\t\t'+eraser.get()+'\n')
        text.insert(END,'No. of Sharpner(5):\t\t\t\t'+sharpner.get()+'\n')
        text.insert(END,'No. of Scale(3):\t\t\t\t'+scale.get()+'\n')
        text.insert(END,'No. of A4Sheet(1):\t\t\t\t'+a4sheet.get()+'\n')
        text.insert(END,'No. of Large Notebook(60):\t\t\t\t'+large.get()+'\n')
        text.insert(END,'No. of Medium Notebook(45):\t\t\t\t'+medium.get()+'\n')
        text.insert(END,'No. of Small Notebook(20):\t\t\t\t'+small.get()+'\n')
        text.insert(END,'No. of Files(10):\t\t\t\t'+files.get()+'\n')
        text.insert(END,'No. of Drawing Book(25):\t\t\t\t'+dbook.get()+'\n')
        text.insert(END,'No. of Drawing Sheet(7):\t\t\t\t'+dsheet.get()+'\n')
        text.insert(END,'No. of Geometry Box(150):\t\t\t\t'+gbox.get()+'\n')
        text.insert(END,'No. of Pencil Box(80):\t\t\t\t'+pbox.get()+'\n')
        text.insert(END,'No. of Water Colour(50):\t\t\t\t'+wcolor.get()+'\n')
        text.insert(END,'No. of SketchPen(70):\t\t\t\t'+sketch.get()+'\n')
        text.insert(END,'No. of Crayon(45):\t\t\t\t'+crayon.get()+'\n')
        text.insert(END,'No. of Pencil Colour(90):\t\t\t\t'+pcolor.get()+'\n')
        text.insert(END,'No. of Exam Board(110):\t\t\t\t'+board.get()+'\n')
        text.insert(END,'No. of Paint Brush(10):\t\t\t\t'+brush.get()+'\n')
        text.insert(END,'No. of Staple Pin(40):\t\t\t\t'+pin.get()+'\n')
        text.insert(END,'No. of Stapler(70):\t\t\t\t'+stapler.get()+'\n')
        text.insert(END,'No. of Glue(75):\t\t\t\t'+glue.get()+'\n')
        text.insert(END,'No. of Tape(55):\t\t\t\t'+tape.get()+'\n\n')
        text.insert(END,'Total Cost\t\t\t\t'+cost.get()+'\n')
        text.insert(END,'Tax(12%):\t\t\t\t'+tax.get()+'\n')
        text.insert(END,'Payment to be made:\t\t\t\t'+pay.get()+'\n')
        text.insert(END,'\t\tTHANKS FOR SHOPPING')
        
        
     
    Button(f4,text='Open Calculator',font='times 20 bold',bg='yellow',relief='raise',command=calc).grid(row=0,column=0)
    Button(f4,text=' Exit',font='times 20 bold',bg='yellow',relief='raise',command=close).grid(row=0,column=1)
    Button(f4,text='Total',font='times 20 bold',bg='yellow',relief='raise',command=ref).grid(row=0,column=2)
    Button(f4,text='Reset',font='times 20 bold',bg='yellow',relief='raise',command=reset).grid(row=0,column=3)
    Button(f4,text='Receipt',font='times 20 bold',bg='yellow',relief='raise',command=receipt).grid(row=0,column=4)
    root4.mainloop()

    
def start():
    root1.destroy()
    root=Tk()
    root.title('Camlin Stationery Management System')
    root.configure(background='green')
    b=PhotoImage(file='logo.gif')
    Label(root,image=b).grid(row=0,column=0,padx=300,pady=50)
    Label(root,text='"Welcome to the Store"',font='times 60 bold').grid(row=1,column=0,padx=20,pady=40)
    
    def menu():
        root.destroy()
        root2=Tk()
        root2.configure(background='light green')
        root2.title('Camlin Stationery Management System :Catalogue')
        Label(root2,text='Item',font='times 35 bold underline',bg='light green').grid(row=0,column=0,sticky=W)
        Label(root2,text='Pencil',font='times 20 ',bg='light green').grid(row=1,column=0,sticky=W)
        Label(root2,text='Pen',font='times 20 ',bg='light green').grid(row=2,column=0,sticky=W)
        Label(root2,text='Eraser',font='times 20 ',bg='light green').grid(row=3,column=0,sticky=W)
        Label(root2,text='Sharpner',font='times 20 ',bg='light green').grid(row=4,column=0,sticky=W)
        Label(root2,text='Scale',font='times 20 ',bg='light green').grid(row=5,column=0,sticky=W)
        Label(root2,text='A4 Sheet',font='times 20 ',bg='light green').grid(row=6,column=0,sticky=W)
        Label(root2,text='Large Notebook',font='times 20 ',bg='light green').grid(row=7,column=0,sticky=W)
        Label(root2,text='Medium Notebook',font='times 20 ',bg='light green').grid(row=8,column=0,sticky=W)
        Label(root2,text='Small Notebook',font='times 20 ',bg='light green').grid(row=9,column=0,sticky=W)
        Label(root2,text='Files',font='times 20 ',bg='light green').grid(row=10,column=0,sticky=W)
        Label(root2,text='Drawing Book',font='times 20 ',bg='light green').grid(row=11,column=0,sticky=W)
        Label(root2,text='Tape',font='times 20 ',bg='light green').grid(row=12,column=0,sticky=W)
        Label(root2,text='Item',font='times 35 bold underline',bg='light green').grid(row=0,column=3,sticky=W,padx=200)
        Label(root2,text='Drawing Sheets',font='times 20 ',bg='light green').grid(row=1,column=3,sticky=W,padx=200)
        Label(root2,text='Geometry Box',font='times 20 ',bg='light green').grid(row=2,column=3,sticky=W,padx=200)
        Label(root2,text='Pencil Box',font='times 20 ',bg='light green').grid(row=3,column=3,sticky=W,padx=200)
        Label(root2,text='Water Colour',font='times 20 ',bg='light green').grid(row=4,column=3,sticky=W,padx=200)
        Label(root2,text='Sketch Pen',font='times 20 ',bg='light green').grid(row=5,column=3,sticky=W,padx=200)
        Label(root2,text='Crayon',font='times 20 ',bg='light green').grid(row=6,column=3,sticky=W,padx=200)
        Label(root2,text='Pencil Colour',font='times 20 ',bg='light green').grid(row=7,column=3,sticky=W,padx=200)
        Label(root2,text='Exam Board',font='times 20 ',bg='light green').grid(row=8,column=3,sticky=W,padx=200)
        Label(root2,text='Paint Brush',font='times 20 ',bg='light green').grid(row=9,column=3,sticky=W,padx=200)
        Label(root2,text='Staple Pins',font='times 20 ',bg='light green').grid(row=10,column=3,sticky=W,padx=200)
        Label(root2,text='Stapler',font='times 20 ',bg='light green').grid(row=11,column=3,sticky=W,padx=200)
        Label(root2,text='Glue',font='times 20 ',bg='light green').grid(row=12,column=3,sticky=W,padx=200)
      

        Label(root2,text='Price',font='times 35 bold underline',bg='light green').grid(row=0,column=1,sticky=W)
        Label(root2,text='28',font='times 20  ',bg='light green').grid(row=1,column=1,sticky=W)
        Label(root2,text='5',font='times 20 ',bg='light green').grid(row=2,column=1,sticky=W)
        Label(root2,text='3',font='times 20 ',bg='light green').grid(row=3,column=1,sticky=W)
        Label(root2,text='5',font='times 20 ',bg='light green').grid(row=4,column=1,sticky=W)
        Label(root2,text='3',font='times 20 ',bg='light green').grid(row=5,column=1,sticky=W)
        Label(root2,text='1',font='times 20 ',bg='light green').grid(row=6,column=1,sticky=W)
        Label(root2,text='60',font='times 20 ',bg='light green').grid(row=7,column=1,sticky=W)
        Label(root2,text='45',font='times 20 ',bg='light green').grid(row=8,column=1,sticky=W)
        Label(root2,text='20',font='times 20 ',bg='light green').grid(row=9,column=1,sticky=W)
        Label(root2,text='10',font='times 20 ',bg='light green').grid(row=10,column=1,sticky=W)
        Label(root2,text='25',font='times 20 ',bg='light green').grid(row=11,column=1,sticky=W)
        Label(root2,text='55',font='times 20 ',bg='light green').grid(row=12,column=1,sticky=W)
        Label(root2,text='Price',font='times 35 bold underline',bg='light green').grid(row=0,column=4,sticky=W)
        Label(root2,text='7',font='times 20 ',bg='light green').grid(row=1,column=4,sticky=W)
        Label(root2,text='150',font='times 20 ',bg='light green').grid(row=2,column=4,sticky=W)
        Label(root2,text='80',font='times 20 ',bg='light green').grid(row=3,column=4,sticky=W)
        Label(root2,text='50',font='times 20 ',bg='light green').grid(row=4,column=4,sticky=W)
        Label(root2,text='70',font='times 20 ',bg='light green').grid(row=5,column=4,sticky=W)
        Label(root2,text='45',font='times 20 ',bg='light green').grid(row=6,column=4,sticky=W)
        Label(root2,text='90',font='times 20 ',bg='light green').grid(row=7,column=4,sticky=W)
        Label(root2,text='110',font='times 20 ',bg='light green').grid(row=8,column=4,sticky=W)
        Label(root2,text='10',font='times 20 ',bg='light green').grid(row=9,column=4,sticky=W)
        Label(root2,text='40',font='times 20 ',bg='light green').grid(row=10,column=4,sticky=W)
        Label(root2,text='70',font='times 20 ',bg='light green').grid(row=11,column=4,sticky=W)
        Label(root2,text='75',font='times 20 ',bg='light green').grid(row=12,column=4,sticky=W)

        def order1():
           
            root2.destroy()
           
            fun()
            
        Button(root2,text='Click Here to Place Order',font='times 30 bold',bg='yellow',relief='raise',command=order1).grid(row=15,column=0,columnspan=4,pady=30)
        
        root2.mainloop()
    def order():
        root.destroy()
        
        fun()
       
   
    Button(root,text='Click to Go to Catalogue',font='times 30 bold',bg='yellow',relief='raise',command=menu).grid(row=2,column=0,padx=35,pady=40)
    Button(root,text='Click Here to Place Order',font='times 30 bold',bg='yellow',relief='raise',command=order).grid(row=3,column=0,padx=35,pady=20)
    root.mainloop()
Button(root1,text='Click Here to Start',font='times 20 bold',bg='red',command=start).grid(row=2,column=0,padx=10,pady=10)
Label(root1,text='Submitted by: Tarang Banzal      Er.No.:161B249',relief='ridge',font='times 30 bold',bg='yellow').grid(row=3,column=0,padx=15,pady=15)


root1.mainloop()
