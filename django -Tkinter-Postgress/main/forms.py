from django import forms
from main.models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields= ['first_name','second_name','ref_number','course']
		widgets={
		'first_name':forms.Textarea(attrs={'col':1,'rows':1}),
		'second_name':forms.Textarea(attrs={'col':1,'rows':1}),
		'ref_number':forms.Textarea(attrs={'col':1,'rows':1}),
		
		}