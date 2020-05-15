from django.db import models
from django.urls import reverse

# Create your models here.

class Student(models.Model):
	COURSES=(
		('COMPUTER_SCIENCE','COMPUTER_SCIENCE'),
		('ENGINEERING','ENGINEERING'),
		('EDUCATION','EDUCATION'),
		('ECONOMIC','ECONOMIC'),
		('ARTS','ARTS'),
		('MEDICINE','MEDICINE'),
		)


	first_name=models.TextField(max_length=100)
	second_name=models.TextField(max_length=100)
	ref_number=models.TextField(unique=True,max_length=100)
	course=models.TextField(choices=COURSES)

	def __str__(self):
		return '{}   {}'.format(self.second_name,self.first_name)

	def get_absolute_url(self):
		return reverse('main:student-detail',kwargs={'pk':self.id})

