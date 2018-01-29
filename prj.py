from Tkinter import *
import sqlite3
from tkMessageBox import *
import time
import datetime


def fp2():
    #w1.destroy()
    def show():
        print 9
        con=sqlite3.Connection('varsTech')
        cur=con.cursor()
        cur.execute("create table IF NOT EXISTS vars(ecode number primary key,efname varchar(20),elname varchar(20))")
        x=eid.get()
        print x
        #x=int(x)
        cur.execute("select * from vars where ecode=(?)",(x,))
        con.commit()
        a=cur.fetchall()
        cur.execute("select * from vars")
        q=cur.fetchall()
        j=0
        
        b = (",".join([str(i[0]) for i in a]))
        print b
        c = (",".join([str(i[1]) for i in a]))
        print c
        d = (",".join([str(i[2]) for i in a]))
        print d
        cur.execute("select * from prj where ecode=(?)",(x,))
        con.commit()
        w=cur.fetchall()
        cur.execute("select * from prj")
        q=cur.fetchall()
        j=0
        print 'w',w
        print 'q',q
        
        x = (",".join([str(i[0]) for i in q]))
        print x
        y = (",".join([str(i[1]) for i in q]))
        print y
        z = (",".join([str(i[2]) for i in q]))
        print z
        e = (",".join([str(i[3]) for i in q]))
        print 'e'
        print e
        s=e.split('-')
        s.reverse()
        print s
        f = (",".join([str(i[4]) for i in q]))
        print f
        Label(w2,text='Employee Id :',font=('arial',16,'bold'),bd=10,bg="old lace",fg="black").place(relx=.2,rely=.40,anchor=CENTER)
        Label(w2,text='                                  ',font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.5,rely=.40,anchor=CENTER)

        Label(w2,text=b,font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.5,rely=.40,anchor=CENTER)

        Label(w2,text='Employee Name: ',font=('arial',16,'bold'),bd=10,bg="old lace",fg="black").place(relx=.2,rely=.5,anchor=CENTER)
        Label(w2,text='                                  ',font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.5,rely=.5,anchor=CENTER)
        Label(w2,text=(c+' '+d),font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.5,rely=.5,anchor=CENTER)
        #Label(w2,text='Employee Last Name  : ',font=('arial',16,'bold'),bd=10,bg="old lace",fg="black").place(relx=.2,rely=.6,anchor=CENTER)
        #Label(w2,text=d,font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.5,rely=.6,anchor=CENTER)
        Label(w2,text='Current project ID  : ',font=('arial',16,'bold'),bd=10,bg="old lace",fg="black").place(relx=.2,rely=.6,anchor=CENTER)
        Label(w2,text='                                  ',font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.5,rely=.6,anchor=CENTER)
        Label(w2,text=x,font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.5,rely=.6,anchor=CENTER)
        Label(w2,text='Current project name  : ',font=('arial',16,'bold'),bd=10,bg="old lace",fg="black").place(relx=.2,rely=.7,anchor=CENTER)
        Label(w2,text='                                  ',font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.6,rely=.7,anchor=CENTER)
        Label(w2,text=y,font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.6,rely=.7,anchor=CENTER)
        Label(w2,text='Last date of completion : ',font=('arial',16,'bold'),bd=10,bg="old lace",fg="black").place(relx=.2,rely=.8,anchor=CENTER)
        Label(w2,text='                                  ',font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.6,rely=.8,anchor=CENTER)
        Label(w2,text=s[0]+'-'+s[1]+'-'+s[2],font=('arial',16,'bold'),bd=10,bg="light sky blue",fg="black").place(relx=.6,rely=.8,anchor=CENTER)
        #print len(q)
        
    def showall():
        con=sqlite3.Connection('varsTech')
        cur=con.cursor()
        cur.execute("create table IF NOT EXISTS vars(ecode number primary key,efname varchar(20),elname varchar(20))")
        x=eid.get()
        cur.execute("select * from vars");
        con.commit()
        a=cur.fetchall()
        #print [str(i[0]) for i in a]
        j=0
        sa=Tk()
        sa.minsize(width=466, height=466)
        sa.maxsize(width=466, height=466)
        Label(sa,text='    ',font='times 14 bold').grid(row=0,column=0)
        while j < len(a):
            b = [int(i[0]) for i in a]
            b= str(b[j])
            c = [str(i[1]) for i in a]
            c=str(c[j])
            d = [str(i[2]) for i in a]
            d=str(d[j])
            
            Label(sa,text='eid : '+b+'   efname : '+c+'   elname : '+d,font='times 14 bold').grid(row=j,column=1)
            j=j+1

    w2=Tk()
    w2.minsize(width=666, height=766)
    w2.maxsize(width=666, height=766)
    Label(w2,text='').grid(row=0)
    Label(w2,text='Enter your id to see details',font=('arial',16,'bold'),bd=10,bg="azure",fg="black").place(relx=.3,rely=.10,anchor=CENTER)
    #Label(w2,text='').grid(row=2)
    eid=Entry(w2,font=('arial',16,'bold'),bd=5,bg="pink",fg="black")
    eid.place(relx=.75,rely=.10,anchor=CENTER)
    #Label(w2,text='').grid(row=4)
    Button(w2,text='get details',font=('arial',12,'bold'),bd=5,bg="chocolate",fg="azure",command=show).place(relx=.45,rely=.25,anchor=CENTER)
    Button(w2,text='see all employee details',font=('arial',12,'bold'),bd=5,bg="chocolate",fg="azure",command=showall).place(relx=.75,rely=.25,anchor=CENTER)
def fp3():
    print 7



def fp4():
    def p(x):
        #x=str(x)
        print x
        con=sqlite3.Connection('VarsTech')
        cur=con.cursor()
        cur.execute("create table IF NOT EXISTS prj(pid varchar(20),pname varchar(20),sdate date,edate date,ecode number REFERENCES vars(ecode))")
        sd=datetime.date(int(psdy.get()), int(psdm.get()), int(psdd.get())) 
        ed=datetime.date(int(pedy.get()), int(pedm.get()),int(pedd.get()))   
        #sd=datetime.date(2007, 7, 7)
        #ed=datetime.date(2007, 8, 7)
        a=[(pid.get(),pname.get(),sd,ed,x)]
        cur.executemany("insert into prj values(?,?,?,?,?)",a)
        cur.execute("select * from prj")
        print cur.fetchall()
        con.commit()
    def co():
        showinfo('success','project created sucessfully')
        w3.destroy()
    def sel():
        def bb():
            showinfo('success','employee selected sucessfully')
            sll.destroy()
        con=sqlite3.Connection('varsTech')
        cur=con.cursor()
        cur.execute("select * from vars")
        con.commit()
        a=cur.fetchall()
        j=0
        #Checkbutton(w3,text='ytdtc',command=lambda:p(9)).place(relx=.4,rely=(.7+j),anchor=CENTER)
        sll=Tk()
        Label(sll,text='  ').grid(row=0,column=0)
        while j < len(a):
            print a
            b = [str(i[0]) for i in a]
            b= str(b[j])
            print b
            c = [str(i[1]) for i in a]
            c=str(c[j])
            d = [str(i[2]) for i in a]
            d=str(d[j])
            t=(b+'    '+c+' '+d)
            
            xx=b
            #print b
            Checkbutton(sll,text=b+'    '+c+' '+d,command=lambda:p(xx)).grid(row=1+j,column=1)
            j=j+1
        Button(sll,text='done!',font=('arial',12,'bold'),bd=5,bg="chocolate",fg="azure",command=bb).grid(row=j+1,column=1)
    #sel.destroy()
    w3=Tk()
    w3.minsize(width=666, height=466)
    w3.maxsize(width=666, height=466)
    Label(w3,text='Enter project id ',font=('arial',16,'bold'),bd=10,bg="pale green",fg="black").place(relx=.2,rely=.10,anchor=CENTER)
    Label(w3,text='Enter project name ',font=('arial',16,'bold'),bd=10,bg="pale green",fg="black").place(relx=.2,rely=.25,anchor=CENTER)
    Label(w3,text='Enter project start date ',font=('arial',16,'bold'),bd=10,bg="pale green",fg="black").place(relx=.2,rely=.4,anchor=CENTER)
    Label(w3,text='Enter project end date ',font=('arial',16,'bold'),bd=10,bg="pale green",fg="black").place(relx=.2,rely=.55,anchor=CENTER)
    Label(w3,text='select the employees ',font=('arial',16,'bold'),bd=10,bg="pale green",fg="black").place(relx=.2,rely=.7,anchor=CENTER)
    Button(w3,text='select employees',font=('arial',12,'bold'),bd=5,bg="chocolate",fg="azure",command=sel).place(relx=.75,rely=.7,anchor=CENTER)
    Button(w3,text='create project',font=('arial',16,'bold'),bd=5,bg="green",fg="black",command=co).place(relx=.5,rely=.9,anchor=CENTER)
    pid=Entry(w3,font=('arial',16,'bold'),bd=5,bg="pink",fg="black")
    pid.place(relx=.75,rely=.10,anchor=CENTER)
    pname=Entry(w3,font=('arial',16,'bold'),bd=5,bg="pink",fg="black")
    pname.place(relx=.75,rely=.25,anchor=CENTER)
    psdd=Entry(w3,font=('arial',16,'bold'),bd=5,bg="pink",fg="black")
    psdd.place(relx=.75,rely=.4,anchor=CENTER)
    psdm=Entry(w3,font=('arial',16,'bold'),bd=5,bg="pink",fg="black")
    psdm.place(relx=.88,rely=.4,anchor=CENTER)
    psdy=Entry(w3,font=('arial',16,'bold'),bd=5,bg="pink",fg="black")
    psdy.place(relx=1.01,rely=.4,anchor=CENTER)
    pedd=Entry(w3,font=('arial',16,'bold'),bd=5,bg="pink",fg="black")
    pedd.place(relx=.75,rely=.55,anchor=CENTER)
    pedm=Entry(w3,font=('arial',16,'bold'),bd=5,bg="pink",fg="black")
    pedm.place(relx=.88,rely=.55,anchor=CENTER)
    pedy=Entry(w3,font=('arial',16,'bold'),bd=5,bg="pink",fg="black")
    pedy.place(relx=1.01,rely=.55,anchor=CENTER)
    
