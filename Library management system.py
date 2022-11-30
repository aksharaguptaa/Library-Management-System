#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import*
import random
from datetime import datetime
import tkinter.messagebox


class Library:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='black')

       
        LibCardNo=StringVar()
        Name=StringVar()
        BookID=StringVar()
        NoOfDaysIssued=StringVar()
        DateOfIssue=StringVar()
        BookTitle=StringVar()
        LateFee=StringVar()
        DateOfReturn=StringVar()
        Author=StringVar()

        def iDelete():
            iReset()
            self.txtDisplayR.delete("1.0",END)

        def iReset():
           
            LibCardNo.set("")
            Name.set("")
            BookID.set("")
            NoOfDaysIssued.set("")
            DateOfIssue.set("")
            BookTitle.set("")
            LateFee.set("")
            DateOfReturn.set("")
            Author.set("")

           
           
        def iExit():
           
            iExit =tkinter.messagebox.askyesno ("Library Management System", "Are you sure, you want to exit?")
            if iExit>0:
                root.destroy()
                return

       
           
             
        def iReceipt():
           
            self.txtDisplayR.insert(END, 'ENROLLMENT NO.: \t\t'  +   LibCardNo.get()  + "\n")
            self.txtDisplayR.insert(END, 'NAME: \t\t'  +  Name.get()  + "\n")
            self.txtDisplayR.insert(END, 'BOOK ID: \t\t'  +  BookID.get()  + "\n")
            self.txtDisplayR.insert(END, 'BOOK TITLE: \t\t'  +   BookTitle.get()  + "\n")
            self.txtDisplayR.insert(END, 'DATE OF ISSUE: \t\t'  +   DateOfIssue.get()  + "\n")
            self.txtDisplayR.insert(END, 'DUE DATE: \t\t'  +   DateOfReturn.get()  + "\n")
            self.txtDisplayR.insert(END, 'LATE FEE: \t\t'  +    LateFee.get()  + "\n")
            self.txtDisplayR.insert(END, 'AUTHOR: \t\t'  +    Author.get() +  "\n\n\n")

                   
       
       
        #----------------------------------------------------Frame--------------------------------------------------------------
        

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1300, padx=20, bd=20, relief=SUNKEN, bg="dark blue")
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,width=42,font=('arial', 40,'bold'),text="\tLIBRARY MANAGEMENT SYSTEM\t",padx=5)
        self.lblTitle.grid()

        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE, bg="dark blue")
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1300, height=400, padx=20, relief=RIDGE, bg="dark blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE
                             , font=('arial', 18,'bold'), text="STUDENT'S DETAILS",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=500, height=200, padx=20, relief=RIDGE
                                   , font=('arial', 18,'bold'), text="LIST OF BOOKS",)
        DataFrameRIGHT.pack(side=RIGHT)
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')


        #-------------------------------------------------Widget----------------------------------------------------------------

        self.lblBookID = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="BOOK ID", padx=2, pady=2)
        self.lblBookID .grid(row=1, column=0, sticky=W)
        self.lblBookID = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = BookID, width =25)
        self.lblBookID .grid(row=1, column=1)

        self.lblLibraryCardNo =Label(DataFrameLEFT, font=('arial', 12,'bold'), text="ENROLLMENT NO. *",padx=2,pady=2)
        self.lblLibraryCardNo .grid(row=1, column=0,sticky=W)
        self.txtLibraryCardNO=Entry(DataFrameLEFT, font=('arial', 12,'bold'), textvariable = LibCardNo, width=25)
        self.txtLibraryCardNO.grid(row=1, column=1)

        self.lblBookTitle =Label(DataFrameLEFT, font=('arial', 12,'bold'), text="BOOK TITLE",padx=2,pady=2)
        self.lblBookTitle.grid(row=1, column=2,sticky=W)
        self.txtBookTitle=Entry(DataFrameLEFT, font=('arial', 12,'bold'),textvariable = BookTitle, width=25)
        self.txtBookTitle.grid(row=1, column=3)

        self.lblName =Label(DataFrameLEFT, font=('arial', 12,'bold'), text="NAME *",padx=2,pady=2)
        self.lblName.grid(row=3, column=0,sticky=W)
        self.txtName=Entry(DataFrameLEFT, font=('arial', 12,'bold'),textvariable = Name, width=25)
        self.txtName.grid(row=3, column=1)

        self.lblDateOfIssue =Label(DataFrameLEFT, font=('arial', 12,'bold'), text="DATE OF ISSUE",padx=2,pady=2)
        self.lblDateOfIssue.grid(row=0, column=2,sticky=W)
        self.txtDateOfIssue=Entry(DataFrameLEFT,font=('arial', 12,'bold'),textvariable = DateOfIssue, width=25)
        self.txtDateOfIssue.grid(row=0, column=3)

        self.lblLateFee =Label(DataFrameLEFT, font=('arial', 12,'bold'), text="LATE FEE",padx=2,pady=2)
        self.lblLateFee.grid(row=3, column=2,sticky=W)
        self.txtLateFee=Entry(DataFrameLEFT,font=('arial', 12,'bold'),textvariable = LateFee, width=25)
        self.txtLateFee.grid(row=3, column=3)

        self.lblBookId =Label(DataFrameLEFT, font=('arial', 12,'bold'), text="BOOK ID",padx=2,pady=2)
        self.lblBookId.grid(row=4, column=0,sticky=W)
        self.txtBookId=Entry(DataFrameLEFT,font=('arial', 12,'bold'),textvariable = BookID, width=25)
        self.txtBookId.grid(row=4, column=1)

        self.lblDateOfReturn =Label(DataFrameLEFT, font=('arial', 12,'bold'), text="DUE DATE",padx=2,pady=2)
        self.lblDateOfReturn.grid(row=4, column=2,sticky=W)
        self.txtDateOfReturn=Entry(DataFrameLEFT,font=('arial', 12,'bold'),textvariable = DateOfReturn, width=25)
        self.txtDateOfReturn.grid(row=4, column=3)

        self.lblNoOfDaysIssued =Label(DataFrameLEFT, font=('arial', 12,'bold'), text="NO. OF DAYS ISSUED",padx=2,pady=2)
        self.lblNoOfDaysIssued.grid(row=5, column=0,sticky=W)
        self.txtNoOfDaysIssued=Entry(DataFrameLEFT,font=('arial', 12,'bold'),textvariable = NoOfDaysIssued, width=25)
        self.txtNoOfDaysIssued.grid(row=5, column=1)
       
        self.lblAuthor =Label(DataFrameLEFT, font=('arial', 12,'bold'), text="AUTHOR",padx=2,pady=2)
        self.lblAuthor.grid(row=5, column=2,sticky=W)
        self.txtAuthor=Entry(DataFrameLEFT,font=('arial', 12,'bold'),textvariable = Author,width=25)
        self.txtAuthor.grid(row=5, column=3)
        
        
        #============================================widget=====================================================
        
        
        self.txtDisplayR=Text(DataFrameRIGHT,font=('arial', 12,'bold'),width=47, height=13,padx=8,pady=20)
        self.txtDisplayR.grid(row=0, column=2)
        
        

        #======================================Listbox============================================================
       

        ListOfBooks = ['1.  Mastering in C++','2.  Korth Book of DBMS','3.  Programming with C','4.  Hello India','5.  Let Us C','6.  OOPS in C++',
                       '7.  Textbook of Optics', '8.  Probability and Statistics','9.  Concepts Of Physics','10.  AI Super Powers','11.  Introduction to Algorithms','12.  Textbook of Computer Science','13.  Python Programming']



        def SelectedBook(evt):
            value =str(booklist.get(booklist.curselection()))
            w = value

            if (w == "1.  Mastering in C++"):
                BookID.set("ISBN 11223344")
                BookTitle.set("Mastering in C++")
                Author.set("Paul Parker")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()

                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)

       
            elif (w == "2.  Korth Book of DBMS"):
               
                 BookID.set("ISBN 12223344")
                 BookTitle.set("Korth Book of DBMS")
                 Author.set("RD Sharma")
                 NoOfDaysIssued.set(14)
                 LateFee.set("Rs.50")
                 iReceipt()
                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=14)
                 d3 = (d1 + d2)
                 DateOfIssue.set(d1)
                 DateOfReturn.set(d3)

            elif (w == "3.  Programming with C"):
                 BookID.set("ISBN 13223344")
                 BookTitle.set("Programming with C")
                 Author.set("Charles Dickens")
                 NoOfDaysIssued.set(14)
                 LateFee.set("Rs.50")
                 iReceipt()
                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=14)
                 d3 = (d1 + d2)
                 DateOfIssue.set(d1)
                 DateOfReturn.set(d3)
            elif (w == "4.  Hello India"):
               
                BookID.set("ISBN 14223344")
                BookTitle.set("Hello India")
                Author.set("Rahul Pandit")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)

            elif (w == "5.  Let Us C"):
               
                BookID.set("ISBN 15223344")
                BookTitle.set("Let Us C")
                Author.set("The Brothers")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)

            elif (w == "6.  OOPS in C++"):
               
                BookID.set("ISBN 16223344")
                BookTitle.set("OOPS in C++")
                Author.set("Dr.SP.Jauhar")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)

            elif (w == "7.  Textbook of Optics"):
               
                BookID.set("ISBN 17223344")
                BookTitle.set("Textbook of Optics")
                Author.set("SL Arora")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)

            elif (w == "8.  Probability and Statistics"):
               
                BookID.set("ISBN 18223344")
                BookTitle.set("Probability and Statistics")
                Author.set("JK Rowling")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)

            elif (w == "9.  Concepts Of Physics"):
               
                BookID.set("ISBN 19223344")
                BookTitle.set("Concepts Of Physics")
                Author.set("HC Verma")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)

            elif (w == "10.  AI Super Powers"):
               
                BookID.set("ISBN 20223344")
                BookTitle.set("AI Super Powers")
                Author.set("Andy Mangles")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)

            elif (w == "11.  Introduction to Algorithms"):
               
                BookID.set("ISBN 21223344")
                BookTitle.set("Introduction to Algorithms")
                Author.set("Twinkle Khanna")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)

            elif (w == "12.  Textbook of Computer Science"):
               
                BookID.set("ISBN 22223344")
                BookTitle.set("Textbook of Computer Science")
                Author.set("APJ Abdul ")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)

            elif (w == "13.  Python Programming"):
               
                BookID.set("ISBN 23223344")
                BookTitle.set("Python Programming")
                Author.set("RJ Palacio")
                NoOfDaysIssued.set(14)
                LateFee.set("Rs.50")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateOfIssue.set(d1)
                DateOfReturn.set(d3)






               
           

           
       
        booklist = Listbox(DataFrameRIGHT, width=30, height=12,font=('arial', 12,'bold'))
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)
       
        for items in ListOfBooks:
            booklist.insert(END,items)



       
        #======================================Button============================================================


        self.btnDelete=Button(ButtonFrame, text= 'Delete',font=('arial', 12,'bold'), width=30, bd=4,command=iDelete )
        self.btnDelete.grid(row=0,column=1)

        self.btnReset=Button(ButtonFrame, text= 'Reset',font=('arial', 12,'bold'), width=30, bd=4, command=iReset)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame, text= 'Exit',font=('arial', 12,'bold'),width=30, bd=4, command=iExit )
        self.btnExit.grid(row=0,column=3)



 

       
       
   

if __name__ =='__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()


# In[ ]:




