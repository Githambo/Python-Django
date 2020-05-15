import tkinter as tk
from main.backend import Database

database=Database("db.sqlite3")

window=tk.Tk()
window.title("Asset Manager")
window.geometry("850x520")
menu=tk.Menu(window)

menu.add_command(label="Addition",command=lambda:addition_frame())
menu.add_command(label="Search",command=lambda:search_frame())
menu.add_command(label="Records",command=lambda:records_frame())
menu.add_command(label="Order")
window.configure(menu=menu)

def addition_frame():
	options=("COMPUTERS","FURNITURES","SERVERS","OFFICE_EQUIPMENTS")

	first_name=tk.StringVar()
	second_name=tk.StringVar()
	ref_number=tk.StringVar()
	course=tk.StringVar()	

	ld=tk.Label(text="FIRST NAME:")
	ld.grid(row=0,column=0)
	ltag=tk.Label(text="SECOND NAME:")
	ltag.grid(row=1,column=0)
	lserial=tk.Label(text="REGISTRATION NUMBER:")
	lserial.grid(row=2,column=0)
	lcat=tk.Label(text="COURSE:")
	lcat.grid(row=3,column=0)
	
	
	first_name=tk.Entry(textvar=first_name,width=80)
	first_name.grid(row=0,column=1)	
	second_name=tk.Entry(textvar=second_name,width=80)
	second_name.grid(row=1,column=1)	
	ref_number=tk.Entry(textvar=ref_number,width=80)
	ref_number.grid(row=2,column=1)	
	course=tk.Entry(textvar=course,width=80)
	course.grid(row=3,column=1)	
	
	

	def insert_data():
		database.insert(first_name.get(),second_name.get(),ref_number.get(),course.get())

	submit_b=tk.Button(text="SUBMIT",width=10,command=insert_data)
	submit_b.grid(row=12,column=1)


def search_frame():
	frame1=tk.Frame(window,bg="blue",width=800,height=500,)	
	frame1.grid(row=0,column=1)	

def order_frame():
	frame1=tk.Frame(window,bg="red",width=800,height=500,)	
	frame1.pack(padx=20,pady=20)

def records_frame():	
	records=database.view()
	for data in records:
		print(data,'\n')


	l1=tk.Label(window,text=records)
	l1.grid()
window.mainloop()