def fp5():
    def insert():
        con=sqlite3.Connection('varsTech')
        cur=con.cursor()
        cur.execute("create table IF NOT EXISTS vars(ecode number primary key,efname varchar(20),elname varchar(20))")
        #print ecode.get()
        x=ecode.get()
        cur.execute("select * from vars where ecode=(?)",(x,))
        con.commit()
        a=cur.fetchall()
        print(len(a))
        if len(a)!=0:
            showerror('error','Employee Record Already Exist')
        else:    
            a=[(ecode.get(),efname.get(),elname.get())]
            cur.executemany("insert into vars values(?,?,?)",a)
            cur.execute("select * from vars")
            print cur.fetchall()
            con.commit()
            showinfo('success','Details Saved Sucessfully')
            w5.destroy()
    w5=Tk()
    w5.minsize(width=666, height=466)
    w5.maxsize(width=666, height=466)
    #Label(w5,text='',font='times 10 bold italic').grid(row=0,column=0)
    #Label(w5,text='',font='times 10 bold').grid(row=1)
    Label(w5,text='Enter emp Code ',font=('arial',16,'bold'),bd=10,bg="pale green",fg="black").place(relx=.2,rely=.10,anchor=CENTER)
    #Label(w5,text='',font='times 10 bold').grid(row=3)
    Label(w5,text='Enter first name: ',font=('arial',16,'bold'),bd=10,bg="pale green",fg="black").place(relx=.2,rely=.25,anchor=CENTER)
    Label(w5,text='',font='times 10 bold').grid(row=5)
    Label(w5,text='Enter last name: ',font=('arial',16,'bold'),bd=10,bg="pale green",fg="black").place(relx=.2,rely=.4,anchor=CENTER)

    #Label(w5,text='',font='times 10 bold').grid(row=7)
    ecode=Entry(w5,font=('arial',16,'bold'),bd=4,bg="azure",fg="black")
    ecode.place(relx=.6,rely=.10,anchor=CENTER)
    efname=Entry(w5,font=('arial',16,'bold'),bd=4,bg="azure",fg="black")
    efname.place(relx=.6,rely=.25,anchor=CENTER)
    elname=Entry(w5,font=('arial',16,'bold'),bd=4,bg="azure",fg="black")
    elname.place(relx=.6,rely=.4,anchor=CENTER)
    #Label(w5,text='',font='times 10 bold').grid(row=9)
    Button(w5,text='insert',font=('arial',12,'bold'),bd=5,bg="chocolate",fg="azure",command=insert).place(relx=.5,rely=.6,anchor=CENTER)
