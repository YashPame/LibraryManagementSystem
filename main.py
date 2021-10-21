from tkinter import *
from tkinter import messagebox
import mysql.connector


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Library Management System')
        self.root.geometry('1522x790+0+0')

        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Yash",
            database="yashlibrary"
        )
        self.mycursor = self.mydb.cursor()
        # ========================================================
        self.ABW_NameOfBookVariable = StringVar()
        self.ABW_BookIDVariable = StringVar()
        self.ABW_BookPriceVariable = StringVar()

        self.RBW_NameOfBookVariable = StringVar()
        self.RBW_BookIDVariable = StringVar()

        self.BS_TotalBooksVariable = StringVar()
        self.BS_BorrowedBooksVariable = StringVar()

        self.CB_BookNameVariable = StringVar()
        self.CB_BookIDVariable = StringVar()
        self.CB_BookDetailsVariable = StringVar()

        self.BBW_NameOfBookVariable = StringVar()
        self.BBW_BookIDVariable = StringVar()
        self.BBW_StudentNameVariable = StringVar()
        self.BBW_StudentIDVariable = StringVar()
        self.BBW_BorrowDateVariable = StringVar()

        self.RW_NameOfBookVariable = StringVar()
        self.RW_BookIDVariable = StringVar()
        self.RW_StudentNameVariable = StringVar()
        self.RW_StudentIDVariable = StringVar()
        self.RW_ReturnDateVariable = StringVar()

        self.FB_NameOfBookVariable = StringVar()
        # ========================================================

        HeadingLBL = Label(self.root, text="Yash Library", font='times 30 bold', border=5, relief=RIDGE)
        HeadingLBL.place(x=0, y=0, width=1522, height=60)

        BookBorrowFrame = LabelFrame(self.root, text="Book Borrowing Window", font='times 12 bold', bd=3, relief=RIDGE)
        BookBorrowFrame.place(x=10, y=70, width=400, height=400)

        BookReturnFrame = LabelFrame(self.root, text="Book Return Window", font='times 12 bold', bd=3, relief=RIDGE)
        BookReturnFrame.place(x=420, y=70, width=400, height=400)

        CheckBookStatusFrame = LabelFrame(self.root, text="Check Book Status", font='times 12 bold', bd=3, relief=RIDGE)
        CheckBookStatusFrame.place(x=830, y=70, width=400, height=400)

        BookStatusFrame = LabelFrame(self.root, text="Books Status", font='times 12 bold', bd=3, relief=RIDGE)
        BookStatusFrame.place(x=1240, y=70, width=272, height=120)

        AddBookFrame = LabelFrame(self.root, text="Add Book Window", font='times 12 bold', bd=3, relief=RIDGE)
        AddBookFrame.place(x=10, y=480, width=400, height=200)

        RemoveBookFrame = LabelFrame(self.root, text="Remove Book Window", font='times 12 bold', bd=3, relief=RIDGE)
        RemoveBookFrame.place(x=420, y=480, width=400, height=200)

        FindBookFrame = LabelFrame(self.root, text="Find Book", font='times 12 bold', bd=3, relief=RIDGE)
        FindBookFrame.place(x=1240, y=200, width=272, height=500)

        # ------------------------------ADD BOOK WINDOW------------------------------------------------------
        ABW_NameOfBookLBL = Label(AddBookFrame, text='Name of Book', font='times 12 bold', anchor=W)
        ABW_NameOfBookLBL.place(x=10, y=10, width=130, height=30)
        ABW_NameOfBookTXT = Entry(AddBookFrame, textvariable=self.ABW_NameOfBookVariable, font='times 12 bold')
        ABW_NameOfBookTXT.place(x=150, y=10, width=200, height=30)

        with open('BookID.txt', 'r') as f:
            self.AddBookid = f.read()
        self.ABW_BookIDVariable.set(self.AddBookid)

        ABW_BookIDLBL = Label(AddBookFrame, text='Book ID', font='times 12 bold', anchor=W)
        ABW_BookIDLBL.place(x=10, y=50, width=130, height=30)
        ABW_BookIDTXT = Entry(AddBookFrame, textvariable=self.ABW_BookIDVariable, font='times 12 bold')
        ABW_BookIDTXT.place(x=150, y=50, width=200, height=30)

        ABW_BookPriceLBL = Label(AddBookFrame, text='Price', font='times 12 bold', anchor=W)
        ABW_BookPriceLBL.place(x=10, y=90, width=130, height=30)
        ABW_BookPriceTXT = Entry(AddBookFrame, textvariable=self.ABW_BookPriceVariable, font='times 12 bold')
        ABW_BookPriceTXT.place(x=150, y=90, width=200, height=30)

        ABW_AddBookBTN = Button(AddBookFrame, text='Add Book', font='times 15 bold', bd=3, relief=RAISED,
                                command=self.AddBookBTN)
        ABW_AddBookBTN.place(x=10, y=130, width=350, height=40)

        # ------------------------------Remove BOOK WINDOW------------------------------------------------------
        RBW_NameOfBookLBL = Label(RemoveBookFrame, text='Name of Book', font='times 12 bold', anchor=W)
        RBW_NameOfBookLBL.place(x=10, y=10, width=130, height=30)
        RBW_NameOfBookTXT = Entry(RemoveBookFrame, textvariable=self.RBW_NameOfBookVariable, font='times 12 bold')
        RBW_NameOfBookTXT.place(x=150, y=10, width=200, height=30)

        RBW_BookIDLBL = Label(RemoveBookFrame, text='Book ID', font='times 12 bold', anchor=W)
        RBW_BookIDLBL.place(x=10, y=50, width=130, height=30)
        RBW_BookIDTXT = Entry(RemoveBookFrame, textvariable=self.RBW_BookIDVariable, font='times 12 bold')
        RBW_BookIDTXT.place(x=150, y=50, width=200, height=30)

        RBW_RemoveBookBTN = Button(RemoveBookFrame, text='Remove Book', font='times 15 bold', bd=3, relief=RAISED,
                                   command=self.RemoveBookBTN)
        RBW_RemoveBookBTN.place(x=10, y=130, width=350, height=40)

        # ------------------------------Book Status----------------------------------------------
        BS_TotalBooksLBL = Label(BookStatusFrame, text='Total Books', font='times 12 bold', anchor=W)
        BS_TotalBooksLBL.place(x=10, y=10, width=120, height=30)
        with open('TotalBooks.txt', 'r') as f:
            self.TotalBook = f.read()
        self.BS_TotalBooksVariable.set(self.TotalBook)
        BS_TotalBooksTXT = Label(BookStatusFrame, textvariable=self.BS_TotalBooksVariable, font='times 12 bold',
                                 relief=RIDGE, bd=3)
        BS_TotalBooksTXT.place(x=140, y=10, width=120, height=30)

        with open('BorrowedBooks.txt', 'r') as f:
            self.BorrowBook = f.read()
        self.BS_BorrowedBooksVariable.set(self.BorrowBook)
        BS_TotalBorrowedBooksLBL = Label(BookStatusFrame, text='Borrowed Books', font='times 12 bold', anchor=W)
        BS_TotalBorrowedBooksLBL.place(x=10, y=50, width=120, height=30)
        BS_TotalBorrowedBooksTXT = Label(BookStatusFrame, textvariable=self.BS_BorrowedBooksVariable,
                                         font='times 12 bold', relief=RIDGE, bd=3)
        BS_TotalBorrowedBooksTXT.place(x=140, y=50, width=120, height=30)

        # ------------------------------Find Book Frame----------------------------------------------
        FB_NameOfBookLBL = Label(FindBookFrame, text='Name of Book', font='times 12 bold', anchor=W)
        FB_NameOfBookLBL.place(x=10, y=10, width=130, height=30)
        FB_NameOfBookTXT = Entry(FindBookFrame, textvariable=self.FB_NameOfBookVariable, font='times 12 bold')
        FB_NameOfBookTXT.place(x=10, y=40, width=200, height=30)

        FB_FindBTN = Button(FindBookFrame, text='✔', font='times 12 bold', command=self.FindBookBTN)
        FB_FindBTN.place(x=220, y=40, width=40, height=30)

        self.FB_SimilarBookTXT = Text(FindBookFrame, font='times 12 bold', relief=RIDGE, bd=2)
        self.FB_SimilarBookTXT.place(x=10, y=80, width=247, height=390)

        Scroll = Scrollbar(self.FB_SimilarBookTXT)
        Scroll.pack(side=RIGHT, fill=Y)
        Scroll.config(command=self.FB_SimilarBookTXT.yview)
        self.FB_SimilarBookTXT.config(yscrollcommand=Scroll.set)

        # -------------------------------Book Borrowing Window------------------------------------------
        BBW_NameOfBookLBL = Label(BookBorrowFrame, text='Name of Book', font='times 12 bold', anchor=W)
        BBW_NameOfBookLBL.place(x=10, y=10, width=130, height=30)
        BBW_NameOfBookTXT = Entry(BookBorrowFrame, textvariable=self.BBW_NameOfBookVariable, font='times 12 bold')
        BBW_NameOfBookTXT.place(x=150, y=10, width=200, height=30)

        BBW_BookIDLBL = Label(BookBorrowFrame, text='Book ID', font='times 12 bold', anchor=W)
        BBW_BookIDLBL.place(x=10, y=50, width=130, height=30)
        BBW_BookIDTXT = Entry(BookBorrowFrame, textvariable=self.BBW_BookIDVariable, font='times 12 bold')
        BBW_BookIDTXT.place(x=150, y=50, width=200, height=30)

        BBW_StudentNameLBL = Label(BookBorrowFrame, text='Student Name', font='times 12 bold', anchor=W)
        BBW_StudentNameLBL.place(x=10, y=90, width=130, height=30)
        BBW_StudentNameTXT = Entry(BookBorrowFrame, textvariable=self.BBW_StudentNameVariable, font='times 12 bold')
        BBW_StudentNameTXT.place(x=150, y=90, width=200, height=30)

        BBW_StudentIDLBL = Label(BookBorrowFrame, text='Student ID', font='times 12 bold', anchor=W)
        BBW_StudentIDLBL.place(x=10, y=130, width=130, height=30)
        BBW_StudentIDTXT = Entry(BookBorrowFrame, textvariable=self.BBW_StudentIDVariable, font='times 12 bold')
        BBW_StudentIDTXT.place(x=150, y=130, width=200, height=30)

        BBW_BorrowDateLBL = Label(BookBorrowFrame, text='Borrow Date', font='times 12 bold', anchor=W)
        BBW_BorrowDateLBL.place(x=10, y=210, width=130, height=30)
        BBW_BorrowDateTXT = Entry(BookBorrowFrame, textvariable=self.BBW_BorrowDateVariable, font='times 12 bold')
        BBW_BorrowDateTXT.place(x=150, y=210, width=200, height=30)

        BBW_BorrowBookBTN = Button(BookBorrowFrame, text='Borrow Book', font='times 15 bold', bd=3, relief=RAISED,
                                   command=self.BorrowBookBTN)
        BBW_BorrowBookBTN.place(x=10, y=330, width=350, height=40)

        # -------------------------------Book Return Window------------------------------------------
        BRW_NameOfBookLBL = Label(BookReturnFrame, text='Name of Book', font='times 12 bold', anchor=W)
        BRW_NameOfBookLBL.place(x=10, y=10, width=130, height=30)
        BRW_NameOfBookTXT = Entry(BookReturnFrame, textvariable=self.RW_NameOfBookVariable, font='times 12 bold')
        BRW_NameOfBookTXT.place(x=150, y=10, width=200, height=30)

        BRW_BookIDLBL = Label(BookReturnFrame, text='Book ID', font='times 12 bold', anchor=W)
        BRW_BookIDLBL.place(x=10, y=50, width=130, height=30)
        BRW_BookIDTXT = Entry(BookReturnFrame, textvariable=self.RW_BookIDVariable, font='times 12 bold')
        BRW_BookIDTXT.place(x=150, y=50, width=200, height=30)

        BRW_StudentNameLBL = Label(BookReturnFrame, text='Student Name', font='times 12 bold', anchor=W)
        BRW_StudentNameLBL.place(x=10, y=90, width=130, height=30)
        BRW_StudentNameTXT = Entry(BookReturnFrame, textvariable=self.RW_StudentNameVariable, font='times 12 bold')
        BRW_StudentNameTXT.place(x=150, y=90, width=200, height=30)

        BRW_StudentIDLBL = Label(BookReturnFrame, text='Student ID', font='times 12 bold', anchor=W)
        BRW_StudentIDLBL.place(x=10, y=130, width=130, height=30)
        BRW_StudentIDTXT = Entry(BookReturnFrame, textvariable=self.RW_StudentIDVariable, font='times 12 bold')
        BRW_StudentIDTXT.place(x=150, y=130, width=200, height=30)

        BRW_ReturnDateLBL = Label(BookReturnFrame, text='Return Date', font='times 12 bold', anchor=W)
        BRW_ReturnDateLBL.place(x=10, y=210, width=130, height=30)
        BRW_ReturnDateTXT = Entry(BookReturnFrame, textvariable=self.RW_ReturnDateVariable, font='times 12 bold')
        BRW_ReturnDateTXT.place(x=150, y=210, width=200, height=30)

        BRW_ReturnBookBTN = Button(BookReturnFrame, text='Return Book', font='times 15 bold', bd=3, relief=RAISED,
                                   command=self.ReturnBookBTN)
        BRW_ReturnBookBTN.place(x=10, y=330, width=350, height=40)

        # ----------------------------------Check Book Status-------------------------------------------
        CBS_NameOfBookLBL = Label(CheckBookStatusFrame, text='Name of Book', font='times 12 bold', anchor=W)
        CBS_NameOfBookLBL.place(x=10, y=10, width=130, height=30)
        CBS_NameOfBookTXT = Entry(CheckBookStatusFrame, textvariable=self.CB_BookNameVariable, font='times 12 bold')
        CBS_NameOfBookTXT.place(x=150, y=10, width=200, height=30)

        CBS_BookIDLBL = Label(CheckBookStatusFrame, text='Book ID', font='times 12 bold', anchor=W)
        CBS_BookIDLBL.place(x=10, y=50, width=130, height=30)
        CBS_BookIDTXT = Entry(CheckBookStatusFrame, textvariable=self.CB_BookIDVariable, font='times 12 bold')
        CBS_BookIDTXT.place(x=150, y=50, width=200, height=30)

        self.CBS_BookInfoLBL = Text(CheckBookStatusFrame, font='times 12 bold', bd=2, relief=RIDGE)
        self.CBS_BookInfoLBL.place(x=10, y=90, width=340, height=230)

        Scroll = Scrollbar(self.CBS_BookInfoLBL)
        Scroll.pack(side=RIGHT, fill=Y)
        Scroll.config(command=self.CBS_BookInfoLBL.yview)
        self.CBS_BookInfoLBL.config(yscrollcommand=Scroll.set)

        CBS_CheckStatusBTN = Button(CheckBookStatusFrame, text='Check Book', font='times 15 bold', bd=3, relief=RAISED,
                                    command=self.CheckBookBTN)
        CBS_CheckStatusBTN.place(x=10, y=330, width=350, height=40)

        # ==========================================================================================================

        # ==========================================================================================================

        # ------------------------------Adding Book Process---------------------------------------------

    def AddBookBTN(self):
        ABW__BookName = self.ABW_NameOfBookVariable.get()
        ABW__BookID = self.ABW_BookIDVariable.get()
        ABW__BookPrice = self.ABW_BookPriceVariable.get()

        if ABW__BookName == '':
            messagebox.showerror('ERROR', 'Enter Book Name')
        elif ABW__BookPrice == '':
            messagebox.showerror('ERROR', 'Enter Book Price')
        elif ABW__BookID == '':
            messagebox.showerror('ERROR', 'Enter Book ID')
        else:
            FinalCheck = messagebox.askquestion('Add Book',
                                                f'Do you want to add Book\nBookName={ABW__BookName}\nBookID={ABW__BookID}\nBookPrice={ABW__BookPrice}')
            if FinalCheck == 'yes':
                sqlformula = "INSERT INTO librarybooks (BookName, BookID, BookPrice, BookStatus) VALUES (%s, %s, %s, %s)"
                Book = (ABW__BookName, ABW__BookID, ABW__BookPrice, 'UnBorrowed')

                self.mycursor.execute(sqlformula, Book)
                self.mydb.commit()

                with open('BookID.txt', 'r') as f1:
                    f1 = f1.read()
                with open('BookID.txt', 'w') as f:
                    f.write(str(int(f1) + 1))

                self.ABW_NameOfBookVariable.set('')
                self.ABW_BookIDVariable.set((int(f1) + 1))
                self.ABW_BookPriceVariable.set('')

                with open('TotalBooks.txt', 'r') as f1:
                    f1 = f1.read()
                with open('TotalBooks.txt', 'w') as f:
                    f.write(str(int(f1) + 1))
                self.BS_TotalBooksVariable.set(str((int(f1) + 1)))
                messagebox.showinfo('Success', 'Book Added Successfully')

            else:
                pass

    def RemoveBookBTN(self):
        RBW__BookName = self.RBW_NameOfBookVariable.get()
        RBW__BookID = self.RBW_BookIDVariable.get()

        if RBW__BookName == '':
            messagebox.showerror('ERROR', 'Enter Book Name')
        elif RBW__BookID == '':
            messagebox.showerror('ERROR', 'Enter Book ID')
        else:
            sql = f"SELECT * FROM librarybooks WHERE BookID={RBW__BookID} OR BookName='{RBW__BookName}'"

            self.mycursor.execute(sql)
            myresult = self.mycursor.fetchall()

            for r in myresult:
                FinalCheck = messagebox.askquestion('Confirmation', f'Are you sure to Remove this Book\n{r[0:2]}')
                if FinalCheck == 'yes':
                    if r[6] == 'Borrowed':
                        messagebox.showerror('ERROR', 'Book is Borrowed, Cant remove it')
                    else:
                        sql = f"DELETE FROM librarybooks WHERE BookID={r[1]} AND BookName='{r[0]}'"
                        self.mycursor.execute(sql)
                        self.mydb.commit()

                        with open('TotalBooks.txt', 'r') as f1:
                            f1 = f1.read()
                        with open('TotalBooks.txt', 'w') as f:
                            f.write(str(int(f1) - 1))
                        self.BS_TotalBooksVariable.set(str((int(f1) - 1)))

                        self.RBW_NameOfBookVariable.set('')
                        self.RBW_BookIDVariable.set('')
                        messagebox.showinfo('SUCCESS', 'Book Removed Successfully')

                else:
                    pass

    def CheckBookBTN(self):
        CB__BookName = self.CB_BookNameVariable.get()
        CB__BookID = self.CB_BookIDVariable.get()
        self.CBS_BookInfoLBL.delete(0.0, END)
        if CB__BookName == "" and CB__BookID != "":
            sql = f"SELECT * FROM librarybooks WHERE BookID={CB__BookID}"
            self.mycursor.execute(sql)
            myresult = self.mycursor.fetchall()
            for i in myresult:
                FinalDetails = f"--Book Name:{i[0]}\n  Book ID:{i[1]}\n  BookStatus:{i[6]}\n  BorrowDate:{i[5]}\n  Borrower Name&ID:{i[3]}, {i[4]}\n\n"
                self.CBS_BookInfoLBL.insert(INSERT, FinalDetails)
            self.CB_BookNameVariable.set('')
            self.CB_BookIDVariable.set('')
        elif CB__BookID == "" and CB__BookName != "":
            sql = f"SELECT * FROM librarybooks WHERE BookName='{CB__BookName}'"
            self.mycursor.execute(sql)
            myresult = self.mycursor.fetchall()
            for i in myresult:
                FinalDetails = f"--Book Name:{i[0]}\n  Book ID:{i[1]}\n  BookStatus:{i[6]}\n  BorrowDate:{i[5]}\n  Borrower Name&ID:{i[3]}, {i[4]}\n\n"
                self.CBS_BookInfoLBL.insert(INSERT, FinalDetails)
            self.CB_BookNameVariable.set('')
            self.CB_BookIDVariable.set('')
        elif CB__BookID != "" and CB__BookName != "":
            sql = f"SELECT * FROM librarybooks WHERE BookName='{CB__BookName}' AND BookID={CB__BookID}"
            self.mycursor.execute(sql)
            myresult = self.mycursor.fetchall()
            for i in myresult:
                FinalDetails = f"--Book Name:{i[0]}\n  Book ID:{i[1]}\n  BookStatus:{i[6]}\n  BorrowDate:{i[5]}\n  Borrower Name&ID:{i[3]}, {i[4]}\n\n "
                self.CBS_BookInfoLBL.insert(INSERT, FinalDetails)
            self.CB_BookNameVariable.set('')
            self.CB_BookIDVariable.set('')
        else:
            messagebox.showerror("ERROR", "Enter Valid Details")

    def BorrowBookBTN(self):
        BB__BookName = self.BBW_NameOfBookVariable.get()
        BB__BookID = self.BBW_BookIDVariable.get()
        BB__StudentName = self.BBW_StudentNameVariable.get()
        BB__StudentID = self.BBW_StudentIDVariable.get()
        BB__BorrowDate = self.BBW_BorrowDateVariable.get()

        if BB__BookName == "":
            messagebox.showerror('ERROR', 'Enter Book Name')
        elif BB__BookID == "":
            messagebox.showerror('ERROR', 'Enter Book ID')
        elif BB__StudentName == "":
            messagebox.showerror('ERROR', 'Enter Student Name')
        elif BB__StudentID == "":
            messagebox.showerror('ERROR', 'Enter Student ID')
        elif BB__BorrowDate == "":
            messagebox.showerror('ERROR', 'Enter Borrow Date')
        else:
            sql = f"SELECT * FROM librarybooks WHERE BookID={BB__BookID} OR BookName='{BB__BookName}'"

            self.mycursor.execute(sql)
            myresult = self.mycursor.fetchall()

            for r in myresult:
                FinalCheck = messagebox.askquestion('Confirmation', f'Are you sure to Borrow this Book\n{r[0:2]}')
                if FinalCheck == 'yes':
                    if r[6] == 'UnBorrowed':
                        bookStatus = 'Borrowed'
                        sql = f"UPDATE librarybooks SET StudentName='{BB__StudentName}' , StudentID='{BB__StudentID}', BorrowDate='{BB__BorrowDate}', BookStatus='{bookStatus}' WHERE BookName='{r[0]}' AND BookID='{r[1]}'"
                        self.mycursor.execute(sql)
                        self.mydb.commit()

                        with open('BorrowedBooks.txt', 'r') as f1:
                            f1 = f1.read()
                        with open('BorrowedBooks.txt', 'w') as f:
                            f.write(str(int(f1) + 1))
                        self.BS_BorrowedBooksVariable.set(str((int(f1) + 1)))

                        self.BBW_NameOfBookVariable.set('')
                        self.BBW_BookIDVariable.set('')
                        self.BBW_StudentNameVariable.set('')
                        self.BBW_StudentIDVariable.set('')
                        self.BBW_BorrowDateVariable.set('')
                        messagebox.showinfo('SUCCESS', 'Book Borrowed Successfully')
                    elif r[6] == 'Borrowed':
                        messagebox.showerror('ERROR', 'Book is already Borrowed\nCheck Book Status to know more')
                    else:
                        pass

    def ReturnBookBTN(self):
        RBW__BookName = self.RW_NameOfBookVariable.get()
        RBW__BookID = self.RW_BookIDVariable.get()
        RBW__StudentName = self.RW_StudentNameVariable.get()
        RBW__StudentID = self.RW_StudentIDVariable.get()
        RBW__ReturnDate = self.RW_ReturnDateVariable.get()

        if RBW__BookName == "":
            messagebox.showerror('ERROR', 'Enter Book Name')
        elif RBW__BookID == "":
            messagebox.showerror('ERROR', 'Enter Book ID')
        elif RBW__StudentName == "":
            messagebox.showerror('ERROR', 'Enter Student Name')
        elif RBW__BookName == "":
            messagebox.showerror('ERROR', 'Enter Student ID')
        elif RBW__ReturnDate == "":
            messagebox.showerror('ERROR', 'Enter Return Date')
        else:
            sql = f"SELECT * FROM librarybooks WHERE BookID={RBW__BookID} OR BookName='{RBW__BookName}'"

            self.mycursor.execute(sql)
            myresult = self.mycursor.fetchall()

            for r in myresult:
                FinalCheck = messagebox.askquestion('Confirmation', f'Are you sure to Return this Book\n{r[0:2]}')
                if FinalCheck == 'yes':
                    if r[6] == 'Borrowed' and r[4] == RBW__StudentID:
                        bookStatus = 'UnBorrowed'
                        StudentName = ""
                        StudentID = ""
                        BorrowDate = ""
                        sql = f"UPDATE librarybooks SET StudentName='{StudentName}' , StudentID='{StudentID}', BorrowDate='{BorrowDate}', BookStatus='{bookStatus}' WHERE BookName='{r[0]}' AND BookID='{r[1]}'"
                        self.mycursor.execute(sql)
                        self.mydb.commit()

                        with open('BorrowedBooks.txt', 'r') as f1:
                            f1 = f1.read()
                        with open('BorrowedBooks.txt', 'w') as f:
                            f.write(str(int(f1) - 1))
                        self.BS_BorrowedBooksVariable.set(str((int(f1) - 1)))

                        self.RW_NameOfBookVariable.set('')
                        self.RW_BookIDVariable.set('')
                        self.RW_StudentNameVariable.set('')
                        self.RW_StudentIDVariable.set('')
                        self.RW_ReturnDateVariable.set('')
                        messagebox.showinfo('SUCCESS', 'Book Returned Successfully')
                    elif r[6] == 'UnBorrowed':
                        messagebox.showerror('ERROR', 'Book is NOT Borrowed\nCheck Book Status to know more')
                    else:
                        pass

    def FindBookBTN(self):
        FB__BookName = self.FB_NameOfBookVariable.get()
        if FB__BookName == "":
            messagebox.showerror('ERROR', 'Enter Book Name')
        else:
            self.FB_SimilarBookTXT.delete(0.0, END)
            sql = f"SELECT * FROM librarybooks WHERE BookName LIKE '%{FB__BookName}%'"
            self.mycursor.execute(sql)
            myresult = self.mycursor.fetchall()

            FinalDetails = f"Here are Books Similar to the\nBook Name you Entered:\n"
            self.FB_SimilarBookTXT.insert(INSERT, FinalDetails)
            for i in myresult:
                FinalDetails = f"{i[0]}\n"
                self.FB_SimilarBookTXT.insert(INSERT, FinalDetails)

            self.FB_NameOfBookVariable.set('')


if __name__ == '__main__':
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
