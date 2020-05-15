from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from django.http import HttpResponse
import tkinter as tk

# Create your views here.
from main.forms import StudentForm
from main.models import Student
from main.backend import Database

def index(request):
	template_name='base.html'
	return render(request,template_name)

class NewStudent(CreateView):
	form_class=StudentForm
	template_name='main/add_student.html'

	def form_valid(self,request):
		if self.request.method=='POST':
			form=StudentForm(self.request.POST)
			if form.is_valid():
				form.save()
				return HttpResponse("Student Created Successfuly")
			return render(request,self.template_name,{'form':form})
		else:
			return render(request,self.template_name)

class StudentList(ListView):
	model=Student

class StudentDetail(DetailView):
	model=Student

class StudentUpdate(UpdateView):
	form_class=StudentForm
	model=Student
	template_name='main/s-update.html'

def tkinter_view(request):		
	database=Database("db.sqlite3")

	window=tk.Tk()
	window.title("Asset Manager")
	window.geometry("850x520")
	menu=tk.Menu(window)

	menu.add_command(label="Addition",command=lambda:addition_frame())
	
	window.configure(menu=menu)

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
	win=window.mainloop()

	return render(request,'base.html',{'win':win})
