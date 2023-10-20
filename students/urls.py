from django.urls import path
from . import views

urlpatterns = [
    # url for index page
    path('', views.index, name='index'),
    # url for log out
    path('signout', views.signout, name='signout'),
    # url home view
    path('home', views.home, name='home'),
    # url for creating student
    path('student_registration', views.student_registration_form, name='student_registration'),
    # url to search for student
    path('search_student', views.search_student, name='search_student'),
    # url for updating student data
    path('<int:id>', views.student_registration_form, name='update'),
    # url for deleting student data
    path('delete<int:id>', views.remove_student, name='delete'),
    # url for view student in model
    path('view/<int:id>', views.view_student, name='view_student'),
    # url for viewing course and student tuition
    path('view_tuition', views.tuition_view, name='view_tuition'),
    # url for add student tuition payment record
    path('add_fees', views.add_fees, name='add_fees'),
    # url for displaying results
    path('Student_results', views.result_home, name='Student_results'),
    # url to search for student
    path('search_result', views.search_result, name='search_result'),
    # url for add results
    path('add_results', views.add_result, name='add_results'),
    # url for updating result
    path('update_result/<int:id>', views.add_result, name='update_result'),
    # url for deleting results
    path('delete_result/<int:id>', views.remove_result, name='delete_result'),    
    # url for viewing particular student result in modal
    path('view_result/<int:id>', views.view_result, name='view_result'),
]
