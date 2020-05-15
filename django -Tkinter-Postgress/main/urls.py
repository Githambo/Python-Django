from django.urls import path
from main import views

app_name='main'

urlpatterns=[
	path('',views.index,name="index"),
	path('newstudent',views.NewStudent.as_view(),name="add-student"),
	path('studentlist',views.StudentList.as_view(),name="student-list"),
	path('student/<int:pk>',views.StudentDetail.as_view(),name="student-detail"),
	path('student/<int:pk>/update',views.StudentUpdate.as_view(),name="student-update"),
	path('tkinter',views.tkinter_view,name="tk"),

	

]