def fp1():
    root.destroy()
    w1=Tk()
    w1.minsize(width=666, height=466)
    w1.maxsize(width=666, height=466)
    Label(w1,text='',font='times 16 bold').grid(row=0)
    Label(w1,text='VARS Tecs',font='times 24 bold').grid(row=1,columnspan=5)
    Label(w1,text='',font='times 10 bold').grid(row=2)
    Label(w1,text='For information about employees',font='times 14').grid(row=3,column=2)
    Label(w1,text='   ',font='times 10 bold').grid(row=2,column=3)
    Button(w1,text='get info',font='10',command=fp2).grid(row=3,column=4)
    Label(w1,text='  ',font='times 10 bold').grid(row=4)
    #Label(w1,text='For information about work progress',font='times 14').grid(row=5,column=2)
    #Label(w1,text='   ',font='times 10 bold').grid(row=5,column=3)
    #Button(w1,text='work progress',font='10',command=fp3).grid(row=5,column=4)
    #Label(w1,text='  ',font='times 10 bold').grid(row=6)
    Label(w1,text='create new project',font='times 14').grid(row=5,column=2)
    Label(w1,text='   ',font='times 10 bold').grid(row=5,column=3)
    Button(w1,text='create',font='10',command=fp4).grid(row=5,column=4)
    Label(w1,text='  ',font='times 10 bold').grid(row=6)
    Label(w1,text='create new employee account',font='times 14').grid(row=7,column=2)
    Label(w1,text='   ',font='times 10 bold').grid(row=7,column=3)
    Button(w1,text='create',font='10',command=fp5).grid(row=7,column=4)

root=Tk()
root.minsize(width=766, height=566)
root.maxsize(width=766, height=566)
icon=PhotoImage(file="bcd1.gif")
l1=Label(root,image=icon)
l1.pack()
Label(root,text='WELCOME',font=('arial',26,'bold'),bd=10,bg="light blue",fg="black").place(relx=.5,rely=.10,anchor=CENTER)
#Label(root,text='',font=('arial',26,'bold'),bd=10,bg="white",fg="black").place(relx=.5,rely=.20,anchor=CENTER)
Label(root,text='Rituraj Mishra',font=('arial',26,'bold'),bd=10,bg="white",fg="black").place(relx=.5,rely=.25,anchor=CENTER)
#Label(root,text='',font=('arial',26,'bold'),bd=10,bg="white",fg="black").place(relx=.5,rely=.10,anchor=CENTER)
Label(root,text='161B302',font=('arial',26,'bold'),bd=10,bg="white",fg="black").place(relx=.5,rely=.4,anchor=CENTER)
#Label(root,text='',font='times 10 bold italic').pack()
Label(root,text='Work Management System of Employees',font=('arial',26,'bold'),bd=10,bg="pink",fg="black").place(relx=.5,rely=.55,anchor=CENTER)
#Label(root,text='',font='times 10 bold italic').pack()
Label(root,text='Wait for 3 seconds',font=('arial',16,'bold'),bd=10,bg="purple",fg="black").place(relx=.5,rely=.7,anchor=CENTER)
root.after(3000,fp1)
#Button(root,text='proceed',font='16',command=fp1).pack()

root.mainloop()
