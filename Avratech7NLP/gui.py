from tkinter import *
from tkinter import messagebox
from get_data import get_clean_data

def run():

	messagebox.showinfo('The Label', get_clean_data(urlinp.get(),labelinp.get())[2])
	urlinp.delete ( 0, END )
	labelinp.delete(0, END)


root = Tk()
root.configure(bg='black')
root.title('NLP Avratech7')




host = Label(root, text='Host',bg='black', fg='red').grid(row=0, column=0, sticky=E)
db_name = Label(root, text='DB Name',bg='black', fg='red').grid(row=1, column=0, sticky=E)
user = Label(root, text='User',bg='black', fg='red').grid(row=2, column=0, sticky=E)
passowrd = Label(root, text='Passowrd',bg='black', fg='red').grid(row=3, column=0, sticky=E)


hostt = Entry(root, fg='red')
hostt.grid(row=0, column=1)
hostt.insert(10,'drona.db.elephantsql.com')
db_namet = Entry(root, fg='red')
db_namet.grid(row=1, column=1)
db_namet.insert(10,'lnhiqqex')
usert = Entry(root, fg='red')
usert.grid(row=2, column=1)
usert.insert(10,'lnhiqqex')
passowrdt = Entry(root, fg='red', show="*")
passowrdt.grid(row=3, column=1)
passowrdt.insert(10,'iP6W0C7_-6rsUI9dK7JN7WI6qxPVEx-q')



url = Label(root, text='URL', bg='black', fg='red').grid(row=4, column=0)
urlinp = Entry(root, width=40)
urlinp.grid(row=4, column=1, columnspan=2,pady=20)
label = Label(root, text='Label', bg='black', fg='red').grid(row=5, column=0)
labelinp = Entry(root)
labelinp.grid(row=5, column=1)

emp = Label(root, text='', bg='black', fg='red').grid(row=6, column=0)
ok = Button(root, text='OK',bg='green', command=run,width=10).grid(row=6, column=1)
exit = Button(root, text='Exit',bg='green', command=root.quit,width=10).grid(row=6, column=2)

root.geometry("300x250")

root.mainloop()


