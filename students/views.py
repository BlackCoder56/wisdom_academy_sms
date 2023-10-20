from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Student, Result, Course, Student_fees
from . forms import StudentForm, ResultForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    students = Student.objects.all()
    if request.user.is_authenticated:    
        return render(request, 'wisdom_academy/home.html', {'students': students})
    else:
         if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # messages.success(request, 'You have successfully logged in!')
                return redirect('home')
            else:
                messages.error(request, 'An error occurred please try again!')
                return redirect('home')
    return render(request, 'wisdom_academy/home.html',{'students': students})

# log out view
def signout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('index')

# student registration view
def student_registration_form(request, id=0): 
        
    if request.user.is_authenticated:        
        if request.method == "GET":
                if id == 0:
                    form = StudentForm()
                else:
                    student = Student.objects.get(pk=id)
                    form = StudentForm(instance=student)
                return render(request, 'wisdom_academy/student_registration.html',{'form':form})
        else:                
        
            if id == 0:
                form = StudentForm(request.POST)
            else:
                student = Student.objects.get(pk=id)
                form = StudentForm(request.POST, instance=student)
            
            if form.is_valid():
                form.save()           
                return redirect('home')
            return render(request, 'wisdom_academy/student_registration.html',{'form':form})
    else:
        messages.success(request, 'An error occurred. Please try again!')
        return redirect('student_registration')

# view to delete student record
def remove_student(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('home')
# view to display particular student data in modal basing on id
def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home'))
# view to search for student
def search_student(request):
    if request.method == "POST":
        searched = request.POST['searched']
        students = Student.objects.filter(student_name__contains=searched)
        return render(request, 'wisdom_academy/search_student.html', {'students': students})
    else:
        return redirect('home')

# view for result home page
def result_home(request):
    results = Result.objects.all()
    if request.user.is_authenticated:
        return render(request, 'Student_results/results.html', {'results':results})
    else:
        return redirect('home')       
    
# view to search for result
def search_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Student.objects.filter(student_name__contains=searched)
        return render(request, 'wisdom_academy/search_result.html', {'results': results})
    else:
        return redirect('Student_results')

# view to add result
def add_result(request, id=0):
    if request.user.is_authenticated:        
        if request.method == "GET":
            if id == 0:
                form = ResultForm()
            else:
                result = Result.objects.get(pk=id)
                form = ResultForm(instance=result)
            return render(request, 'Student_results/add_result.html',{'form':form})
        else:                
        
            if id == 0:
                form = ResultForm(request.POST)
            else:
                result = Result.objects.get(pk=id)
                form = ResultForm(request.POST, instance=result)            
            if form.is_valid():
                form.save()           
                return redirect('Student_results')
            return render(request, 'Student_results/add_result.html', {'form':form})
    else:
        messages.success(request, 'An error occurred. Please try again!')
        return redirect('add_results')
    
# view to delete result from db
def remove_result(request, id):
    results = Result.objects.get(pk=id)
    results.delete()
    return redirect('Student_results')

# view to display particular student result data
def view_result(request, id):
    results = Result.objects.get(pk=id)
    return HttpResponseRedirect(reverse('Student_results'))

# view to display student's tuition details
def tuition_view(request):
    if request.user.is_authenticated:
        courses = Course.objects.all()
        s_tuition = Student_fees.objects.all()
        studentt = Student.objects.all()
        
        return render(request, 'Student_tuition/tuition.html',{'s_tuition':s_tuition, 'courses':courses, 'studentt': studentt})
        
    else:
        return redirect('home')    
    
# view to search for tuition
def search_tuition(request):
    if request.method == "POST":
        searched = request.POST['searched']
        s_tuition = Student_fees.objects.filter(student_name__contains=searched)
        return render(request, 'wisdom_academy/search_result.html', {'s_tuition': s_tuition})
    else:
        return redirect('Student_results')
# view for adding student tuition record
def add_fees(request):
    # st_code = form.cleaned_data['code']
    # st_fee = form.cleaned_data['st_fees']    
    
    get_code = request.POST.get('code')
    get_paid = request.POST.get('st_fees')
    # student_data = Student.objects.filter(student_code = student_code).all()
    # student_data = Student.objects.filter(student_code = get_code).values()
    student_data =  Student.objects.values_list('student_name', flat=True).filter(student_code = get_code)
    # context = {
    #     'student_data': student_data,
    # }
    
    # for st_name in student_data:
    #     std_name = st_name.student_name
    # my_models = Student_fees.objects.filter(pk__in=set(student_data))
    
    string_name = str(student_data)
    
    form = Student_fees(request, student_code=string_name, paid=get_paid)   
    if request.method == 'POST':      
        if form.is_valid:        
            form.save()
        # fees = Student_fees.objects.create(student_code=student_code, paid=paid)
        return HttpResponseRedirect(reverse('view_tuition'))
       
    else:
       return render(request, 'Student_tuition/tuition.html')
    
    